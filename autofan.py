# google_route.py - 优化版主程序
import os
import sys
import json
import subprocess
import argparse
from urllib.request import urlopen

# 模块1: 网络接口工具 - 针对您的网络环境优化
def get_network_info():
    """
    获取网络适配器信息，专门筛选状态为"Up"的WLAN和手机网络适配器
    返回字典格式: { "wwan_index": int, "wwan_gateway": str, "wifi_index": int }
    """
    # 获取所有网络适配器信息
    cmd = (
        "Get-NetAdapter | "
        "Where-Object { ($_.Name -like '*WLAN*' -or $_.Name -like '*手机网络*') -and $_.Status -eq 'Up' } | "
        "Select-Object Name, InterfaceIndex, Status | "
        "ConvertTo-Json"
    )
    result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
    
    # 检查是否有输出
    if not result.stdout.strip():
        print("未找到活动的WLAN或手机网络适配器")
        return {"wwan_index": None, "wwan_gateway": None, "wifi_index": None}
    
    adapters = json.loads(result.stdout)
    network_info = {"wwan_index": None, "wwan_gateway": None, "wifi_index": None}
    
    print("检测到的活动适配器:")
    # 识别WWAN和WiFi适配器
    for adapter in adapters:
        adapter_name = adapter["Name"]
        if "vEthernet" in adapter_name:
            continue
        index = adapter["InterfaceIndex"]
        status = adapter["Status"]
        print(f"  - {adapter_name} (索引: {index}, 状态: {status})")

        if "手机网络" in adapter_name:
            network_info["wwan_index"] = index
            # 获取WWAN网关
            cmd = f"Get-NetRoute -InterfaceIndex {index} -DestinationPrefix '0.0.0.0/0' | Select-Object -ExpandProperty NextHop"
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
            network_info["wwan_gateway"] = result.stdout.strip()
            
        elif "WLAN" in adapter_name:
            network_info["wifi_index"] = index
    
    return network_info

# 模块2: Google IP管理
def download_google_ips(output_file="google_ips.txt"):
    """下载最新的Google IP地址范围并保存到文件"""
    try:
        # 从官方源获取IP列表
        with urlopen("https://www.gstatic.com/ipranges/goog.json") as response:
            data = json.load(response)
        
        # 提取IPv4范围
        ipv4_ranges = [prefix["ipv4Prefix"] for prefix in data["prefixes"] if "ipv4Prefix" in prefix]
        
        # 保存到文件
        with open(output_file, "w") as f:
            f.write("\n".join(ipv4_ranges))
        
        print(f"下载完成: 共获取 {len(ipv4_ranges)} 个Google IPv4地址范围")
        return True
    
    except Exception as e:
        print(f"下载失败: {str(e)}")
        return False

# 模块3: 路由配置
def configure_routing(ip_file, wwan_gateway, wwan_index):
    """配置路由规则：Google流量走WWAN，其他走WiFi"""
    # 清除旧路由
    with open(ip_file, "r") as f:
        for line in f:
            cidr = line.strip()
            if cidr:
                continue# test: 暂时不移除
                os.system(f'powershell -Command "Remove-NetRoute -DestinationPrefix {cidr} -Confirm:$false "')
    
    # 添加新路由
    count = 0
    with open(ip_file, "r") as f:
        for line in f:
            cidr = line.strip()
            if cidr:
                cmd = (
                    f'New-NetRoute -DestinationPrefix {cidr} '
                    f'-NextHop {wwan_gateway} '
                    f'-InterfaceIndex {wwan_index} '
                    '-RouteMetric 500 '
                )
                os.system(f'powershell -Command "{cmd}"')
                count += 1
    
    # 确保默认路由使用WiFi
    net_info = get_network_info()
    if net_info["wifi_index"]:
        os.system(f'powershell -Command "Set-NetIPInterface -InterfaceIndex {net_info["wifi_index"]} -InterfaceMetric 10"')
    
    print(f"\n路由配置完成: 共添加 {count} 条Google路由规则")
    print(f"• Google流量 → WWAN (网关: {wwan_gateway}, 接口索引: {wwan_index})")
    print("• 其他流量 → WiFi")

# 模块4: 验证工具
def verify_configuration():
    """验证路由配置是否正确"""
    print("\n验证路由配置:")
    
    # 显示活动适配器
    net_info = get_network_info()
    
    # 测试Google流量
    print("\n测试Google流量 (应走WWAN):")
    os.system('tracert -d www.google.com')
    
    # 测试非Google流量
    print("\n测试非Google流量 (应走WiFi):")
    os.system('tracert -d www.microsoft.com')
    
    # 显示部分Google路由
    print("\nGoogle路由规则:")
    os.system('powershell -Command "Get-NetRoute | Where-Object { $_.DestinationPrefix -like \'*google*\'-or $_.DestinationPrefix -like \'*gstatic*\' } | Format-Table DestinationPrefix, NextHop, InterfaceAlias, RouteMetric"')

# 模块5: 计划任务管理
def setup_scheduled_task():
    """创建Windows计划任务自动更新路由"""
    script_path = os.path.abspath(__file__)
    ps_script = f'''
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "\\"{script_path}\\" --apply"
$trigger = New-ScheduledTaskTrigger -Daily -At 3am
$settings = New-ScheduledTaskSettingsSet -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName "UpdateGoogleRoutes" -Action $action -Trigger $trigger -Settings $settings -Description "自动路由Google流量到WWAN" -RunLevel Highest
'''
    
    with open("create_task.ps1", "w") as f:
        f.write(ps_script)
    
    os.system('powershell -ExecutionPolicy Bypass -File create_task.ps1')
    os.remove("create_task.ps1")
    print("计划任务已创建: 每天凌晨3点自动更新路由")

# 主程序
def main():
    parser = argparse.ArgumentParser(description="Google流量分流工具")
    parser.add_argument("--setup", action="store_true", help="初始设置（下载IP列表并配置路由）")
    parser.add_argument("--apply", action="store_true", help="应用路由配置（需管理员权限）")
    parser.add_argument("--verify", action="store_true", help="验证当前路由配置")
    parser.add_argument("--task", action="store_true", help="创建计划任务")
    parser.add_argument("--clean", action="store_true", help="清除所有Google路由规则")
    parser.add_argument("--list", action="store_true", help="列出活动网络适配器")
    args = parser.parse_args()

    # 检查管理员权限
    if any([args.setup, args.apply, args.task, args.clean]):
        try:
            result = subprocess.run(["net", "session"], capture_output=True, text=True)
            if result.returncode != 0:
                print("请以管理员身份运行此程序")
                return
        except:
            print("管理员权限检查失败")
            return

    # 执行相应操作
    if args.setup:
        if not download_google_ips():
            return
        net_info = get_network_info()
        if net_info["wwan_gateway"] and net_info["wwan_index"]:
            configure_routing("google_ips.txt", net_info["wwan_gateway"], net_info["wwan_index"])
            setup_scheduled_task()
        else:
            print("无法获取WWAN网络信息，请确保已连接移动网络")

    elif args.apply:
        net_info = get_network_info()
        if net_info["wwan_gateway"] and net_info["wwan_index"]:
            configure_routing("google_ips.txt", net_info["wwan_gateway"], net_info["wwan_index"])
        else:
            print("无法获取WWAN网络信息")

    elif args.verify:
        verify_configuration()

    elif args.task:
        setup_scheduled_task()

    elif args.clean:
        with open("google_ips.txt", "r") as f:
            for line in f:
                cidr = line.strip()
                if cidr:
                    os.system(f'powershell -Command "Remove-NetRoute -DestinationPrefix {cidr} -Confirm:$false"')
        print("已清除所有Google路由规则")
    
    elif args.list:
        print("\n活动网络适配器:")
        net_info = get_network_info()
        print(f"WLAN接口索引: {net_info.get('wifi_index', '未找到')}")
        print(f"WWAN接口索引: {net_info.get('wwan_index', '未找到')}")
        print(f"WWAN网关地址: {net_info.get('wwan_gateway', '未找到')}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
    # get_network_info()  # 测试网络适配器信息获取
    # download_google_ips()
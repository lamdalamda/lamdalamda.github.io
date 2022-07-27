---
layout: page
title: "Deploy  Guide"
permalink: /deploy/
---

相关文件在deploy_guide repo里

* TOC
{:toc}


**转载侵删**


# Hardware 硬件


## e5 鸡血 @ z10pa


烧录器装好驱动https://item.taobao.com/item.htm?spm=a1z09.2.0.0.68162e8dApTxX1&id=592580392777&_u=n1ucmpp9f1e3
取下BIOS芯片，按照商家页面把bios芯片夹住，然后连usb。打开软件之后，先检测烧录器，然后打开鸡血bios （.cap），先擦除再写入（不知道需不需要擦除）。

电脑需要拔下电池，跳线到cmos重置模式半小时以上


刷好的bios芯片对着缺口插回去，尝试安装系统发现不可以用（卡在win10logo），于是在别的电脑上安装系统之后插回来，还是卡在了win10的logo。 重启三次之后进入安全模式选择禁用驱动程序强制签名，成功进去系统。

此时电脑上面是两个cpu，4条内存，一个nvme硬盘，连接了板载显卡，没有插独显

以这种方式进去系统之后，在系统里面双击win10安装程序，删除所有个人文件重装系统，安装完后系统正常工作，重启之后也正常

可以参考https://www.bilibili.com/read/cv4116433

之后是电源选择高性能，关闭快速启动，bios设定里面c state limie 设置成c0、c1，开启c3 report,禁用c6 report

再之后，格式化一个u盘，把  v3.efi 和 start.nsh放进去，引导这个优盘，让优盘把v3 efi相当于复制进系统的efi分区即可

**未证实：**
似乎刷回5.4kernel之后，系统会卸载微码补丁，此时频率会经常达到3以上。而新版kernel似乎会安装intel microcode，导致破解失效？？


### 双路设置：

只在1路插内存：即32g内存都在cpu1上面，cpuz跑分15w+

两路都插内存，总共64g，跑分10w

开启关闭虚拟化都是这样

关闭numa之后跑分回到15w+

而且在wsl相关性设置中，cpu 组1 变成了64个cpu，组2只有8个？？？？
原本是平均分配的

-->可以通过重启虚拟机解决

```
net stop LxssManager 
net start LxssManager
```



## zbook17 changing to DC screen 换屏幕

https://forum.51nb.com/thread-1966563-1-1.html

2020.9新帖子，改30针屏线，没准可行！

目前已有是40针屏线，具有2lane定义，查看b173han04.0 和04.7似乎符合 40pin 2lane 

## nvme support

参照https://tieba.baidu.com/p/6282527282?see_lz=1
过程，使用clover来进行
先把原本硬盘数据备份到新盘，再备份回这个m.2
bios设置：
制作了clover的启动盘，可以加载nvme驱动并且引导系统
尝试把clover放进硬盘里面:

方法，对于目前的GPT硬盘，直接把EFI分区清空之后把200M的clover盘中文件全考进去，重启之后bios可以识别这个uefi并且引导出来就是clover



# MacOS系统问题

## 账户无法使用

绑定银行卡之后再itunes里面激活

## 其他一些问题
m1的yml和其他yml不太通用


# Linux系统设置

## 安装5.4 kernel
```{markdown}
sudo apt-get update
sudo apt-get upgrade
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-headers-5.4.0-050400_5.4.0-050400.201911242031_all.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-headers-5.4.0-050400-generic_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-headers-5.4.0-050400-lowlatency_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-image-unsigned-5.4.0-050400-generic_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-image-unsigned-5.4.0-050400-lowlatency_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-modules-5.4.0-050400-generic_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-modules-5.4.0-050400-lowlatency_5.4.0-050400.201911242031_amd64.deb
sudo dpkg -i *.deb
```
## 安装5.11 kernel
```{markdown}
sudo apt-get update
sudo apt-get upgrade
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.11/amd64/linux-headers-5.11.0-051100-generic_5.11.0-051100.202102142330_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.11/amd64/linux-headers-5.11.0-051100-lowlatency_5.11.0-051100.202102142330_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.11/amd64/linux-headers-5.11.0-051100_5.11.0-051100.202102142330_all.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.11/amd64/linux-image-unsigned-5.11.0-051100-generic_5.11.0-051100.202102142330_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.11/amd64/linux-image-unsigned-5.11.0-051100-lowlatency_5.11.0-051100.202102142330_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.11/amd64/linux-modules-5.11.0-051100-generic_5.11.0-051100.202102142330_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.11/amd64/linux-modules-5.11.0-051100-lowlatency_5.11.0-051100.202102142330_amd64.deb
sudo dpkg -i *.deb
```
## basic linux command：

su / sudo ：管理员权限

sh xxxxx.sh :运行sh脚本

yum install / apt-get install : centos 和 ubuntu安装软件

scp （-r） 本地 目标： 可以复制到远程主机

注意！ 远程主机的.bashrc不可以有echo

pwd显示路径

`top`
查看cpu使用率

`top -u david`
查看用户的cpu使用率


`cat /proc/cpuinfo`
查看cpu型号核心数量

`s-tui`
很好用的检测软件

## basic library

- ubuntu 18.04:

`apt-get install build-essential gcc-multilib rpm lib32ncurses5 lib32z1`

- ubuntu 20.04

`apt-get install build-essential gcc-multilib rpm lib32z1`


## ubuntu18.04 root 登陆

https://blog.csdn.net/COCO56/article/details/107628019



## 隔离部分cpu使其只用来运行部分任务
对于z10pa可以打开
`gedit /etc/default/grub`
更改：
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash isolcpus=2-17,20-35"
```
之后
`sudo update-grub`

重启之后可以通过资源管理器看，如果一直是0%说明成功

调度被隔离的核心：

使用taskset
例如：

`taskset -c 2-17,20-35 mpirun -n 32 vasp`

这样也可以开启numa然后只在一个numa节点上运行程序


## 系统监测：

千万不要用aida64，会导致功耗bug

使用hwinfo


# windows的一些系统设置


## Driver 安装驱动的那些事
### 声卡soundblaster

安装soundblaster xfi notebook （SB0950）:
下载
https://files.creative.com/manualdn/Drivers/AVP/10925/0x2F4D4864/SBXN_PCDRV_LB_1_01_0095.exe
注意：**安装时候卸载ESET等任何杀毒软件！**

### install graphic card driver for unsupported graphic card 安装显卡驱动 zbook17

zbook17显卡：
根据网上，只支持到p5200?

更换--》简单，用热风枪吹掉显卡支架，
记得bios开启混合显卡模式

驱动：
直接下载最新exe驱动，右键解压，卸载所有nvidia驱动，用driver cleaner再清除一遍，然后设备管理器-microsoft基本适配器
然后安装，从磁盘安装，找到那个inf（是bli结尾的？）。我是安装之前改好了inf，不确定需不需要改inf

inf更改：
首先设备管理器找到显卡硬件id，然后再nVidia驱动解压出来的文件里面 找惠普对应的（103C结尾，应该是bli之类的inf）
禁用设备签名（设置里面，恢复，高级重新启动），然后inf右键安装

### killer ax200

https://bbs.luobotou.org/thread-45955-1-1.html11



## 开启远程桌面:

文件资源管理器,右键此电脑,跳出来设置的窗口,在相关设置里面有远程桌面,点进去打开

## windows照片查看器

保存成reg文件双击运行

```markdown
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations]
 ".jpg"="PhotoViewer.FileAssoc.Tiff"
 ".jpeg"="PhotoViewer.FileAssoc.Tiff"
 ".bmp"="PhotoViewer.FileAssoc.Tiff"
 ".png"="PhotoViewer.FileAssoc.Tiff"
 ".ico"="PhotoViewer.FileAssoc.Tiff"
 ".jpe"="PhotoViewer.FileAssoc.Tiff"
 ".dib"="PhotoViewer.FileAssoc.Tiff"
 ".jfif"="PhotoViewer.FileAssoc.Tiff"
 ".wdp"="PhotoViewer.FileAssoc.Tiff"
```

## a script for running android simulator 安卓模拟器等可以尝试

启用：
```markdown

bcdedit /set hypervisorlaunchtype off
```

恢复：
```markdown

bcdedit /set hypervisorlaunchtype off
```


# wsl的基本设置

## 双路主机：

可以任务管理器右键vmmm选择让wsl运行在哪个cpu上面

新发现：当关闭超线程之后，wsl可以同时在两个cpu中运行

注意可能需要重新安装libintel64？

性能测试

## root 权限

 `ubuntu1804.exe config --default-user root` 

打不开的时候：netsh winsock reset

## 重启wsl

`net stop LxssManager`
`net start LxssManager`

## WSl的linux GUI
GUI-xfce
https://zhuanlan.zhihu.com/p/150555651
RDP:
https://zhuanlan.zhihu.com/p/149501381
显示GUI

**某个具体过程（通过xfce4实现）**

`sudo apt-get install xfce4`

.bashrc中添加：

`export DISPLAY=:0.0`


之后下载并安装 VcXsrv Windows X Server

https://sourceforge.net/projects/vcxsrv/

Windows X-server based on the xorg git sources (like xming or cygwin's xwin), but compiled with Visual C++ 2012 Express Edition. Source code can also be compiled with VS2008, VS2008 Express Edition and VS2010 Express Edition, although current project and makefile are not fully compatible anymore.

 先启动 XLaunch

 再在 WSL 中启动 Xfce 会话

`startxfce4`


最好用centos或者ubuntu18.04

## 远程桌面连接linux
sudo apt install xrdp
sudo systemctl enable --now xrdp
sudo ufw allow from 192.168.3.0/24 to any port 3389 proto tcp






# 基础软件


## VMware
### 虚拟机的ssh注意事项，对于vmware虚拟机

安装vmhs-fuge还是啥的，为了虚拟机与实体机通信

虚拟机可以尝试使用固定ip

### vmware vmhs-fuge 使用的一些常用指令
访问硬盘用的
`/usr/bin/vmhgfs-fuse .host:/ /mnt/hgfs -o subtype=vmhgfs-fuse,allow_other`


## SSH设置操作

### ssh-server
LINUX默认没有ssh-server，也就是说默认不能作为ssh的目标

需要安装openssh-server

`sudo apt-get install openssh-server`

###  SSH config 文件示例


```{markdown}

Host vm
    HostName 192.168.254.128
    User root
    IdentityFile "C:\Users\（改成用户名）\.ssh\id_rsa"

```


### ssh免密码登录


(windows必须)首先在service服务中，打开openssh，自动启动

- 生成ssh密钥
（可能需要先cd到~/.ssh再生成，因为ssh-keygen的-f有点傻）


`ssh-keygen -t rsa -f ~/.ssh/${密钥名字}`

- 将密钥放到远程主机

生成两个文件，把.pub放到远程机器的/.ssh下面，再把内容复制到远程主机的~/.ssh/authorized_keys里面

```
scp ~/.ssh/${密钥名字}.pub (用户名)@(远程主机):~/.ssh/

ssh登录远程主机之后

cat ~/.ssh/${密钥名字}.pub >> ~/.ssh/authorized_keys
```

之后windows机器ssh-add 私钥名字,或者在~/.ssh的config里面写好

**注意authorized keys里面每个主机只能有一个密钥**

### ssh映射磁盘

安装直接前往 github 对应项目的 release 中下载最新版本即可，需注意 sshfs-win 对 winfsp 的最低版本依赖（下载最新版本一般即可满足），另外有GUI（用户图形操作界面）可供下载

sshfs-win：https://github.com/billziss-gh/sshfs-win/releases

winfsp：https://github.com/billziss-gh/winfsp/releases

然后映射网络磁盘里面输入

\\sshfs\用户名@服务器名字\ 

后面不用加\home啥的，过去就相当于在\home\用户名底下

如果想要上层的话也可以

\\sshfs.r\用户名@服务器名字\home\用户名\.......

sshfs相当于省略\home\用户名的过程



## git & github

对于新的os需要对git以及github进行设置

`git config --global user.name "lamdalamda"`

`git config --global user.email "邮箱"`

### github ssh

`ssh-keygen -t ed25519 -C "email address"`

`ssh-add ~/.ssh/id_ed25519`

再把pubkey复制到GitHub 设置里面的ssh keys里

之后可以进行正常使用

### github clone

对于需要pull 或者 push 到github的
如果是在vscode里面打开在点击pull或者push时候github扩展会跳出来打开chrome要求验证
也可以使用ssh登录，比较费劲

命令示例：
`git clone git@github.com:lamdalamda/deploy_guide.git`

### GitHub page

一般是在settings-page里面设定source在/docs 下面，然后建立docs文件夹，放进去index.html

如果用index.md使用markdown渲染出来，注意使用vscode插件markdown math和markdown preview enhanced

渲染出来html的话，在GitHub page上面不能显示正确的数学公式，需要在在<head>部分把原本的stylesheet部分换成以下代码
```markdown

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.css" integrity="sha384-yFRtMMDnQtDRO8rLpMIKrtPCD5jdktao2TV19YiZYWMDkUR5GQZR/NOVTdquEx1j" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.js" integrity="sha384-9Nhn55MVVN0/4OFx7EE5kpFBPsEMZxKTCnA+4fqDmg12eCTqGi6+BB2LjY8brQxJ" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body);"></script>
```

这段代码会更新

_https://katex.org/docs/autorender.html_



### github page 目录

使用toc.py 搬运自https://github.com/Higurashi-kagome/pythontools/blob/master/text/toc.py

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

## python 

先装好anaconda

### environment 环境相关

- 默认环境
在bashrc里添加
`conda activate environment name`

- export the environment 导出环境:

`conda env export --name research > research.yml`


- import environment from yml file 导入环境:

`conda env create -f environment.yml`

- a sample

https://github.com/lamdalamda/system-configure-record/blob/master/CARE/research.yml

### library 库
#### tensorflow:
- tensorflow windows 
假设tensorflow安装在D:\Anaconda3\Lib\site-packages\tensorflow环境里，那么打开D:\Anaconda3\Lib\site-packages\tensorflow\python\platform\build_info.py这个文件

检查一下默认写好的系统变量CUDA_PATH和CUDA_PATH_V9.0是否无误


检查一下系统变量path中是否有NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin和NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64并且正确。
默认路径如下：
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64

直接pip install tensorflow就行，有错误改错误

tensorflow-cuda：需要找到tensorflow对应的cuda，cudnn

下载下来之后安装，放在环境变量里面，缺什么加什么
官网版本未必对应，可以看安装后缺少的dll版本

- test code for tensorflow tensorflow测试

```markdown
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

### 实例

- 监控网站信息变化，比如托福或者疫苗等

同时具有发送邮件提醒功能

https://www.jianshu.com/p/7c4f251485b7?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation


## LMOD - module 管理软件
- lua
  
```{markdown}
sudo apt install lua5.3 lua-bit32:amd64 lua-posix:amd64 lua-posix-dev liblua5.3-0:amd64 liblua5.3-dev:amd64 tcl tcl-dev tcl8.6 tcl8.6-dev:amd64 libtcl8.6:amd64

sudo update-alternatives --install /usr/bin/lua \
    lua-interpreter /usr/bin/lua5.3 130 \
    --slave /usr/share/man/man1/lua.1.gz lua-manual \
    /usr/share/man/man1/lua5.3.1.gz
sudo update-alternatives --install /usr/bin/luac \
    lua-compiler /usr/bin/luac5.3 130 \
    --slave /usr/share/man/man1/luac.1.gz lua-compiler-manual \
    /usr/share/man/man1/luac5.3.1.gz
sudo ln -s /usr/lib/x86_64-linux-gnu/liblua5.3-posix.so \
    /usr/lib/x86_64-linux-gnu/lua/5.3/posix.so
```
- lmod

下载lmod本体

```{markdown}
./configure --prefix=/opt/apps
sudo make install
sudo ln -s /opt/apps/lmod/lmod/init/profile        /etc/profile.d/z00_lmod.sh

```
之后：
`sudo gedit /etc/bash.bashrc`
添加这些：

```{markdown}
if ! shopt -q login_shell; then
  if [ -d /etc/profile.d ]; then
    for i in /etc/profile.d/*.sh; do
      if [ -r $i ]; then
        . $i
      fi
    done
  fi
fi
```

- oneapi的module
在oneapi根目录下面运行

```{markdown}
./modulefiles-setup.sh
module use modulefiles
```

- nvhpc
nvhpc的modulefile在安装目录的modulefiles里面


## easybuild

安装好lmod之后

```{markdown}
export EB_TMPDIR=/tmp/$USER/eb_tmp
python3 -m pip install --ignore-installed --prefix $EB_TMPDIR easybuild
export PATH=$EB_TMPDIR/bin:$PATH
export PYTHONPATH=$(/bin/ls -rtd -1 $EB_TMPDIR/lib*/python*/site-packages | tail -1):$PYTHONPATH
export EB_PYTHON=python3
eb --install-latest-eb-release --prefix $HOME/easybuild
module use $HOME/easybuild/modules/all
```
重启清除tmp，之后module load Easybuild使用

## spack

spack find -v

可以列出已经安装的包的完整名称，之后load

### spack 镜像
在没有外网链接的系统上尝试使用spack

1. 在有外网连接的机器上创建镜像

`spack mirror create -d ~/spack_mirror -D nvhpc@20.9 openmpi fftw clingo `

其中-d后面是创建镜像的位置，-D是包括所有的denpendency，后面是包的名称
注意clingo是必须
将得到的镜像文件夹上传到没有外网链接的机器

### NSCC
- spack初始化
必备条件：python3.8+ gcc6+

nscc上面：module load gcc/6.5.0 python/3.8.3

`ssh nscc04-ib0`来获得外网连接

之后`spack --insecure -d install zlib`



## ROCm
### 4.3
amd gpu加速通过ROCm实现（类似CUDA）

这次直接登陆的root来安装的：

首先安装ROCm 4.3在ubuntu20.04.在安装系统时候不安装图形驱动：

这里logname改称用户名

```
sudo usermod -a -G video $LOGNAME
sudo usermod -a -G render $LOGNAME

echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf

echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf

echo 'EXTRA_GROUPS=render' | sudo tee -a /etc/adduser.conf

sudo apt update

sudo apt dist-upgrade

sudo apt install libnuma-dev
sudo apt install wget gnupg2

wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -

echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.3/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list

sudo apt update
sudo apt install rocm-dkms 

echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin' | sudo tee -a /etc/profile.d/rocm.sh

```

重启系统之后

验证安装使用：

/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo



- 数学lib
注意一定要在最后安装

`sudo apt-get install rocm-libs`

### 5.0.1

5.0.1 要求5.8或者5.11kernel
根据文档，如果想要安装多个rocm版本的话，需要先安装最新的。比如想要安装5.0.1和4.1，那么需要先安装5.0.1

首先移除了所有的旧版软件，然后安装5.11kernel

```
sudo apt-get update

wget https://repo.radeon.com/amdgpu-install/21.50.1/ubuntu/bionic/amdgpu-install_21.50.1.50001-1_all.deb

sudo apt-get install ./amdgpu-install_21.50.1.50001-1_all.deb 

```

修改rocm list文件：
`sudo gedit /etc/apt/sources.list.d/rocm.list`
添加这些内容
```
deb [arch=amd64] https://repo.radeon.com/rocm/apt/5.0.1 ubuntu main
deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.1.1 xenial main
```
然后
```
sudo apt update
sudo amdgpu-install --usecase=rocm --rocmrelease=4.1.1
sudo amdgpu-install --usecase=rocm --rocmrelease=5.0.1
```

会报错说需要modules-extra

尝试用“新立德软件管理器“搜索5.11.0-46，除了unsigned image和nvidia相关的都安装

发现使用low latency kernel还是会报错，必须使用generic
使用generic之后成功

安装4.1.1时候正常，但是安装5.0.1时候出现一个comgr冲突，可能是旧版的comgr没卸载干净
卸载之后重新安装可能会有问题，重启一下然后`sudo apt-get autoremove`

但是4.5.0开始不支持gfx803,所以只是用那个package manager方便

最好直接修改/etc/apt/sources.list.d/rocm.list
```
deb [arch=amd64] https://repo.radeon.com/rocm/apt/5.0   ubuntu main
deb [arch=amd64] https://repo.radeon.com/rocm/apt/5.0.1   ubuntu main
deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.3   ubuntu main
deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.1   xenial main
deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.1.1   xenial main
deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.5  ubuntu main


```





```
sudo apt-get update

wget https://repo.radeon.com/amdgpu-install/21.50/ubuntu/focal/amdgpu-install_21.50.50000-1_all.deb

sudo apt-get install ./amdgpu-install_21.50.50000-1_all.deb

echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/5.0   ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/5.0.1   ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.1   xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.3   ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.5   ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.1.1   xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list



sudo amdgpu-install --usecase=rocm --rocmrelease=5.0.0
sudo amdgpu-install --usecase=rocm --rocmrelease=4.3.0

```


### 4.1

- 安装kernel
rocm4.1需要linux 5.4kernel（或者5.6？）

经过测试这样安装kernel
```{markdown}
sudo apt-get update
sudo apt-get upgrade
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-headers-5.4.0-050400_5.4.0-050400.201911242031_all.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-headers-5.4.0-050400-generic_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-headers-5.4.0-050400-lowlatency_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-image-unsigned-5.4.0-050400-generic_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-image-unsigned-5.4.0-050400-lowlatency_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-modules-5.4.0-050400-generic_5.4.0-050400.201911242031_amd64.deb
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.4/linux-modules-5.4.0-050400-lowlatency_5.4.0-050400.201911242031_amd64.deb
sudo dpkg -i *.deb
```
然后需要将其他rocm卸载干净
```
sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils && sudo reboot
sudo apt-get purge rocm-libs
```
安装过程：
```
sudo apt update

sudo apt dist-upgrade

sudo apt install libnuma-dev

sudo reboot
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -

echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.1/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin' | sudo tee -a /etc/profile.d/rocm.sh

sudo apt install rocm-dkms && sudo reboot
```
- 手动安装hip (大可不必,因为已经给安装好了)
```
git clone -b roc-4.1.x https://github.com/RadeonOpenCompute/llvm-project.git
cd llvm-project
mkdir -p build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=1 -DLLVM_TARGETS_TO_BUILD="AMDGPU;X86" -DLLVM_ENABLE_PROJECTS="clang;lld;compiler-rt" ../llvm
make -j
sudo make install
```
- ROCM device (用来cmake的？)
```
export PATH=/opt/rocm/llvm/bin:$PATH
git clone -b roc-4.1.x https://github.com/RadeonOpenCompute/ROCm-Device-Libs.git
cd ROCm-Device-Libs
mkdir -p build && cd build
CC=clang CXX=clang++ cmake -DLLVM_DIR=/opt/rocm/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_WERROR=1 -DLLVM_ENABLE_ASSERTIONS=1 -DCMAKE_INSTALL_PREFIX=/opt/rocm ..
make -j
sudo make install
```

- 数学lib
注意一定要在最后安装

`sudo apt-get install rocm-libs`



## PBS/qsub 队列--目前未成功

安装PBS 队列管理；

git clone git@github.com:openpbs/openpbs.git

按照install操作
configure之前conda deactivate

安装libpython3.6
`sudo add-apt-repository universe`

`sudo apt-get update`

`sudo apt-get install libpython3.6`

安装libhwloc5

`wget http://ftp.de.debian.org/debian/pool/main/h/hwloc/libhwloc5_1.11.12-3_amd64.deb`

`sudo dpkg -i libhwloc5_1.11.12-3_amd64.deb`

然后运行两次：
`sudo dpkg -i openpbs-server_20.0.1-1_amd64.deb `

### 源代码安装-未成功
 github上下载master源码（20.0.1还没有ubutnu20.04支持，如果是ubuntu18.04那直接找安装包就行）
 
 安装依赖
    sudo apt-get install gcc make libtool libhwloc-dev libx11-dev \
      libxt-dev libedit-dev libical-dev ncurses-dev perl \
      postgresql-server-dev-all postgresql-contrib python3-dev tcl-dev tk-dev swig \
      libexpat-dev libssl-dev libxext-dev libxft-dev autoconf \
      automake g++
 
 sudo apt install expat libedit2 postgresql python3 postgresql-contrib sendmail-bin \
      sudo tcl tk libical3 postgresql-server-dev-all
 
 
 之后./autogen
 
 然后 ./configure CFLAGS="-g -O2 -Wall -Werror -Wno-unused-result -Wno-array-bounds -Wno-stringop-overflow -Wno-format-truncation -Wno-format-overflow" --prefix=/opt/pbs
 
 make 
 
 sudo make install




## zotero

- zotero 批量合并重复条目
https://github.com/frangoud/ZoteroDuplicatesMerger
下载安装之后,zotero中最左侧导航栏里面有duplicates items,选中之后会显示所有的重复项目.然后右键duplicate merger -> bulk merge还是啥的.就可以合并了


- citation

https://marketplace.visualstudio.com/items?itemName=mblode.zotero

这个是用vscode写latex时候用来插入引文的插件.暂时还不知道该怎么用


## latex 配置
### latex中文支持
参考https://zhuanlan.zhihu.com/p/43133114


对于latex workshop插件，在visual studio code的settings.json 里面添加如下内容

```markdown
    // Latex workshop
    "latex-workshop.latex.tools": [
          {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "%DOC%"
            ]
          },
          {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
              ]
          },          
          {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
            ]
          },
          {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
            "%DOCFILE%"
            ]
          }
        ],
    "latex-workshop.latex.recipes": [
          {
            "name": "xelatex",
            "tools": [
            "xelatex"
                        ]
                  },
          {
            "name": "latexmk",
            "tools": [
            "latexmk"
                        ]
          },

          {
            "name": "pdflatex -> bibtex -> pdflatex*2",
            "tools": [
            "pdflatex",
            "bibtex",
            "pdflatex",
            "pdflatex"
                        ]
          }
        ],
    "latex-workshop.view.pdf.viewer": "tab",  
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log",
        "*.fdb_latexmk"
      ]
```

2022-04-02:

在苹果上面好像没没法正常运行,改了一下recipe,变成这个样子
```

"latex-workshop.latex.tools": [
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-pdf",
      "%DOC%"
      ]
    },
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "%DOC%"
        ]
    },          
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "%DOC%"
      ]
    },
    {
      "name": "bibtex",
      "command": "bibtex",
      "args": [
      "%DOCFILE%"
      ]
    }
  ],
"latex-workshop.latex.recipes": [
  
    {
      "name": "xelatex",
      "tools": [
      "xelatex",
      "bibtex",
      "xelatex",
      "xelatex",
                  ]
            },
    {
      "name": "latexmk",
      "tools": [
      "latexmk"
                  ]
    },

    {
      "name": "pdflatex -> bibtex -> pdflatex*2",
      "tools": [
      "pdflatex",
      "bibtex",
      "pdflatex",
      "pdflatex"
                  ]
    }
  ],
```


## slurm队列管理

在slurm官网下载配置文件放到/etc/slurm-llvm/中
 
 然后
```{markdown}
sudo apt install slurm-wlm-torque
sudo apt install slurm-wlm-emulator

 systemctl start munge
systemctl status munge

systemctl enable munge
```
 
 
## 看番-animesearcher

https://github.com/zaxtyson/AnimeSearcher

可以git下来源代码使用

### 搜索不到东西等问题

git下来源代码，config里面更改一下端口之后，python运行app.py,之后记得在打开html之后在最底下更改app.py中的地址
 

 



# 不好装的软件
## quantum espresso 
### quantum espresso普通编译-已经成功
只需要按照操作说明来


### quantum espresso ROCm-sirius

quantum  espresso 的gpu实现使用sirius。 
sirius手动安装方式：

由于sirius的依赖太复杂，所以可以在spack里面安装sirius然后加载依赖，再手动安装

在spack安装一遍sirius+rocm之后

在不加载intel oneap：
```
module load libxc-5.1.5-gcc-9.3.0-hh5tyyd 
module load spfft-1.0.4-gcc-9.3.0-uxhem63  
module load hdf5-1.10.7-gcc-9.3.0-rb5rztf 
module load gsl-2.7-gcc-9.3.0-jrey7js
module load spglib-1.16.1-gcc-9.3.0-vhsoqdf
module load spla-1.5.1-gcc-9.3.0-k4ifbob
module load openblas-0.3.18-gcc-9.3.0-5p72oue
module load fftw-3.3.10-gcc-9.3.0-75kqnix 
```
在sirius里面
```
mkdir build
cd build
cmake -DUSE_ROCM=on -DUSE_OPENMP=on ..
make -j4
```

### quantum espresso ROCm-spack安装--目前未成功

在整个安装过程中还跑了这些指令

```
apt-get install build-essential gcc-multilib rpm lib32z1
apt-get install gfortran
apt-get install hipfort


. ~/repo/spack/share/spack/setup-env.sh
spack install zlib
spack install gcc
spack install sirius +rocm amdgpu_target=gfx803
```

另外注意更改spack的配置文件

~/.spack/packages.yaml
```

packages:
  hip:
    externals:
    - spec: hip@4.3.0
      prefix: /opt/rocm/hip
      extra_attributes:
        compilers:
          c: /opt/rocm/llvm/bin/clang++
          c++: /opt/rocm/llvm/bin/clang++
          hip: /opt/rocm/hip/bin/hipcc
      buildable: false
  hsa-rocr-dev:
    externals:
    - spec: hsa-rocr-dev@4.3.0
      prefix: /opt/rocm
      extra_attributes:
        compilers:
          c: /opt/rocm/llvm/bin/clang++
          cxx: /opt/rocm/llvm/bin/clang++
      buildable: false
  llvm-amdgpu:
    externals:
    - spec: llvm-amdgpu@4.3.0
      prefix: /opt/rocm/llvm
      extra_attributes:
        compilers:
          c: /opt/rocm/llvm/bin/clang++
          cxx: /opt/rocm/llvm/bin/clang++
      buildable: false


```

~/.spack/linux/compilers.yaml

```
compilers:
- compiler:
    spec: clang@amd
    paths:
      cc: /opt/rocm/llvm/bin/clang
      cxx: /opt/rocm/llvm/bin/clang++
      f77: null
      fc: null
    flags: {}
    operating_system: ubuntu20.04
    target: x86_64
    modules: []
    environment: {}
    extra_rpaths: []
- compiler:
    spec: clang@13.0.0
    paths:
      cc: /usr/bin/clang-ocl
      cxx: null
      f77: null
      fc: null
    flags: {}
    operating_system: ubuntu20.04
    target: x86_64
    modules: []
    environment: {}
    extra_rpaths: []
- compiler:
    spec: gcc@9.3.0
    paths:
      cc: /usr/bin/gcc
      cxx: /usr/bin/g++
      f77: /usr/bin/gfortran
      fc: /usr/bin/gfortran
    flags: {}
    operating_system: ubuntu20.04
    target: x86_64
    modules: []
    environment: {}
    extra_rpaths: []
```

## lammps-rocm 已成功

不要加载oneapi环境！！！！

ROCM4.3尝试安装


### 需要安装openmpi

下载openmpi

安装过程：
`CC=amdclang CXX=amdclang++ FC=amdflang ./configure`

`make`

`sudo make install`

### 安装lammps-rocm
`sudo apt-get install hipcub ffmpeg`

在lammps下载目录中
```{markdown}
mkdir build
cd build
export HIP_PLATFORM=amd
cmake -D PKG_GPU=on GPU_API=HIP -D HIP_ARCH=gfx803 -D CMAKE_CXX_COMPILER=hipcc ../cmake/
```
运行时候出现问题：找不到libomp.so解决办法：

`export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm-4.3.0/llvm/lib`

`sudo ldconfig`

- 第二次安装GPU

环境ROCM-4.1
spack安装的openmpi
应该是通过`spack install openmpi^clang@amd`

clang@amd的配置文件：

```
- compiler:
    spec: clang@amd
    paths:
      cc: /opt/rocm/llvm/bin/clang
      cxx: /opt/rocm/llvm/bin/clang++
      f77: /opt/rocm/llvm/bin/flang
      fc: /opt/rocm/llvm/bin/flang
    flags: {}
    operating_system: ubuntu20.04
    target: x86_64
    modules: []
    environment: {}
    extra_rpaths: []
```

具体安装lammps应该是
```
cmake -D PKG_GPU=on -D GPU_API=HIP -D HIP_PLATFORM=amd -D HIP_ARCH=gfx803 -D CMAKE_CXX_COMPILER=hipcc -D CMAKE_INSTALL_PREFIX=/home/dx/app/lammps-gpu ../cmake
make -j32
make install
```


- KOKKOS
```
mkdir build
cd build
cmake -C ../cmake/presets/basic.cmake -C ../cmake/presets/hip_amd.cmake ../cmake
```
尚未成功

**注意运行lammps时候需要 -sf gpu才能正常运行**

- 测试
`mpirun -n 4 ~/app/lammps-gpu/bin/lmp -sf gpu -var x 70 -in ~/repo/lammps-29sep2021/bench/in.lj`


var x是将系统扩大，但是x-100时候会爆显存
x=70左右时候就已经有200w个原子了，应该也够用了

### lammps-mlip

machine learning force field?

尝试使用GPU包安装但是不成功。GPU和mlip是不能一起用的

步骤：

`spack install openblas^clang@amd`

首先解压mlip2， interface， lammps
然后

```
module load openblas-*
mkdir build
cd build
cmake .. -D CMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -D CMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang -D CMAKE_Fortran_COMPILER=/opt/rocm/llvm/bin/flang -DBLAS_ROOT=/home/dx/app/spack/opt/spack/linux-ubuntu20.04-haswell/clang-amd/openblas-0.3.18-m26i3cw4d3v2h3ntqqdqesjfrq5d5pxo/lib  # 记得改路径
make -j32
cp lib_mlip_interface.a /home/dx/repo/interface-lammps-mlip-2-master # 改路径
export LAMMPS_PATH=/home/dx/repo/lammps-29Sep2021
mkdir -p $LAMMPS_PATH/lib/mlip
cp lib_mlip_interface.a $LAMMPS_PATH/lib/mlip
cp LAMMPS/Makefile.lammps.template $LAMMPS_PATH/lib/mlip/Makefile.lammps
cp -r LAMMPS/USER-MLIP/ $LAMMPS_PATH/src/
cp LAMMPS/Install.sh $LAMMPS_PATH/src/USER-MLIP/
cp LAMMPS/README $LAMMPS_PATH/src/USER-MLIP/
cd $LAMMPS_PATH/src
make no-user-mlip
make yes-user-mlip
# 之后需要修改一些makefile
```
安装GPU包
需要在/home/dx/repo/lammps-29Sep2021/lib/gpu/Makefile.hip中，在“don't change section below without need”之前添加
```
HIP_PLATFORM=amd
HIP_ARCH=gfx803
```
然后在这个文件夹里面`make -j32 -f Makefile.hip`

之后修改lammps-29Sep2021/src/MAKE/Makefile.mpi(注意路径)
```
CC =		mpicxx
CCFLAGS =	-g -O3 -std=c++11 -lgfortran -L/opt/rocm/lib -lamdhip64   -fopenmp -L/home/dx/app/spack/opt/spack/linux-ubuntu20.04-haswell/clang-amd/openblas-0.3.18-m26i3cw4d3v2h3ntqqdqesjfrq5d5pxo/lib	-lopenblas


SHFLAGS =	-fPIC
DEPFLAGS =	-M

LINK =		mpicxx
LINKFLAGS =	-g -O3 -std=c++11  -lgfortran -L/opt/rocm/lib -lamdhip64   -fopenmp -L/home/dx/app/spack/opt/spack/linux-ubuntu20.04-haswell/clang-amd/openblas-0.3.18-m26i3cw4d3v2h3ntqqdqesjfrq5d5pxo/lib	-lopenblas
LIB =
SIZE =		size
```

以及`lammps-29Sep2021/src/STUBS/Makefile`

把g++改成`/opt/rocm/llvm/bin/clang++`（不确定有没有必要但还是改了吧）

然后lammps-29Sep2021/src/中

```
make yes-gpu
make mpi-stubs
make -j32 mpi

```
最后会得到lmp-mpi

但是mlip和kokkos没法一块用

鉴定为脑瘫行为.


## vasp

似乎不能在root账户编译。

首先：安装intel oneapi

会更新

要安装base和 hpctookit不知道需不需要

`wget https://registrationcenter-download.intel.com/akdlm/irc_nas/17977/l_BaseKit_p_2021.3.0.3219_offline.sh`

`wget https://registrationcenter-download.intel.com/akdlm/irc_nas/17764/l_HPCKit_p_2021.2.0.2997_offline.sh`

sh 运行下载好的包，安装oneapi

之后要source 一下，参考intel的start guide
在.bashrc里面
`source /opt/intel/oneapi/setvars.sh`

然后编译英特尔库
**make libintel64** 如果是默认路径

`cd /opt/intel/oneapi/mkl/2021.3.0/interfaces/fftw3xf/ `
`make libintel64`

### vasp build

`OFLAG      = -O2 -xhost`
参考bilibili

`export PATH=$PATH:/root/repo/vasp.5.4.4/bin`

### vasp cuda

CUDA在makefile include里面要改
`GENCODE_ARCH    := -gencode=arch=compute_52,code=\"sm_52,compute_52\"` 

报错icc: command line error: option '-openmp' is not supported. Please use the replacement option '-qopenmp'

解决后
再报错找不到mpi.h
尝试吧makefile.include中改成
`MPI_INC    = $(I_MPI_ROOT)/intel64/include`


也可以尝试sudo apt install libopenmpi-dev，但还没试

再报错，
查看了一下，cuda root 指向CUDA_ROOT  ?= /usr/local/cuda/，这个cuda指向了\\wsl\Ubuntu-18.04\usr\local\cuda-11.0\targets\x86_64-linux\lib，然后-lcuda不能运行是因为没有libcuda.so。 这个文件被放在了stub文件夹里，还有libnvidia-ml也被放了进去，所以复制了出来

总之找不到什么文件就搜索一下然后指一下路径

### vasp bug

**segmentation fault**

`ulimit -s 262140` 

至少需要incar poscar potcar kpoints才能运行


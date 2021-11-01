---
layout: page
title: Deploy Guide
permalink: /deploy/
---

相关文件在deploy_guide repo里

* TOC
{:toc}


**转载侵删**

**declare no authorship to this page**

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

### 隔离部分cpu使其只用来运行部分任务
对于z10pa可以打开/etc/default/grub
更改：
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash isolcpus=2-17,20-35"
```
之后
sudo update-grub

重启之后可以通过资源管理器看，如果一直是0%说明成功

调度被隔离的核心：

使用taskset
例如：

taskset 2-17,20-35 mpirun -n 32 vasp

这样也可以开启numa然后只在一个numa节点上运行程序


## 系统监测：

千万不要用aida64，会导致功耗bug

使用hwinfo


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


## 苹果

### 账户无法使用

绑定银行卡之后再itunes里面激活

### 其他一些问题
m1的yml和其他yml不太通用

# Driver 安装驱动的那些事

## install graphic card driver for unsupported graphic card 安装显卡驱动 zbook17

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

## killer ax200

https://bbs.luobotou.org/thread-45955-1-1.html11

# windows system setting 系统设置

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

# SSH设置操作

## ssh 虚拟机注意事项

安装vmhs-fuge还是啥的，为了虚拟机与实体机通信

虚拟机可以尝试使用固定ip

### vmware 使用的一些常用指令
访问硬盘用的
`/usr/bin/vmhgfs-fuse .host:/ /mnt/hgfs -o subtype=vmhgfs-fuse,allow_other`


##  SSH config 文件示例

```markdown

Host 192.168.254.128
    HostName 192.168.254.128
    User root
    IdentityFile "C:\Users\（改成用户名）\.ssh\id_rsa"

```


## ssh免密码登录


(windows)首先在service服务中，打开openssh，自动启动

ssh-keygen -t rsa -f ~/.ssh/(密钥名字)
产生ssh密钥

生成的pub放到linux机器的/.ssh下面，再把内容复制到./.ssh/authorized_keys里面

```
scp ~/.ssh/(密钥名字) (用户名)@(远程主机):~/.ssh/

ssh登录远程主机之后

cat ~/.ssh/(密钥名字) >> ~/.ssh/authorized_keys
```

之后windows机器ssh-add 私钥名字,或者在。ssh的config里面写好
注意authorized keys里面每个主机只能有一个密钥

## 映射ssh的磁盘

安装直接前往 github 对应项目的 release 中下载最新版本即可，需注意 sshfs-win 对 winfsp 的最低版本依赖（下载最新版本一般即可满足），另外有GUI（用户图形操作界面）可供下载

sshfs-win：https://github.com/billziss-gh/sshfs-win/releases
winfsp：https://github.com/billziss-gh/winfsp/releases

然后映射网络磁盘里面输入

\\sshfs\用户名@服务器名字\ 

后面不用加\home啥的，过去就相当于在\home\用户名底下

如果想要上层的话也可以

\\sshfs.r\用户名@服务器名字\home\用户名\.......

sshfs相当于省略\home\用户名的过程



# linux本身设置
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
## wsl的基本设置

### 双路主机：

可以任务管理器右键vmmm选择让wsl运行在哪个cpu上面

新发现：当关闭超线程之后，wsl可以同时在两个cpu中运行

注意可能需要重新安装libintel64？

性能测试

### root 权限

 `ubuntu1804.exe config --default-user root` 

打不开的时候：netsh winsock reset

### 重启wsl

`net stop LxssManager`
`net start LxssManager`

## linux GUI
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



## basic library

### ubuntu 18.04:

`apt-get install build-essential gcc-multilib rpm lib32ncurses5 lib32z1`

### ubuntu 20.04

`apt-get install build-essential gcc-multilib rpm lib32z1`


## ubuntu18.04 root 登陆

https://blog.csdn.net/COCO56/article/details/107628019






# python 

先装好anaconda

## environment 环境相关

### 默认环境
在bashrc里添加
`conda activate environment name`

### export the environment 导出环境:

`conda env export --name research > research.yml`


### import environment from yml file 导入环境:

`conda env create -f environment.yml`

### a sample

https://github.com/lamdalamda/system-configure-record/blob/master/CARE/research.yml

## library 库
### tensorflow:
#### tensorflow windows 
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

#### test code for tensorflow tensorflow测试

```markdown
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

## 实例

### 监控网站信息变化，比如托福或者疫苗等

同时具有发送邮件提醒功能

https://www.jianshu.com/p/7c4f251485b7?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation

# Softwares 各种软件问题

## ROCm
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



## PBS/qsub 队列--目前未成功

安装PBS 队列管理；

git clone git@github.com:openpbs/openpbs.git

按照install操作
configure之前conda deactivate
./configure CC=icc 

## quantum espresso 
### quantum espresso普通编译-已经成功
只需要按照操作说明来

### quantum espresso with ROCM-未成功

安装完全新的ubuntu20.04之后，安装build essential,再按照rocm官方说明安装rocm

之后下载spack.git 

按照说明， 找到r9 fury 对应的是gfx803:

spack install sirius +rocm amdgpu_target=gfx803

openmpi报错找不到fortran和c:
```
spack install gcc 
spack load gcc 
spack compiler find

```


### spack安装--目前未成功

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


### 需要安装openmpi

下载openmpi

安装过程：
./configure

make 

sudo make install 

### 安装lammps-rocm
sudo apt-get install hipcub ffmpeg

在lammps下载目录中

mkdir build
cd build
export HIP_PLATFORM=amd
cmake -D PKG_GPU=on GPU_API=HIP -D HIP_ARCH=gfx803 -D CMAKE_CXX_COMPILER=hipcc ../cmake/

运行时候出现问题：找不到libomp.so解决办法：

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm-4.3.0/llvm/lib

sudo ldconfig




## vasp

似乎不能在root账户编译。

首先：安装intel oneapi

会更新

要安装base和 hpctookit不知道需不需要

wget https://registrationcenter-download.intel.com/akdlm/irc_nas/17977/l_BaseKit_p_2021.3.0.3219_offline.sh
wget https://registrationcenter-download.intel.com/akdlm/irc_nas/17764/l_HPCKit_p_2021.2.0.2997_offline.sh 

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

### vasp other

vasp6.1的GPU编译，新坑：https://zhuanlan.zhihu.com/p/302826820



## spack

spack find -v

可以列出已经安装的包的完整名称，之后load


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

## PBS队列管理
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
 
# 看番

https://github.com/zaxtyson/AnimeSearcher

可以git下来源代码使用

## 搜索不到东西等问题

git下来源代码，config里面更改一下端口之后，python运行app.py,之后记得在打开html之后在最底下更改app.py中的地址
 

 

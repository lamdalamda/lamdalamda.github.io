---
layout: page
title: vasp输入
permalink: /vasp_inputs/
katex: True
---


* TOC
{:toc}

总结了一些常用tag和实例



Adapted from vasp wiki


# INCAR-电子步


## ICHARG

initial charge density 初始电荷密度

### ICHARG=0

读取WAVECAR来获得初始电荷密度

### ICHARG=1

从CHGCAR里面读取

### ICHARG=2

原文：take superposition of atomic charge densities

不知道什么意思

### ICHARG=4

从POT里面读取

要求LVTOT=.TRUE.

### ICHARG=10+（0，1，2，4）

与前面各自对应，但是电子密度在整个electronic minimization过程中不变
用处：
在绘制band structure时候（比如 L-Γ-X-U）的图的时候，通过读取已有的CHGCAR，把KPOINTS设定在L-Γ-X-U，就可以画出来band structure



## NELMIN
minimum number of electronic SCF steps：每个离子步中最少的电子步数量
$$>0$$： relaxation to local energy minimum 计算最小能量的模式：




## EDIFF

电子步能量收敛的判据


## ISMEAR 
能量在费米能量周围的轨道，其电子占有概率的设置。？

https://www.vasp.at/wiki/index.php/ISMEAR

definition： determines how the partial occupancies $$f_{nk}$$ are set for each orbital
不知道对不对: 原本假设是Kohn Sham计算出来每一个态都与一个电荷相关联，但是，对于金属比如说，费米面附近的态是被**部分**填充的(fermi-dirac 公式，填充概率在$$E_{fermi}$$周围从100%下降到0%，这种情况下，ISMEAR来决定费米面附近是怎么被**部分**填充的 

### ISMEAR = N, N为正整数
计算方式为methfessel-paxton order N.
看不懂，但是这个partial occpancies可以是负数或者大于1
用于计算金属力和phonon frequency，有精确的SIGMA时候计算结果比较准确
不应用于半导体和绝缘体，错误会达到20%

### ISMEAR = 0
Gaussian smearing (不懂)
这个方法通过sigma= finite value 外推到 sigma=0 时候的能量，但是可以不给初始的sigma？
可用于绝缘体计算force和phonon frequency

对于未知体系，用ismear=0比较好


### ISMEAR=−1
 Fermi smearing.
### ISMEAR=−2
partial occupancies are read in from the WAVECAR or INCAR file, and kept fixed
需要定义FERWE，有可能需要FERDO

#### FERWE
条件:ISMEAR=−2时候必须

`FERWE=f(1)f(2)f(3)...f(NBANDS*Nk)`
定义每一个band和k点的 partial occupancy 部分占据

Nk应该是k点数量

#### FERDO
条件：ISMEAR=-2且是 spin-polarized calculation(?)

`FERDO=f(1)f(2)f(3)...f(NBANDS*Nk)`

Nk应该是k点数量

Note that the partial occupancies are also written to the OUTCAR file, but in this case they are multiplied by 2, i.e. they are between 0 and 2.

### ISMEAR=−3
: 根据一组sigma和ismear来循环计算，需要SMEARINGS参数

#### SMEARINGS

SMEARINGS =  ismear1 sigma1  ismear2 sigma2 ... 
当ISMEAR = -3 时候必须设置，对于SMEARINGS中每一个参数进行尝试 并且计算能量

要求 
IBRION = -1 即 离子不允许移动
并且设置NSW

### ISMEAR=−4

: tetrahedron method (use a Γ-centered k-mesh).
### ISMEAR=−5

: tetrahedron method with Blöchl corrections (use a Γ-centered k-mesh).
适用于semiconductor 和 insulator。
适用于bulk materials, DOS 计算结果比较好，但是计算力和stress tensor时候对于金属在计算力的时候有5%~10%偏差，可用于绝缘体计算force和phonon frequency，因为没有partial occupation， occupation只能是1和0。

### SIGMA

是ISMEAR的相关选项
似乎ISMEAR=0 时候可以不定义SIGMA

definition：width of the smearing in eV.
不知道对不对；费米能级周围的宽度
由于fermi-dirac公式，电子占据特定量子态的概率为$$\frac{1}{1+exp(\frac{E-E_f}{kT})}$$。由于vasp计算时候k点网格是有限的，电子没有办法精确的占据网格，所以通过这个sigma来允许$$[E_{fermi}\pm (SIGMA) ]eV$$范围内的 轨道/态 被部分占据。 K点网格越多 （KPOINTS）那么SIGMA可以设置的越小




# INCAR-离子步

## NSW

maxmimum number of ionic steps 最大离子步数量

IBRION =0 时候，是必须项目
IBRION !=0 时候，即，在进行relaxation时候，能进行的最多离子步数量



## EDIFFG

离子步能量收敛的判据


如果EDIFFG>0当 新的离子步 的 电子步收敛时的**能量** 与 上一个离子步 的 电子步收敛时的**能量** 之差小于收敛判据EDIFFG时离子步优化结束。如果EDIFFG<0,则为当所有力小于EDIFFG绝对值时（负的EDIFFG）离子步优化结束。


# INCAR-任务

## SYSTEM = string
系统的名称，没有锤子用，显示在outcar里面


## IBRION

https://www.vasp.at/wiki/index.php/IBRION

分子动力学或弛豫离子？  MD or relaxation to the local minimum energy

当IBRION =0 进行分子动力学molecular dynamics计算

其他情况下是relaxation to minimum energy的计算

### ISIF = 1~7
https://www.vasp.at/wiki/index.php/ISIF
重要参数，指定自由度

ISIF=3：全自由，用于晶格弛豫，寻找晶格常数

### POTIM = real

IBRION的重要参数
set the time step for MD (IBRION=0) or step width scaling (IBRION !=0)

### IBRION = 0

分子动力学计算，integrate Newton's equations of motion.
POTIM的单位是femto second

### SMASS
是IBRION=0或者3时设置
smass=-3 NVE ensemble molecular dynamic
SMASS=-2 the initial velocities are kept constant
SMASS=-1
SMASS≥0, a canonical ensemble is simulated using the algorithm of Nosé.
In this case the velocities are scaled
总能量守恒

SMASS提供阻尼因子 μ

### IRBION =-1
离子不能移动，只是计算电子的自由度，没锤子用

### NFREE

IBRIO>0时的重要设置，定义了：离子收敛过程中记住的步骤数

### IBRION =1
要求初始位置非常精确，否则需要设置Nelmin=4~8

### IBRION=2 

比较快的离子弛豫算法

### IBRION=3 

阻尼分子动力学

### IBRION =5 ,6,7,8,44

看不懂







# INCAR-输出

## LORBIT

LORBIT于RWIGS一起，决定了输出PROCAR PROOUT
具体参考https://www.vasp.at/wiki/index.php/LORBIT

# DOSCAR

需要INCAR 中 定义 LORBIT才会有这个输出

# POSCAR
## vasp5
fcc (100) surface _注释_

 3.53 _大于0：晶格常数，缩放所有的晶格向量（之后 三行）和原子坐标，如果小于0，则代表了总体积_

   .50000   .50000   .00000 _晶格向量1_

  -.50000   .50000   .00000 _晶格向量1_

   .00000   .00000  5.00000 _晶格向量1_

   B N _元素_

   1 1 _每个元素数量_

Selective Dynamics _如果是selective dynamics,则可以定义每个原子是否可以移动_

Kartesisch _笛卡尔坐标或者直接坐标_

   .00000   .00000   .00000 F F F _F是fixed，固定坐标_

   .00000   .50000   .50000 F F F

   .00000   .00000  1.00000 F F F

   .00000   .50000  1.50000 T T T

   .00000   .00000  2.00000 T T T

Cartesian _如果有初始速度的话会有接下来这些行_

 0.01 0.01 0.01 _初始速度相关的_

 0.00 0.00 0.00
 
optionally predictor-corrector coordinates 

   given on file CONTCAR of MD-run


# 实例：普通的计算（过渡金属氧化物nasicon）


## 计算内容
通过conjugate gradient算法（studynote里面有）进行对晶格尺寸的优化（ionic relaxation）[IBRION=2]。通过计算力和stress tensor来调整晶格，计算过程中晶格中离子位置 和 晶格形状 和 晶格体积 都是可变的[ISIF=3]。

## 计算过程解释
参考vasp_study_note中的DFT计算过程总结部分：


### 起始
读取POSCAR得到起始离子位置，并给出初始电荷密度猜测为：（假设没有相互作用时的）单个原子电荷密度的简单叠加[ICHARG=2]，从而得到起始的电子密度n(r)。


### 电子步
用这个电子密度代入Kohn-sham 方程$$[\frac{-\hbar^2}{2m}\nabla^2+V(r)+V_H(r)+V_{XC}(r)]\phi_i(r)=\epsilon_i\phi_i(r)$$中的hartree potential，$$V_H(r)=e^2\int \frac{n(r')}{|r-r'|}d^3r'$$，可以得到一组电子波函数，用得到的电子波函数求新的n(r)，然后递归运算。递归运算算法是常用算法[ALGO=NORMAL]（Blocked-Davidson 算法）。

计算时，费米面附近轨道的占有概率用Gaussian method计算[ISMEAR = 0]，这个设置适合于半导体绝缘体。计算方式是：设定一个初始的sigma值0.05[SIGMA = 0.05]，使得能量在$$E_{Fermi} \pm sigma$$范围内的轨道可以被电子部分占据（常用于计算金属） 。通过减少sigma重新计算来外推到 sigma=0 时候的能量。

[ENCUT = 520](eV)与计算速度有关，参考studynote中energy cutoff。block theorem给出的倒空间某点k对应的单电子波函数波函数$$\phi(x,k)=e^{ikx}\sum _K c_{k+K} e^{iKx}$$。此电子波函数所对应的能量本征值为$$E=\frac{\hbar}{2m}|k+K|^2$$，由于K是任意倒易单位矢量，所以E有无数多个，但是显然只有较低能量的是有效的（电子不会优先占用高能量）。所以设定了cutoff使得
$$E_{cutoff}=\frac{\hbar}{2m}G_{cut}^2$$
这样对于给定的cutoff（如520eV），可以得到k的新的波函数
$$\phi(x,k)=e^{ikx}\sum _{|k+K|<G_{cut}} c_{k+K} e^{iKx}$$
这样使得电子波函数不会太复杂，减少计算成本

由于过渡金属的存在（Ti），设置了自旋极化的计算[ISPIN = 2]。自旋极化是指d轨道被部分占据时，自旋方向相同的电子会产生磁矩的现象。磁矩大小 与 自旋方向相同的电子数量有关。起始的磁矩猜测是[MAGMOM = 38*0.6]。这个是用pymatgen生成的

另外，过渡金属需要LDA+U计算来引入d电子局域化的影响。U参数是向d或f层加入电子时候的额外能量参数。由[LDAU = True]打开LDA+U计算，[LDAUTYPE = 2]指定了+U计算类别是简化LSDA+U方法。设定[LDAUU]中四个数字依次对应POSCAR中的四个元素的U值（POSCAR中第二个元素是Ti，对应U=某值。POSCAR中其他元素不是过渡金属，所以U=0）。J参数是与d、f电子自旋相关的参数，但是在LDAU的基础上J也有对应的一套参数
[LDAUL = 0 0 0 0]是quantum number of on-site interaction。[LDAUPRINT = 1]是将LDA+U的一些结果写入OUTCAR输出。[LASPH = True]（平面波基矢的非球面贡献）可增加+U计算的准确性。对于[LDAUTYPE = 2]，[LMAXMIX = 4]可以加速收敛

计算时候使用的赝势是[METAGGA = Scan]，是meta-GGA的一种。[LMIXTAU = True]可以通过传递电子的动能信息帮助收敛。[LREAL = Auto]要求赝势在实空间进行投影，对投影算符进行自动优化，一般都会使用这个。

此递归运算为电子步（离子位置固定，计算电子密度从而获得当前离子位置所对应的能量），收敛条件是[EDIFF = 1e-05]。[NELMIN = 6]和[NELM = 200]要求电子步最多进行200步，最少进行6步。事实上大于40步一般就完蛋。

### 离子步
每次电子步收敛后，进行离子步（通过conjugate gradient算法[IBRION=2]）计算。从最后一个电子步中读取受力，通过受力方向来对离子来进行一个微小的移动（此移动与POTIM相关，或许不收敛的时候可以尝试修改以下POTIM？），得到新的离子位置。对新的离子位置，重复电子步的计算。如果EDIFFG>0当 新的离子步 的 电子步收敛时的**能量** 与 上一个离子步 的 电子步收敛时的**能量** 之差小于收敛判据EDIFFG时离子步优化结束。如果EDIFFG<0,则为当所有力小于|EDIFFG|时离子步优化结束。得到最终的晶体结构


离子步收敛时（离子移动的判据EDIFFG = -0.01）计算结束。cutoff是ENCUT = 520 eV。最多允许进行[NSW = 150]150步

## 输出
[LDAUPRINT = 1]是将LDA+U的一些结果写入OUTCAR输出。[LORBIT = 11]输出了DOSCAR和lm-decomposed PROCAR。[LWAVE = False]是指不将波函数写入WAVECAR

## 性能优化

[LPLANE = TRUE]是一个计算优化项目，[NCORE=12]是并行核心数量，一般等于单路核心数量。[NSIM = 4]是同时优化的band数量一般不需要改。[PREC = Accurate]会让计算结果相对准确。


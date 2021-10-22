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
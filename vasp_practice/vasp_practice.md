---
layout: page
title: vasp实例
permalink: /vasp_practice/
katex: True
---
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


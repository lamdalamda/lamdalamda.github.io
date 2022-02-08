---
layout: post
title:  "固态电池中锂金属阳极综述"
categories: "阅读文献"
katex: True
---

是需要重点看一下的一个比较全面的综述，不仅是目前研究状况，还有很多的基础知识

主要讲的是锂金属阳极（LMA）与无机固体电解质（ISE）之间界面（interface）或者中间相的形成。

第二章图1是一个非常完整的评估界面可用性的流程图，可以用做参考。

有两种情况，第一种是无机固体电解质ISE本身就不会和锂金属阳极反应，此时两者之间是形成界面interface。

第二种是无机固体电解质ISE和锂金属阳极反应生成中间相interphase，如果interphase本身的resistance低而且生长是有限制的（self limiting growth）那么也是一个可用的体系

在满足以上两种之后会有一些额外的判据。 
1. interface或者interphase的过电压是否足够低，以及

2. 在Li沉积和脱离的过程中能否保持原有的形态(形态稳定性)。形态不稳定可能来源于：在阳极负载（消耗阳极或者说，放电过程中）会形成孔隙 

第三章对于锂金属本身，和无机固体电解质的大部分物理性能都进行了一些描述


# 界面的热力学稳定性

热力学稳定性窗口

Grand Potential phase diagram （参考文献https://pubs-acs-org.libproxy1.nus.edu.sg/doi/full/10.1021/acsami.5b07517中给出了一些信息）

Li金属化学势$$\mu_{Li}(\phi)=\mu^0_{Li}-ze\phi=\mu^0_{Li}-e\phi$$

其中$$\mu^0_{Li}$$是锂金属化学势（或者说可以粗略估计为bulk Li金属的DFT能量）

那么对于固体电解质(例如，$$Li_3PS_4$$)，在电压$$\phi$$下首先发生的可能的分解反应是

$$Li_3PS_4+5Li=P+4Li_2S$$

对于分解反应，反应能量是

$$E(\phi)=[E(P)+4E(Li_2S)]-[E(Li_3PS_4)]-5[\mu_{Li}(\phi)]=[E(equilibrium\space phase)]-[E(solid\space electrolyte)]-n_{Li}\mu_{Li}(\phi)=E(equilibrium\space phase)-E(solid\space electrolyte)-n_{Li}\mu^0_{Li}+e\phi$$

因为分解产物和Li的反应是在电压继续变化之后的事情，所以实际上就是找到首先发生，或者说，找到使得$$E(equilibrium\space phase)-E(solid\space electrolyte)-n_{Li}\mu^0_{Li}$$能量最负（还是能量最正？）的反应

这个grand potential本质上也就是反应本身产生的电压

热力学稳定性窗口/电化学稳定性窗口ESW是下限，实际上哪怕热力学上不稳定，动力学上也可能是稳定的。(反应足够慢)

前面说的两种情况，如果无机固体电解质和锂金属阳极之间不会发生反应则产生interface，如果发生反应则是interphase。事实上大部分情况下都是interphase，即无机固体电解质会被Li还原。

1. nonreactive，thermodynamically stable or kinetically stablilized. No interphase formed.这种情况就是所谓的interface

2. reactive and unstable Li metal- inorganic solid electrolyte interface, where a mixed conducting interphase (MCI) forms.这个是interphase的第一种情况，这个是不好的

3. a kinetically self-limiting Li metal - inorganic solid electrolyte （ISE）interface with the formation of an almost exclusively ion conducting metabstable solid electrolyte interphase (SEI). 这个是interphase的第二种情况，这个是理想情况。

**前面有一个看起来是自相矛盾的地方，可能有的地方说要求ISE（无机固体电解质）导电性好来使得内阻尽可能低，有的地方说要求ISE导电性足够低以防止ISE不停生长自放电。实际上这里面是要离子电导率尽量大，电子电导率足够低，最后总的导电性是好的，但是导电主要是通过离子传输导电而不是电子导电。也就是说要求ISE（无机固体电解质）导电性好来使得内阻尽可能低是对的，ISE导电性足够低以防止ISE不停生长自放电是指要求电子导电性足够低**


# 基本的电极动力学

CT：charge transfer

在比较低的过电位时候过电压和反应电流呈线性，所以可以用等效的电阻（总极化电阻）来描述动力学。对于界面处的总极化电阻要求在个位数的$$\Omega cm^2$$范围内。过电压由两部分组成：

1. 传统液体电解质中也有的过电压：charge transfer overpotential, diffusion overpotential, crystallization overpotential（这是啥）

2. 和固体电解质体系中独有的：space charge layer effect, defect relaxation, current constriction(restriction polarization).这些实际上是动力学限制因素，但是也可以表现为过电压

界面动力学中涉及的传输步骤有

1. CT, charge transfer $$Li-e^-=Li^+$$
2. interface region $$Li^+->Li^+(@solute)$$
3. relaxation:Li在固体电解质中的扩散过程

## CT过程
对于液体电解质本身研究有一些问题，不是重点

对于固体电解质体系，锂金属阳极基本处于电压与电流基本呈线性关系的低过电位状态。很多研究中把通过实验测量的阻抗谱直接等于电荷转移电阻charge transfer （CT）。 由于实际上的电解质被空气污染等问题所以是不可靠的，综述表示大部分实验应该高估了此电荷转移电阻，有一个研究认为CT电阻本身小到忽略不计$$0.1\Omega cm^2$$级别。另外一个测量交换电流密度的试验结果也表示，CT电阻应该很小。所以对于这个各种传输步骤对于过电压或者说对于电阻的贡献目前基本是未知的，因为所有的试验工作都显示出了线性的过电压与电流关系。

除了这个问题，机械应变在压力大于10MPa的时候也变成一个需要考虑的因素。

## 空间电荷层（interface region）
这段描述不多，对应的是传输步骤的第二项。电荷转移动力学最多会导致转移电阻增加6倍

## relaxation

对应传输步骤第三项。
理论上ISE中锂离子通过空位来进行传输过程。这方面的电阻是取决于缺陷浓度与Li在电解质中的扩散系数。对于足够好的超离子导体来说不是太大问题，但仍是一个需要考虑的因素。

## 结晶过程/ 电镀-剥离
4.2.6大致总结了金属表面的结晶/溶解过程。

对于固体金属电极认为结晶过程是一个主要的速率控制。对于Li和ISE这里，结晶导致的过电压研究的相对比较少。结晶极化主要就是说，锂原子在电极表面进行结晶形核成长所需要的过电压。对于一些其他类别金属的记忆效应或许就是因为结晶极化：新的电极表面平整导致剥离比较困难，但是在循环之后的充电过程电极表面金属原子进行重新结晶的时候晶粒尺寸小活性位点多，这时候表现出来电池的性能会更好（ostwald ripening）

## 电流收缩

由于锂金属电极和固体电解质是固体-固体界面，所以接触是离散的，那么电流分布也是离散的。这个是电流收缩现象。这也是一个比较复杂的效应。通常是在实际的界面阻抗中占有一部分的主导地位

## 第四章总结：
一些比较常见的机理在锂/无机电解质界面的界面阻抗中被高估了。比如charge transfer过程应该是有比较低的阻抗的。


# 第五章


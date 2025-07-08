---
layout: post
title:  "镁电池的电解质,氯化镁氯化铝和四氢呋喃"
categories: "读后感"
---

这个用的是溶解在四氢呋喃中的氯化镁铝（MACC）作为电解质，是少数可以可逆地插入Mg的电解质体系。此体系中是电解的$MgCl^+ + AlCl_4^- = MgCl_2+ AlCl_3 $ 有一个主要问题就是充电过程中Al会优先于Mg在负极沉积，所以这个电解质需要优先处理

# 模型

在这个溶液体系中使用了PCM方式建模（doi10.1021/cr9904009）。这种建模方式是将离溶质近的溶剂分子（或者说，有化学键或者范德华力？）+ 溶质分子形成一个first solvation shell区域（explicit）。而其他离得远的溶剂分子，或者说在first solvation shell区域之外的，是作为implicit model，考虑的是solvent-solvent interaction。

也就是说

explicit=内圈分子=Mg和/或Al+Cl+配位的内层THF

implicit=内圈之外的整个溶剂

这种模型中得到的gibbs free energy是

$$G_{PCM}=E_{PCM}+Zpe_{expl}+q_{expl}-TS_{expl}$$

或者

$$G_{total}=E_{explicit}+Zpe_{explicit}+q_{explicit}-TS_{explicit}+E_{整个溶剂}$$



其中PCM下标是指包括所有分子（包括explicit和implicit部分），expl是仅explicit部分。Z（ero）P（oint）E（nergy）是零点能

# 方法


Gaussian09和B3LYP泛函来计算了explicit部分（solvation shell）的能量和弛豫结构。

MACC(氯化镁铝)电解质

vasp设定是使用了4x4x4的kpoint，对于固相金属镁和铝，使用了16x16x16（因为结构足够简单）。力收敛判据是EDIFFG=0.02

对于电解溶液中离子的静电相互作用，使用了Debye-Huckel修正能量

- 分子动力学

计算能量之后使用lammps来进行建模。在NPT中平衡1ns之后在NVT中进行模拟。模拟体系是48x48x48的空间，800个THF分子，和1个MgAlClTHF配合物




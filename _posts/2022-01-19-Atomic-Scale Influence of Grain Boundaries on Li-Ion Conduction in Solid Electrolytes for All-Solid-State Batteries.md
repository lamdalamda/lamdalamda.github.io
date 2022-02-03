---
layout: post
title:  "锂电池固体电解质晶界对于Li传导的的影响"
categories: "阅读文献"
katex: True
---

对于$$Li_3OCl,Li_3OBr$$的研究中，理论的锂离子活化能是0.3～0.4eV，但是实验中，块状的锂离子活化能在0.6eV左右，即理论高估了锂离子在块状固体电解质中的迁移速率。另一方面薄膜形态下的活化能是0.35eV接近理论值。这个差异解释为薄膜的晶粒尺寸要大于块状固体的晶粒尺寸，从而薄膜有比较低的境界电阻？


Lammps计算：设置体系是周期性边界条件，对于整块金属和晶界，分别进行了步长为2fs总时长为10ns的计算。supercell中有5076个离子。首先进行几ns的NPT来使得体系平衡，然后对于500～1000K的温度范围内进行NVT计算。有3.33%的Li和10%的Cl被替换成空位来模拟扩散。

扩散计算方法：

通过公示$$<r^2>=6D_{Li}t，<r^2>是mean squared displacement$$，应该是计算的diffusion coefficient。然后再代入nernst einstein relationship:

$$\frac{\sigma(conductivity)}{D_{Li}}=H_R(=1,Haven ratio)\frac{n(载流子体积浓度)q^2}{kT}$$


**这个文章还很清楚地表现了如何构造晶界模型！（figure 3）**

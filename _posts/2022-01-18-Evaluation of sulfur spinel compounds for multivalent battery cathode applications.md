---
layout: post
title:  "硫尖晶石化合物的评估"
categories: "读后感"
katex: True
---

Mg迁移的活化能在大部分氧化物中都会大于650mV的阈值，但是在硫化物中的迁移率会相对比较高，以比较低的电压为代价


Mg金属阳极沉积时候的枝晶问题更少（相比于Li来说）

动力学问题比较严重，从离子在正极中的迁移率低（活化能高）问题到从电解质到电极表面的去溶剂化问题（参考2021-01-14-Elucidating the structure of the magnesium aluminum chloride complex electrolyte for magnesium-ion batteries）

Mg等多价金属迁移率低有可能会是因为与正极的氧形成更强的化学键，另一方面主要是因为扩散路径，通过增加路径的宽度（或者说层状正极材料的层间距）可以增加迁移率。

energy above hull中，0是stable，0～85meV/atom是metastable的判据，>85eV一般认为是不稳定的

尺寸问题比较明显。Ca离子偏向于八面体配位，而比较小的Mg离子（大约是S离子的40%）对于配位没有太大的倾向性，在四面体间隙中和在八面体间隙中的能量没有太大差别

在计算中使用NEB与另外一个发表有比较大的activation energy barrier的差异，主要是因为在这个计算中晶体结构是relaxed with intercalant，或者说是带着阳离子（Ca/Mg）进行弛豫的，而另一工作是直接把不带阳离子的结构进行弛豫，这两种最后得到的晶格常数不同，这个工作中的activation energy barrier低于另一个工作，大概是因为带着阳离子的话晶体相当于被撑大了，所以更容易发生离子扩散？
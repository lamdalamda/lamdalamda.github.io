---
layout: post
title:  "Li-Fe-P-O2 Phase Diagram from First Principles Calculations"
categories: "读后感"
---


# Li-Fe-P-O2 Phase Diagram from First Principles Calculations
这篇文章讲述了建立Li Fe P O2 相图的过程

$G(T,P,N_{Li},N_{Fe},N_P,N_{O_2})=H(T,P,N_{Li},N_{Fe},N_P,N_{O_2})-TS(T,P,N_{Li},N_{Fe},N_P,N_{O_2})=E(T,P,N_{Li},N_{Fe},N_P,N_{O_2})+PV(T,P,N_{Li},N_{Fe},N_P,N_{O_2})-TS(T,P,N_{Li},N_{Fe},N_P,N_{O_2})$

归一化之后可以得到 partial molar?molal? property

$G(T,P,x_{Li},x_{Fe},x_P,X_{O_2})=E(T,P,x_{Li},x_{Fe},x_P,X_{O_2})-TS(T,P,x_{Li},x_{Fe},x_P,X_{O_2})+PV(T,P,x_{Li},x_{Fe},x_P,X_{O_2})$

那么对于两相之间的G差距

$\Delta G(T,P,x_{Li},x_{Fe},x_P,X_{O_2})=\Delta E(T,P,x_{Li},x_{Fe},x_P,X_{O_2}) - T\Delta S(T,P,x_{Li},x_{Fe},x_P,X_{O_2}) + P\Delta V(T,P,x_{Li},x_{Fe},x_P,X_{O_2})$

对比两个固相的话，体积差距是很小的，所以可以将PV项忽略。另外特殊情况当T=0K时候G=E （或者$\Delta G=\Delta E$）

作者通过DFT来计算E。使用的是GGA泛函，设定是ENCUT=500eV，kpoint只说了appropriate，收敛判据是3meV,即EDFIFF=3E-6

DFT+U参数使用了4.3，这个是二价铁和三价铁U参数的平均值。所以计算二价铁时这个U偏大，计算三价铁时这个U偏小，而对于铁的磷化物来说，由于此时铁的电子不再局域化（DFT+U的前提），所以会有比较大的误差


另外《First-Principles Prediction of Insertion Potentials in Li-Mn Oxides for Secondary Li Batteries》还计算了TS项的影响。估计$PV\approx 10^{-5}eV , TS\propto k_bT \approx 25*10^{-3}eV @ 298K$ 可见影响相对较小
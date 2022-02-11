---
layout: post
title:  "锂电池界面的建模"
categories: "阅读文献"
katex: True
---
也是一个要重点读的文章，这篇文章非常明确地介绍了整个计算过程

所以这里面的界面应该就是说interface而不是interphase，或者也可以说是interphase和其他phase的interface（什么鬼）。总之讲的是两相之间界面的建模

第一个重点公式，也挺好理解的

界面的能量interface energy$$\gamma_{ab}(\Omega)=\frac{E_{ab}(\Omega,A,n_a,n_b)-n_aE_a-n_bE_b}{A}$$

其中Eab是建模的体系中a相+b相+interface区域的总能量，Ea和Eb是bulk energy，omega这里面指代表面的原子配置。

第二个公式work of adhesion

$$W_{ab}(\Omega)=\gamma_{a,vacuum}(\Omega)+\gamma_{b,vacuum}(\Omega)-\gamma_{ab}(\Omega)$$

代入一下的话

$$W_{ab}(\Omega)=\frac{E_{a,vacuum}(\Omega,A,n_a)-n_aE_a}{A}+\frac{E_{b,vacuum}(\Omega,A,n_b)-n_bE_b}{A}-\frac{E_{ab}(\Omega,A,n_a,n_b)-n_aE_a-n_bE_b}{A}=\frac{E_{a,vacuum}(\Omega,A,n_a)+E_{b,vacuum}(\Omega,A,n_b)-E_{ab}(\Omega,A,n_a,n_b)}{A}$$

那么这两个的区别在于，interface energy是界面体系总能量$$E_{ab}(\Omega,A,n_a,n_b)$$减去**bulk**的A相和B相，而负的work of adhesion是界面体系总能量$$E_{ab}(\Omega,A,n_a,n_b)$$减去**表面**的的A相和B相

以上显然对于coherent interface是适用的，但是对于semi-coherent或者incoherent interface来说，可能会形成位错之类的，那么会有一个额外的能量$$E_{strain}$$。文章里面稍微有点绕，讲了一些小体系中Estrain与原子数量的关系，
对于小体系，从

$$\gamma_{ab}(\Omega)=\frac{E_{ab}(\Omega,A,n_a,n_b)-n_aE_a-n_bE_b}{A}$$

变成了

$$\gamma_{ab}(\Omega,n_a,n_b)=\frac{E_{ab}(\Omega,A,n_a,n_b)-n_aE_a-n_bE_b}{A}$$

也就是说现在interface energy从只和表面构型有关变成了除了与表面构型，和原子数量也相关。这主要是因为，原本因为除以了表面积，所以与原子数量无关，现在即使除了表面积，由于改变na或者nb会影响位错的数量 （比如晶格常数差距10%，那么5个a原子可能对应5个b原子，也可能会对上6个b原子），所以这时候interface energy会是na，nb的函数。这个Eab隐含了位错或者形变导致的能量


但是实际上一般研究的都是对于一个表面很大的体系，那么位错与原子数量na或者nb是成比例的，比如晶格常数相差10%，那么可以非常粗略的认为表面每10个晶格就会有一个位错引入，那么可以对公式进行改进

从

$$\gamma_{ab}(\Omega,n_a,n_b)=\frac{E_{ab}(\Omega,A,n_a,n_b)-n_aE_a-n_bE_b}{A}$$


变成

$$\gamma^{lim}_{ab}(\Omega)=\frac{E_{ab}(\Omega,A,n_a,n_b)-n_aE_a-n_bE_b-E_{strain}(\Omega,n_a,n_b)}{A}$$


计算strain energy的方法是，通过固定na的数量，调整nb的数量，计算能量的变化

$$\gamma_{ab}(\Omega,n_a,n_b)=\gamma^{lim}_{ab}(\Omega)+n_b\sigma$$

比如说1000个a原子，晶格常数差距10%，那么可能会对b从890到910个进行计算，然后得到这个strain energy

而真实能量$$\gamma_{ab}(\Omega)$$会处在这个范围

$$\gamma_{ab}^{lim}(\Omega)<\gamma_{ab}(\Omega)<\gamma_{ab}(\Omega,n_a,n_b)$$
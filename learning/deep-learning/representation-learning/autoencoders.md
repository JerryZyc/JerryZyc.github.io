---
layout: single
title: "自编码器 Autoencoders"
permalink: /learning/deep-learning/representation-learning/autoencoders/
classes: wide
---

## 一句话定义
自编码器通过重构输入来学习紧凑的潜在表示。

## 问题设定
- 输入：样本 $x \in \mathbb{R}^d$。
- 输出：潜在表示 $z$ 与重构 $\hat{x}$。
- 假设：低维表示可保留关键信息。
- 边界：可能学到恒等映射或无用特征。

## 数学表述
编码与解码：
$$
z = f_\theta(x), \quad \hat{x} = g_\phi(z)
$$
重构目标：
$$
\min_{\theta,\phi} \; \frac{1}{n} \sum_{i=1}^n \|x_i-\hat{x}_i\|_2^2
$$

## 算法解释
- 通过瓶颈约束迫使模型抽取有效特征。
- 可用于降维、去噪或预训练。

## 优化与实现细节
- 目标来源：重构误差最小化。
- 数值要点：容量过大易学到恒等映射；用稀疏/降噪/正则化限制。

## 关联与边界
- 对比 PCA：自编码器可建模非线性。
- 对比 VAE：VAE 以概率建模并引入 KL 正则。
- 边界：无监督表示可能不利于下游任务。

## 失败模式
- 过拟合导致无泛化表示。
- 潜在维度过高导致无约束。

## 最小伪代码
```text
Encode z = f(x)
Decode x_hat = g(z)
Minimize reconstruction loss
```

## 决策清单
- [ ] 需要无监督表示
- [ ] 潜在维度与任务匹配
- [ ] 有正则化或瓶颈约束

## 个人备注
TODO

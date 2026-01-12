---
layout: single
title: "变分自编码器 VAE"
permalink: /learning/deep-learning/representation-learning/vae/
classes: wide
---

## 一句话定义
VAE 通过变分推断学习可生成的潜在变量模型。

## 问题设定
- 输入：样本 $x$。
- 输出：潜在分布 $q_\phi(z\mid x)$ 与生成模型 $p_\theta(x\mid z)$。
- 假设：潜在变量可解释数据生成过程。
- 边界：解码器过强时会忽略潜变量（posterior collapse）。

## 数学表述
ELBO：
$$
\mathcal{L} = \mathbb{E}_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)] - \mathrm{KL}(q_\phi(z\mid x)\|p(z))
$$

## 算法解释
- 第一项是重构质量。
- 第二项约束潜在分布接近先验。

## 优化与实现细节
- 目标来源：变分下界最大化。
- 数值要点：重参数化技巧 $z=\mu+\sigma\odot\epsilon$。

## 关联与边界
- 对比 AE：VAE 具备概率语义与生成能力。
- 对比 GAN：VAE 更稳定但样本质量可能较低。

## 失败模式
- 后验塌缩。
- KL 权重不平衡。

## 最小伪代码
```text
Encode q(z|x), sample z
Decode x_hat = p(x|z)
Optimize ELBO
```

## 决策清单
- [ ] 需要生成式模型
- [ ] 采用 KL annealing 或 beta 调整
- [ ] 监控后验塌缩

## 个人备注
TODO

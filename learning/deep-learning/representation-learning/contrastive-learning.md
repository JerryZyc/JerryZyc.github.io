---
layout: single
title: "对比学习 Contrastive Learning"
permalink: /learning/deep-learning/representation-learning/contrastive-learning/
classes: wide
---

## 一句话定义
对比学习通过拉近正样本、推远负样本学习判别性表示。

## 问题设定
- 输入：样本对 $(x, x^+)$ 与负样本 $x^-$。
- 输出：表示向量 $z$。
- 假设：可构造语义一致的正样本。
- 边界：负样本质量决定上限。

## 数学表述
InfoNCE：
$$
\ell = -\log \frac{\exp(\mathrm{sim}(z, z^+)/\tau)}{\exp(\mathrm{sim}(z, z^+)/\tau) + \sum_{k} \exp(\mathrm{sim}(z, z_k^-)/\tau)}
$$

## 算法解释
- 表示学习依赖样本增强与对比机制。
- 温度 $\tau$ 控制分布尖锐度。

## 优化与实现细节
- 数值要点：批量大小影响负样本数量；使用动量编码器或 memory bank。

## 关联与边界
- 对比自监督：对比学习是自监督的重要范式。
- 对比度量学习：目标一致但实现不同。

## 失败模式
- 增强策略不合理导致语义破坏。
- 小 batch 负样本不足。

## 最小伪代码
```text
Generate positive pair
Encode to z, z+
Compute InfoNCE loss with negatives
```

## 决策清单
- [ ] 正样本增强合理
- [ ] 负样本数量足够
- [ ] 表示用于下游任务有效

## 个人备注
TODO

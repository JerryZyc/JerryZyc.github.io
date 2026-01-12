---
layout: single
title: "离策略 Off Policy"
permalink: /learning/reinforcement-learning/advanced-topics/off-policy/
classes: wide
---

## 一句话定义
离策略方法使用与目标策略不同的行为策略采样并进行学习。

## 问题设定
- 输入：行为策略 $\mu$、目标策略 $\pi$。
- 输出：目标策略的价值或参数。
- 假设：可从 $\mu$ 采样且能估计重要性权重。
- 边界：分布偏移大时估计高方差。

## 数学表述
重要性采样：
$$
\mathbb{E}_{\pi}[f] = \mathbb{E}_{\mu}\left[\frac{\pi(a\mid s)}{\mu(a\mid s)} f\right]
$$

## 算法解释
- 用行为策略探索，目标策略学习。
- 提升样本效率但引入偏差/方差问题。

## 优化与实现细节
- 数值要点：截断或加权重要性采样降低方差。

## 关联与边界
- 对比在策略：在策略更稳定但样本效率低。
- 边界：行为策略与目标策略差距过大易不稳定。

## 失败模式
- 权重爆炸导致梯度不稳定。
- 经验回放分布偏移。

## 最小伪代码
```text
Collect data with behavior policy
Compute importance weights
Update target policy/value
```

## 决策清单
- [ ] 行为策略与目标策略差距可控
- [ ] 重要性采样稳定
- [ ] 回放分布管理

## 个人备注
TODO

---
layout: single
title: "策略梯度 Policy Gradient"
permalink: /learning/reinforcement-learning/deep-rl/policy-gradient/
classes: wide
---

## 一句话定义
策略梯度直接优化策略参数以最大化期望回报。

## 问题设定
- 输入：可微策略 $\pi_\theta(a\mid s)$。
- 输出：策略参数 $\theta$。
- 假设：策略可采样并可微。
- 边界：梯度方差高。

## 数学表述
目标：
$$
J(\theta) = \mathbb{E}_{\pi_\theta}[G_t]
$$
梯度：
$$
\nabla_\theta J(\theta) = \mathbb{E}\big[\nabla_\theta \log \pi_\theta(a_t\mid s_t) \; G_t\big]
$$

## 算法解释
- REINFORCE 使用回报作为权重。
- 可加入 baseline 降低方差。

## 优化与实现细节
- 数值要点：优势函数替代回报。

## 关联与边界
- 与 actor-critic 紧密相关。
- 边界：样本效率低。

## 失败模式
- 高方差导致不稳定。
- 探索不足。

## 最小伪代码
```text
Collect trajectories
Compute returns
Update theta by policy gradient
```

## 决策清单
- [ ] 连续动作或随机策略需求
- [ ] 采用 baseline 降方差
- [ ] 样本预算充足

## 个人备注
TODO

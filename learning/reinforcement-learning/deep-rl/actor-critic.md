---
layout: single
title: "演员-评论家 Actor-Critic"
permalink: /learning/reinforcement-learning/deep-rl/actor-critic/
classes: wide
---

## 一句话定义
Actor-Critic 同时学习策略与价值函数，用价值作为低方差学习信号。

## 问题设定
- 输入：策略 $\pi_\theta$ 与价值函数 $V_\phi$。
- 输出：更新后的策略与价值。
- 假设：价值函数近似可用。
- 边界：价值估计偏差影响策略。

## 数学表述
优势函数：
$$
A_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)
$$
策略更新：
$$
\nabla_\theta J \approx \nabla_\theta \log \pi_\theta(a_t\mid s_t) A_t
$$

## 算法解释
- Critic 降低方差，Actor 更新策略。

## 优化与实现细节
- 数值要点：价值函数与策略同步更新易不稳定。

## 关联与边界
- 与 PPO/A2C/A3C 直接相关。
- 边界：critic 误差会污染梯度。

## 失败模式
- 价值函数崩溃导致策略退化。
- 同步更新不稳定。

## 最小伪代码
```text
Collect transitions
Compute advantage A
Update actor and critic
```

## 决策清单
- [ ] 价值函数近似足够准确
- [ ] 同步更新策略稳定
- [ ] 监控 critic loss

## 个人备注
TODO

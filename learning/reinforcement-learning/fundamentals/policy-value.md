---
layout: single
title: "策略与价值 Policy Value"
permalink: /learning/reinforcement-learning/fundamentals/policy-value/
classes: wide
---

## 一句话定义
价值函数衡量在给定策略下的期望回报，是策略改进的核心工具。

## 问题设定
- 输入：策略 $\pi$。
- 输出：$V^\pi(s)$ 或 $Q^\pi(s,a)$。
- 假设：回报可用期望表示。
- 边界：需要估计或近似。

## 数学表述
状态价值：
$$
V^\pi(s) = \mathbb{E}_\pi\left[\sum_{t=0}^\infty \gamma^t r_t \mid s_0=s\right]
$$
动作价值：
$$
Q^\pi(s,a) = \mathbb{E}_\pi\left[\sum_{t=0}^\infty \gamma^t r_t \mid s_0=s,a_0=a\right]
$$

## 算法解释
- $V$ 评估状态好坏，$Q$ 评估动作选择。

## 优化与实现细节
- 数值要点：估计价值可用蒙特卡洛或 TD。

## 关联与边界
- 与策略梯度/actor-critic 紧密相关。
- 边界：价值估计误差会影响策略改进。

## 失败模式
- 价值估计偏差导致策略退化。
- 高方差估计导致不稳定。

## 最小伪代码
```text
Estimate V or Q
Use value to improve policy
```

## 决策清单
- [ ] 价值函数形式已选定
- [ ] 估计方法稳定
- [ ] 与策略更新一致

## 个人备注
TODO

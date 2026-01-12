---
layout: single
title: "马尔可夫决策过程 MDP"
permalink: /learning/reinforcement-learning/fundamentals/mdp/
classes: wide
---

## 一句话定义
MDP 用状态转移与奖励刻画序列决策问题，是强化学习的基本建模框架。

## 问题设定
- 输入：状态 $S$、动作 $A$、转移 $P(s'\mid s,a)$、奖励 $R(s,a)$。
- 输出：策略 $\pi(a\mid s)$。
- 假设：马尔可夫性成立。
- 边界：部分可观测需 POMDP。

## 数学表述
目标：
$$
\max_{\pi} \; \mathbb{E}_\pi\left[\sum_{t=0}^{\infty} \gamma^t r_t\right]
$$

## 算法解释
- 状态满足马尔可夫性：未来仅依赖当前状态与动作。

## 优化与实现细节
- 目标来源：期望回报最大化。
- 数值要点：折扣因子 $\gamma$ 控制长期回报权重。

## 关联与边界
- 对比 POMDP：MDP 假设全可观测。
- 边界：状态建模不完整会降低可解性。

## 失败模式
- 状态定义不充分导致策略失效。
- 奖励稀疏导致学习困难。

## 最小伪代码
```text
Define S, A, P, R, gamma
Optimize policy to maximize expected return
```

## 决策清单
- [ ] 状态定义满足马尔可夫性
- [ ] 奖励设计可学习
- [ ] 折扣因子合理

## 个人备注
TODO

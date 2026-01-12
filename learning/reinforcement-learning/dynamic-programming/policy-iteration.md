---
layout: single
title: "策略迭代 Policy Iteration"
permalink: /learning/reinforcement-learning/dynamic-programming/policy-iteration/
classes: wide
---

## 一句话定义
策略迭代交替执行策略评估与策略改进以收敛到最优策略。

## 问题设定
- 输入：MDP、初始策略 $\pi_0$。
- 输出：最优策略 $\pi^*$。
- 假设：模型已知。
- 边界：大规模 MDP 计算昂贵。

## 数学表述
策略改进：
$$
\pi_{k+1}(s) = \arg\max_a \sum_{s'} P(s'\mid s,a)\big(R(s,a,s') + \gamma V^{\pi_k}(s')\big)
$$

## 算法解释
- 评估得到价值函数，改进得到更优策略。

## 优化与实现细节
- 数值要点：可用截断评估近似替代精确评估。

## 关联与边界
- 对比价值迭代：策略迭代收敛更快但每轮成本更高。

## 失败模式
- 状态空间大导致评估不可扩展。

## 最小伪代码
```text
Initialize policy pi
Repeat:
  Evaluate V^pi
  Improve pi by greedy w.r.t V^pi
Until policy stable
```

## 决策清单
- [ ] 模型已知
- [ ] 评估成本可接受
- [ ] 需要稳定最优策略

## 个人备注
TODO

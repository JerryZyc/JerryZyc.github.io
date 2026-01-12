---
layout: single
title: "策略评估 Policy Evaluation"
permalink: /learning/reinforcement-learning/dynamic-programming/policy-evaluation/
classes: wide
---

## 一句话定义
策略评估通过贝尔曼期望方程计算给定策略的价值函数。

## 问题设定
- 输入：策略 $\pi$，MDP $(S,A,P,R,\gamma)$。
- 输出：$V^\pi$ 或 $Q^\pi$。
- 假设：模型已知。
- 边界：仅适用于可获得转移模型的场景。

## 数学表述
贝尔曼期望方程：
$$
V^\pi(s) = \sum_{a} \pi(a\mid s) \sum_{s'} P(s'\mid s,a)\big(R(s,a,s') + \gamma V^\pi(s')\big)
$$

## 算法解释
- 通过迭代收敛到 $V^\pi$。

## 优化与实现细节
- 目标来源：线性方程组求解。
- 数值要点：同步/异步迭代；终止条件基于 $\|V_{k+1}-V_k\|$。

## 关联与边界
- 与策略迭代结合形成完整 DP。
- 边界：状态空间大时不可扩展。

## 失败模式
- 模型误差导致评估偏差。
- 迭代收敛慢。

## 最小伪代码
```text
Initialize V
Repeat:
  V(s) = sum_a pi(a|s) sum_{s'} P(s'|s,a)[R + gamma V(s')]
Until convergence
```

## 决策清单
- [ ] 转移模型可用
- [ ] 状态空间可遍历
- [ ] 收敛阈值合理

## 个人备注
TODO

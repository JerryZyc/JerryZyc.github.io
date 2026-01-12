---
layout: single
title: "价值迭代 Value Iteration"
permalink: /learning/reinforcement-learning/dynamic-programming/value-iteration/
classes: wide
---

## 一句话定义
价值迭代直接迭代贝尔曼最优算子以收敛到最优价值函数。

## 问题设定
- 输入：MDP。
- 输出：$V^*$ 与最优策略 $\pi^*$。
- 假设：模型已知。
- 边界：状态空间大时不可扩展。

## 数学表述
贝尔曼最优方程：
$$
V^*(s) = \max_a \sum_{s'} P(s'\mid s,a)\big(R(s,a,s') + \gamma V^*(s')\big)
$$

## 算法解释
- 通过最优算子迭代逼近 $V^*$。

## 优化与实现细节
- 数值要点：终止条件基于 Bellman 残差。

## 关联与边界
- 对比策略迭代：每步更便宜但迭代次数更多。

## 失败模式
- 收敛慢。
- 大规模状态不可处理。

## 最小伪代码
```text
Initialize V
Repeat:
  V(s) = max_a sum_{s'} P(s'|s,a)[R + gamma V(s')]
Derive greedy policy
```

## 决策清单
- [ ] 模型已知
- [ ] 需要最优价值函数
- [ ] 状态空间规模可控

## 个人备注
TODO

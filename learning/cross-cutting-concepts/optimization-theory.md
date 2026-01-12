---
layout: single
title: "优化理论 Optimization Theory"
permalink: /learning/cross-cutting-concepts/optimization-theory/
classes: wide
---

## 一句话定义
优化理论研究目标函数在约束下的最优解存在性与求解方法。

## 问题设定
- 输入：目标函数 $f(x)$ 与约束集 $\mathcal{C}$。
- 输出：最优解 $x^*$ 或最优值 $f^*$。
- 假设：问题可表述为可微或凸优化。
- 边界：非凸问题通常无全局保证。

## 数学表述
一般形式：
$$
\min_{x \in \mathcal{C}} f(x)
$$
KKT 条件（带约束）：
$$
\nabla f(x^*) + \sum_i \lambda_i \nabla g_i(x^*) + \sum_j \nu_j \nabla h_j(x^*) = 0
$$

## 算法解释
- 梯度法用于无约束或简单约束。
- 拉格朗日方法处理约束。

## 优化与实现细节
- 数值要点：条件数决定收敛速度；二阶法成本高。

## 关联与边界
- 与机器学习的 ERM/MLE/MAP 直接对应。
- 边界：非凸问题需启发式或近似算法。

## 失败模式
- 局部最优或鞍点。
- 约束处理不当导致不可行解。

## 最小伪代码
```text
Define f and constraints
Choose solver
Iterate until convergence
```

## 决策清单
- [ ] 问题是否凸
- [ ] 约束是否可处理
- [ ] 收敛与计算成本可接受

## 个人备注
TODO

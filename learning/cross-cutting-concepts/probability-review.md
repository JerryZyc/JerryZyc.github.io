---
layout: single
title: "概率回顾 Probability Review"
permalink: /learning/cross-cutting-concepts/probability-review/
classes: wide
---

## 一句话定义
概率论为不确定性建模与统计推断提供统一语言。

## 问题设定
- 输入：随机变量与分布假设。
- 输出：概率、期望与条件分布。
- 假设：分布可定义并可估计。
- 边界：不满足独立性或分布假设时推断偏差。

## 数学表述
条件概率：
$$
P(A\mid B)=\frac{P(A,B)}{P(B)}
$$
期望：
$$
\mathbb{E}[X]=\int x p(x) dx
$$

## 算法解释
- 用于定义损失、似然与不确定性估计。

## 优化与实现细节
- 数值要点：概率归一化与数值稳定。

## 关联与边界
- 与统计学习、贝叶斯推断核心相关。
- 边界：高维分布估计困难。

## 失败模式
- 依赖假设不成立导致误判。
- 采样不足导致估计偏差。

## 最小伪代码
```text
Define distribution
Compute expectation or probability
```

## 决策清单
- [ ] 分布假设合理
- [ ] 样本量足够
- [ ] 数值计算稳定

## 个人备注
TODO

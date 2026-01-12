---
layout: single
title: "感知机 Perceptron"
permalink: /learning/deep-learning/foundations/perceptron/
classes: wide
---

## 一句话定义
感知机是线性分类器，通过误分类驱动的更新规则学习可分超平面。

## 问题设定
- 输入：样本 $x_i \in \mathbb{R}^d$，标签 $y_i \in \{-1,+1\}$。
- 输出：参数 $w, b$。
- 假设：数据线性可分（收敛保证）。
- 边界：不可分时无收敛保证。

## 数学表述
判别函数：
$$
\hat{y} = \text{sign}(w^\top x + b)
$$
误分类时更新：
$$
w \leftarrow w + \eta y_i x_i, \quad b \leftarrow b + \eta y_i
$$

## 算法解释
- 只在误分类样本上更新。
- 相当于寻找满足间隔条件的线性分隔面。

## 优化与实现细节
- 目标来源：间隔最大化的启发式。
- 求解器：在线/批量更新。
- 数值要点：特征缩放影响收敛速度。

## 关联与边界
- 对比 SVM：感知机不最大化间隔，SVM 是凸优化。
- 对比逻辑回归：逻辑回归优化对数似然并输出概率。
- 边界：线性不可分需核技巧或非线性模型。

## 失败模式
- 数据不可分导致震荡。
- 噪声标签引起不稳定更新。

## 最小伪代码
```text
Input: X, y
Initialize w, b
Repeat:
  for each (x_i, y_i):
    if y_i (w^T x_i + b) <= 0:
      w = w + eta y_i x_i
      b = b + eta y_i
Return w, b
```

## 决策清单
- [ ] 线性可分性可接受
- [ ] 对噪声敏感性可容忍
- [ ] 与 SVM/逻辑回归对比过

## 个人备注
TODO

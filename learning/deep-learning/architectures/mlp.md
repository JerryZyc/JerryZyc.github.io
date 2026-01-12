---
layout: single
title: "多层感知机 MLP"
permalink: /learning/deep-learning/architectures/mlp/
classes: wide
---

## 一句话定义
MLP 通过多层线性变换与非线性激活组合学习通用函数近似。

## 问题设定
- 输入：$x \in \mathbb{R}^d$。
- 输出：$\hat{y}$ 或表示向量。
- 假设：可通过多层非线性逼近目标函数。
- 边界：缺少显式结构先验，样本效率较低。

## 数学表述
前向：
$$
 h^{(0)} = x, \quad h^{(l)} = \phi(W^{(l)} h^{(l-1)} + b^{(l)})
$$
输出层按任务选择线性或 softmax。

## 算法解释
- 通过层级表示逐步抽取特征。
- 宽度/深度决定表达能力与优化难度。

## 优化与实现细节
- 目标来源：ERM/MLE。
- 数值要点：初始化与归一化对收敛关键。

## 关联与边界
- 对比 CNN：CNN 引入局部与共享参数先验。
- 对比 Transformer：Transformer 具备注意力机制与序列建模能力。
- 边界：高维结构化输入需特定架构。

## 失败模式
- 过拟合或欠拟合。
- 梯度消失/爆炸。

## 最小伪代码
```text
Input: x
For l in 1..L:
  h = phi(W_l h + b_l)
Return output
```

## 决策清单
- [ ] 数据无明显结构先验
- [ ] 模型容量与数据规模匹配
- [ ] 初始化与归一化合理

## 个人备注
TODO

---
layout: single
title: "特征工程 Feature Engineering"
permalink: /learning/machine-learning/ml-in-practice/feature-engineering/
classes: wide
---

## 一句话定义
特征工程是将原始数据转化为可被模型高效利用的表示，从而提升可分性与稳定性。

## 问题设定
- 输入：原始数据 $x$（结构化/非结构化）。
- 输出：特征向量 $\phi(x)$。
- 假设：模型对输入分布与尺度敏感。
- 边界：深度模型可弱化但无法完全替代特征工程。

## 数学表述
特征映射：
$$
\phi: x \mapsto \mathbb{R}^d
$$
目标仍为 ERM：
$$
\min_{\theta} \; \frac{1}{n} \sum_{i=1}^n \ell(f_\theta(\phi(x_i)), y_i)
$$

## 算法解释
- 通过变换使线性/简单模型具备更强表达能力。
- 降噪、归一化、分箱、交互项可显著改善性能。

## 优化与实现细节
- 目标来源：改善可分性与稳定性。
- 常用：归一化、标准化、One-hot、频率编码、目标编码。
- 数值要点：避免在测试集上拟合变换（泄漏）。

## 关联与边界
- 与模型选择强相关：线性模型更依赖特征工程。
- 与数据泄漏强相关：不当编码会泄漏标签信息。
- 边界：高维特征可能导致过拟合。

## 失败模式
- 训练/测试统计不一致。
- 目标编码导致泄漏。
- 过度手工特征导致噪声放大。

## 最小伪代码
```text
Input: raw data X
Fit transforms on train only
Transform train/test to features
Train model on features
```

## 决策清单
- [ ] 变换只在训练集拟合
- [ ] 特征尺度已统一
- [ ] 与模型复杂度匹配

## 个人备注
TODO

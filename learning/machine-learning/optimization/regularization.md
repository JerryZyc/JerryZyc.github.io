---
layout: single
title: "正则化 Regularization"
permalink: /learning/machine-learning/optimization/regularization/
classes: wide
---

## 一句话定义
正则化通过加入惩罚项或约束控制模型复杂度，提高泛化能力与数值稳定性。

## 问题设定
- 输入：基础目标 $\mathcal{L}(\theta)$。
- 输出：正则化后的目标或约束形式。
- 假设：模型存在过拟合风险或病态问题。
- 边界：过强正则会导致欠拟合。

## 数学表述
一般形式：
$$
\min_{\theta} \; \mathcal{L}(\theta) + \lambda \Omega(\theta)
$$
常见：$\ell_2$（ridge）与 $\ell_1$（lasso）。

## 算法解释
- $\ell_2$ 收缩参数，改善条件数。
- $\ell_1$ 产生稀疏解，执行特征选择。

## 优化与实现细节
- 目标来源：MAP（先验对应正则）。
- 选择：交叉验证调 $\lambda$。
- 数值要点：正则与特征缩放耦合。

## 关联与边界
- 对比早停：早停可视作隐式正则。
- 对比数据增强：通过扩展数据降低方差。
- 边界：正则不能修复数据偏差或标签错误。

## 失败模式
- 正则过强导致偏差增大。
- 不同特征尺度导致惩罚不均衡。

## 最小伪代码
```text
Input: loss L(theta), penalty Omega
Choose lambda
Optimize L + lambda * Omega
```

## 决策清单
- [ ] 是否存在过拟合或病态
- [ ] 选择合适正则形式
- [ ] 正则强度有验证支持

## 个人备注
TODO

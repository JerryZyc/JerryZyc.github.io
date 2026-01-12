---
layout: single
title: "正则化 Regularization"
permalink: /learning/deep-learning/training/regularization/
classes: wide
---

## 一句话定义
正则化通过限制模型复杂度减少过拟合并提升泛化。

## 问题设定
- 输入：模型与损失函数。
- 输出：加入正则项的训练目标。
- 假设：过拟合风险存在。
- 边界：正则过强导致欠拟合。

## 数学表述
$$
\min_{\theta} \; \mathcal{L}(\theta) + \lambda \Omega(\theta)
$$
常见：$\ell_2$ 权重衰减、dropout。

## 算法解释
- 权重衰减限制参数规模。
- Dropout 相当于模型集成近似。

## 优化与实现细节
- 数值要点：AdamW 将权重衰减与梯度分离。

## 关联与边界
- 与数据增强、早停互补。
- 边界：不能修复数据分布问题。

## 失败模式
- 正则过强导致性能下降。
- Dropout 在推理时需关闭或缩放。

## 最小伪代码
```text
Add regularization term
Optimize total loss
```

## 决策清单
- [ ] 过拟合风险评估
- [ ] 正则强度有验证支持
- [ ] 与优化器兼容

## 个人备注
TODO

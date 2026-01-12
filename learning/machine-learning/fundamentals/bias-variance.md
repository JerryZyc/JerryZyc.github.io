---
layout: single
title: "偏差-方差 Bias Variance"
permalink: /learning/machine-learning/fundamentals/bias-variance/
classes: wide
---

## 一句话定义
偏差-方差分解描述模型误差由系统性偏差与随机性方差共同构成。

## 问题设定
- 输入：训练集与测试集。
- 输出：泛化误差分解。
- 假设：误差平方可分解，通常在回归与平方损失下成立。
- 边界：不适用于所有损失或任务。

## 数学表述
对回归问题，期望误差分解：
$$
\mathbb{E}[(y-\hat{f}(x))^2] = \text{Bias}^2 + \text{Variance} + \sigma^2
$$
其中 $\sigma^2$ 为不可约噪声。

## 算法解释
- 高偏差：模型过于简单，欠拟合。
- 高方差：模型过复杂，过拟合。

## 优化与实现细节
- 目标来源：平方误差分解。
- 手段：正则化降低方差；提升模型容量降低偏差。
- 数值要点：需要交叉验证评估平衡点。

## 关联与边界
- 与泛化误差、正则化、模型选择直接相关。
- 边界：分类任务常用替代分析。

## 失败模式
- 数据量不足导致方差过高。
- 模型过简导致偏差过高。

## 最小伪代码
```text
Input: models with different capacity
Train each model
Compare train vs validation error
Select bias-variance tradeoff point
```

## 决策清单
- [ ] 训练误差与验证误差差距评估
- [ ] 正则化强度已调节
- [ ] 数据量是否足够

## 个人备注
TODO

---
layout: single
title: "过拟合 Overfitting"
permalink: /learning/deep-learning/dl-in-practice/overfitting/
classes: wide
---

## 一句话定义
过拟合是模型在训练集拟合过度，导致泛化性能下降。

## 问题设定
- 输入：训练/验证误差曲线。
- 输出：过拟合诊断与缓解策略。
- 假设：模型容量过大或数据不足。
- 边界：过拟合不等于训练误差低。

## 数学表述
泛化间隙：
$$
\Delta = R_{val}(f) - R_{train}(f)
$$

## 算法解释
- 过拟合表现为训练误差下降、验证误差上升。

## 优化与实现细节
- 方法：正则化、数据增强、早停、减小模型。

## 关联与边界
- 与偏差-方差、正则化强相关。
- 边界：分布漂移与过拟合需区分。

## 失败模式
- 调参过度导致验证集过拟合。
- 数据泄漏导致错误判断。

## 最小伪代码
```text
Monitor train/val curves
Apply regularization or early stop
```

## 决策清单
- [ ] 过拟合检测依据明确
- [ ] 正则化已启用
- [ ] 数据增强有效

## 个人备注
TODO

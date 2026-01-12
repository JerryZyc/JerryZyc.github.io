---
layout: single
title: "损失函数 Loss Functions"
permalink: /learning/deep-learning/foundations/loss-functions/
classes: wide
---

## 一句话定义
损失函数将预测与目标的差异量化为可优化的标量。

## 问题设定
- 输入：预测 $\hat{y}$、目标 $y$。
- 输出：标量损失 $\ell(\hat{y}, y)$。
- 假设：损失与任务目标一致。
- 边界：不匹配导致错误优化方向。

## 数学表述
回归：
$$
\ell_{\text{MSE}} = \frac{1}{2}(y-\hat{y})^2
$$
分类（交叉熵）：
$$
\ell_{\text{CE}} = -\sum_{c} y_c \log \hat{p}_c
$$

## 算法解释
- 损失决定梯度方向与训练动态。
- 不同损失体现不同风险偏好。

## 优化与实现细节
- 目标来源：似然（交叉熵）或误差度量（MSE）。
- 数值要点：避免 log(0)；用稳定 softmax。

## 关联与边界
- 与评估指标相关但不等同。
- 边界：损失与业务指标错配时需重新设计。

## 失败模式
- 类别不平衡时交叉熵偏向多数类。
- 离群点主导 MSE。

## 最小伪代码
```text
Input: y_hat, y
Compute loss
Return loss
```

## 决策清单
- [ ] 损失与任务一致
- [ ] 数值实现稳定
- [ ] 与评估指标对齐

## 个人备注
TODO

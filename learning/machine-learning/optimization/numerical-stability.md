---
layout: single
title: "数值稳定性 Numerical Stability"
permalink: /learning/machine-learning/optimization/numerical-stability/
classes: wide
---

## 一句话定义
数值稳定性关注算法在有限精度计算下误差是否被放大，以及如何避免灾难性失真。

## 问题设定
- 输入：数值算法与实现细节。
- 输出：稳定计算策略。
- 假设：浮点运算存在舍入误差。
- 边界：稳定性不等于统计鲁棒性。

## 数学表述
条件数衡量输入扰动对输出影响：
$$
\kappa(A) = \|A\|\,\|A^{-1}\|
$$
当 $\kappa$ 大时，问题病态。

## 算法解释
- 数值稳定性通过重写公式、归一化、改用分解（QR/SVD）实现。

## 优化与实现细节
- 避免显式求逆；优先分解求解。
- 使用 log-sum-exp 稳定 softmax。
- 归一化输入特征。

## 关联与边界
- 与正则化、条件数、矩阵分解紧密相关。
- 边界：稳定性问题可在正确模型下仍发生。

## 失败模式
- 小差值相减导致灾难性消去。
- 溢出/下溢导致 NaN。
- 条件数过大导致系数不可靠。

## 最小伪代码
```text
Input: computation
Rewrite to stable form
Use decomposition instead of inverse
Add epsilon if needed
```

## 决策清单
- [ ] 检查条件数或尺度
- [ ] 使用稳定计算技巧
- [ ] 监控 NaN/Inf

## 个人备注
TODO

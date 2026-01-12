---
layout: single
title: "归一化 Normalization"
permalink: /learning/deep-learning/training/normalization/
classes: wide
---

## 一句话定义
归一化通过标准化特征或激活分布来加速训练并稳定梯度。

## 问题设定
- 输入：激活或特征张量。
- 输出：归一化后的张量。
- 假设：分布偏移会降低训练稳定性。
- 边界：小 batch 或序列任务需特殊归一化。

## 数学表述
BatchNorm：
$$
\hat{x} = \frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}},\quad y = \gamma \hat{x} + \beta
$$
LayerNorm 在特征维度归一化。

## 算法解释
- 降低内部协变量偏移。
- 提供可学习缩放与偏移。

## 优化与实现细节
- 目标来源：稳定分布与梯度。
- 数值要点：训练/推理使用不同统计量；小 batch 适合 LayerNorm/GroupNorm。

## 关联与边界
- 与初始化互补。
- 边界：BN 在 RNN 中不稳定，常用 LN。

## 失败模式
- 小 batch 统计不稳定。
- 训练/推理统计不一致导致性能下降。

## 最小伪代码
```text
Input: activations x
Compute mean/var
Normalize and scale
```

## 决策清单
- [ ] 选择合适归一化类型
- [ ] 训练/推理统计一致
- [ ] 兼容 batch size

## 个人备注
TODO

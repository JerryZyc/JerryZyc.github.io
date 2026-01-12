---
layout: single
title: "门控循环单元 LSTM / GRU"
permalink: /learning/deep-learning/architectures/lstm-gru/
classes: wide
---

## 一句话定义
LSTM/GRU 通过门控机制缓解 RNN 长程依赖中的梯度消失。

## 问题设定
- 输入：序列 $\{x_t\}$。
- 输出：序列输出或最终状态。
- 假设：序列存在长期依赖。
- 边界：计算开销高于 RNN。

## 数学表述
LSTM 关键更新：
$$
 i_t = \sigma(W_i x_t + U_i h_{t-1})
$$
$$
 f_t = \sigma(W_f x_t + U_f h_{t-1})
$$
$$
 c_t = f_t \odot c_{t-1} + i_t \odot \tanh(W_c x_t + U_c h_{t-1})
$$
GRU 通过更新门/重置门简化。

## 算法解释
- 门控控制信息流动与记忆保留。
- 适合中长序列。

## 优化与实现细节
- 数值要点：梯度裁剪与正则化。
- 计算代价比 RNN 高。

## 关联与边界
- 对比 RNN：更稳但更复杂。
- 对比 Transformer：并行与长程依赖能力弱。

## 失败模式
- 长序列仍可能遗忘。
- 训练时间长。

## 最小伪代码
```text
Input: x_t, h_{t-1}, c_{t-1}
Compute gates i, f, o
Update c_t, h_t
```

## 决策清单
- [ ] 需要显式记忆门控
- [ ] 序列长度与计算预算匹配

## 个人备注
TODO


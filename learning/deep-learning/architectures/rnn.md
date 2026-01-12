---
layout: single
title: "循环神经网络 RNN"
permalink: /learning/deep-learning/architectures/rnn/
classes: wide
---

## 一句话定义
RNN 通过递归状态更新建模序列依赖。

## 问题设定
- 输入：序列 $\{x_t\}$。
- 输出：序列输出或最终状态。
- 假设：短期依赖可通过递归状态捕获。
- 边界：长依赖易梯度消失。

## 数学表述
$$
 h_t = \phi(W_x x_t + W_h h_{t-1} + b)
$$

## 算法解释
- 隐状态作为压缩记忆。
- 序列长度增加导致梯度不稳定。

## 优化与实现细节
- 目标来源：序列 ERM。
- 数值要点：梯度裁剪；使用门控结构改进记忆。

## 关联与边界
- 对比 LSTM/GRU：门控改善长程依赖。
- 对比 Transformer：Transformer 并行计算更强。
- 边界：长序列效果受限。

## 失败模式
- 梯度消失/爆炸。
- 训练时间长。

## 最小伪代码
```text
Input: sequence x_1..T
h = 0
For t=1..T:
  h = phi(Wx x_t + Wh h)
Return h or outputs
```

## 决策清单
- [ ] 序列长度适中
- [ ] 需要递归状态建模
- [ ] 与 Transformer baseline 对比

## 个人备注
TODO

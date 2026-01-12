---
layout: single
title: "变换器 Transformer"
permalink: /learning/deep-learning/architectures/transformer/
classes: wide
---

## 一句话定义
Transformer 通过自注意力机制建模序列依赖，支持并行计算与全局交互。

## 问题设定
- 输入：序列 $\{x_t\}$ 与位置编码。
- 输出：序列表示或预测。
- 假设：全局依赖重要。
- 边界：注意力复杂度为 $O(T^2)$。

## 数学表述
自注意力：
$$
\text{Attn}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d}}\right)V
$$

## 算法解释
- 通过注意力直接建模任意位置关系。
- 多头注意力增强表达能力。

## 优化与实现细节
- 数值要点：使用 LayerNorm、残差、学习率 warmup。
- 复杂度：$O(T^2)$ 时间与内存。

## 关联与边界
- 对比 RNN：更强并行与长程依赖。
- 对比 CNN：全局建模但成本更高。

## 失败模式
- 长序列计算成本高。
- 小数据下易过拟合。

## 最小伪代码
```text
Input: X
Compute Q,K,V
Apply attention
Stack layers
Return outputs
```

## 决策清单
- [ ] 序列长度可接受 O(T^2)
- [ ] 需要全局依赖建模
- [ ] 数据量足够

## 个人备注
TODO


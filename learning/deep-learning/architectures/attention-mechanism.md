---
layout: single
title: "注意力机制 Attention Mechanism"
permalink: /learning/deep-learning/architectures/attention-mechanism/
classes: wide
---

## 一句话定义
注意力通过可学习权重在输入元素间分配关注，实现动态信息聚合。

## 问题设定
- 输入：查询 $Q$、键 $K$、值 $V$。
- 输出：加权表示。
- 假设：相关性可通过相似度度量。
- 边界：注意力计算成本高。

## 数学表述
$$
\text{Attn}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d}}\right)V
$$

## 算法解释
- 查询决定关注位置。
- 软选择替代硬对齐。

## 优化与实现细节
- 数值要点：缩放避免内积过大；mask 控制依赖。

## 关联与边界
- 与 Transformer 关系：注意力是其核心算子。
- 与 RNN 对齐：注意力缓解长序列信息瓶颈。

## 失败模式
- 注意力稀释导致信息丢失。
- 过大序列导致内存爆炸。

## 最小伪代码
```text
Input: Q,K,V
Compute scores = QK^T / sqrt(d)
Apply softmax and multiply V
```

## 决策清单
- [ ] 需要动态信息聚合
- [ ] 序列长度可承受

## 个人备注
TODO

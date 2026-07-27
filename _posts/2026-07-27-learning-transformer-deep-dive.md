---
title: "Transformer 架构精讲：从注意力机制到核心设计哲学"
date: 2026-07-27
categories: [learning]
tags: [transformer, attention, deep-learning, architecture, nlp]
---

## 为什么需要 Transformer？

在 Transformer 出现之前，序列建模由 RNN/LSTM 主导。它们的核心问题是**串行**：$t$ 时刻的隐状态 $h_t$ 依赖 $h_{t-1}$，无法并行计算，长序列梯度易消失/爆炸。

2017 年 "Attention Is All You Need" 提出 Transformer，首次完全放弃循环结构，仅用**注意力机制**建模序列，同时解决：

| 问题 | RNN/LSTM | Transformer |
|------|----------|-------------|
| 并行计算 | ❌ 串行 | ✅ 完全并行 |
| 长程依赖 | ❌ 随距离衰减 | ✅ 直接连接 |
| 训练效率 | ❌ 慢 | ✅ GPU 友好 |
| 扩展性 | ❌ 有限 | ✅ 可堆叠深度 |

---

## 整体架构

Transformer 是 Encoder-Decoder 结构：

```
输入序列 → [Encoder × N] → 表示 → [Decoder × N] → 输出序列
```

每一层（Encoder/Decoder Block）的核心组件：

1. **自注意力（Self-Attention）** — 建模序列内部关系
2. **前馈网络（FFN）** — 逐位置的非线性变换
3. **残差连接 + 层归一化** — 稳定训练

> 现在的主流用法（BERT、GPT）只用 Encoder 或 Decoder 部分，而非完整的 Encoder-Decoder。

---

## 核心组件 1：缩放点积注意力

### 直觉

给一个查询 $q$，在一组键值对 $(k_i, v_i)$ 中找到最相关的内容：

```
q = "天空是什么颜色的"
k1 = "猫是哺乳动物"      →  相关性低
k2 = "天空是蓝色的"      →  相关性高  →  取出 v2
k3 = "1+1=2"             →  相关性低
```

### 数学形式

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

逐行理解：

| 步骤 | 操作 | 含义 |
|------|------|------|
| $QK^\top$ | 内积矩阵 | 每个 query 与所有 key 的相似度 |
| $\div \sqrt{d_k}$ | 缩放 | 防止大维度下内积爆炸，梯度变平 |
| $\text{softmax}$ | 行归一化 | 每个 query 的权重和为 1 |
| $\times V$ | 加权求和 | 按权重聚合信息 |

### 为什么缩放 $\sqrt{d_k}$？

当 $d_k$ 很大时，内积 $q \cdot k$ 的方差 $\approx d_k$。如果不缩放，softmax 输入会落在梯度极小的饱和区。缩放后方差回 1，梯度正常。

---

## 核心组件 2：多头注意力

不只有一个注意力函数，而是 **$h$ 个头并行计算**：

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h) W^O
$$

$$
\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)
$$

每个头学到不同的投影空间，捕获不同类型的依赖：

- 头 1：语法依赖（主谓宾）
- 头 2：语义相似（同义词）
- 头 3：长程依赖（句尾回指句首）

> 实践中 $h=8$ 或 $h=12$，每个头的维度 $d_k = d_{\text{model}} / h$，总计算量与单头相近。

---

## 核心组件 3：位置编码

注意力是**排列等变的**（permutation equivariant）：

$$
\text{Attention}(Q, K, V) \text{ 对输入顺序不敏感}
$$

不加位置信息，"我打你" 和 "你打我" 结果相同。所以必须注入位置信号。

### 原始 Transformer 的做法：正弦编码

$$
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$
$$
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

**设计意图**：
- 不同维度有不同的波长（$2\pi$ 到 $10000 \cdot 2\pi$）
- 低维度编码局部位置（变化快），高维度编码全局位置（变化慢）
- 对任意 $k$，$PE_{pos+k}$ 可表示为 $PE_{pos}$ 的线性函数 → 模型可学到相对位置关系

### 现在的主流做法：可学习位置编码 / RoPE

- **BERT**：可学习位置嵌入（每个位置一个向量）
- **GPT / LLaMA**：**RoPE（旋转位置编码）** — 将位置信息通过旋转矩阵注入 attention score，天然表达相对位置，且具有远程衰减特性

---

## 核心组件 4：逐位置前馈网络

每个位置的表示独立通过相同的 MLP：

$$
\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2
$$

- 两层线性层 + ReLU（现在常用 SwiGLU / GeLU）
- 内层维度通常 $4\times$ 外层（如 512 → 2048 → 512）
- **每个位置独立**，但**参数共享**（类似 $1\times1$ 卷积）

> FFN 占据了 Transformer 约 2/3 的参数。研究表明 FFN 层在存储"知识"（key-value memory），注意力层负责"路由"。

---

## 核心组件 5：残差连接 + 层归一化

每层输出：

$$
\text{output} = \text{LayerNorm}(x + \text{Sublayer}(x))
$$

- **残差连接**：让梯度直通深层，解决退化问题
- **LayerNorm**：对每个样本的特征维度归一化（均值为 0，方差为 1），稳定训练
- **Pre-Norm vs Post-Norm**：现代实现多用 Pre-Norm（归一化在子层之前），训练更稳定

---

## 完整计算流程（Encoder Block）

```
输入 x (batch, seq_len, d_model)
  │
  ├─ LayerNorm
  ├─ Multi-Head Self-Attention
  ├─ + 残差连接 → x₁
  │
  ├─ LayerNorm
  ├─ FFN (SwiGLU)
  ├─ + 残差连接 → x₂
  │
  └─ 输出到下一层
```

Decoder 额外有 **Masked Self-Attention**（防止看到未来 token）和 **Cross-Attention**（查询编码器输出）。

---

## 为什么 Transformer 如此成功？

### 1. 计算特性

| 指标 | 复杂度 | 解释 |
|------|--------|------|
| 一层计算 | $O(T^2 \cdot d)$ | 注意力矩阵 $T \times T$ |
| 可并行化 | 极高 | 所有 token 同时处理 |
| 信息路径长度 | $O(1)$ | 任意两 token 一步直达 |
| 对比 RNN | $O(T)$ 步 | 信息需逐时间步传递 |

### 2. 缩放特性

Transformer 的损失随**计算量、参数量、数据量**的增大呈现可预测的幂律下降（scaling law），这使得它成为 LLM 的基础架构。

### 3. 归纳偏置少

CNN 有很强的局部性偏置（locality），RNN 有序列偏置。Transformer 几乎无先验归纳偏置，给了模型最大的学习自由度，但也意味着**小数据下容易过拟合**。

---

## 关键变体

| 模型 | 架构 | 核心创新 |
|------|------|---------|
| **BERT** | Encoder only | MLM + NSP 预训练 |
| **GPT 系列** | Decoder only | 自回归语言模型 + 提示学习 |
| **T5** | Encoder-Decoder | 统一文本到文本框架 |
| **ViT** | Encoder | 将图像切块做序列，纯 Transformer 视觉 |
| **Swin Transformer** | Encoder | 层次化 + 窗口注意力，降低计算量 |
| **LLaMA** | Decoder only | RoPE + SwiGLU + 高效训练 |

---

## 训练要点

- **学习率 Warmup**：先用线性预热（前几步从小 lr 上升到目标），再用余弦衰减。防止初始梯度爆炸。
- **Adam 优化器**（$\beta_1=0.9, \beta_2=0.98$）：比 SGD 更匹配 Transformer。
- **Dropout**：注意力权重和 FFN 都加，但在 GPT 等大规模模型中逐渐减少。
- **梯度裁剪**：全局 norm 限制在 1.0 左右。
- **混合精度训练**：FP16/BF16 加速，配合 Loss Scaling。

---

## 常见误区

| 误区 | 纠正 |
|------|------|
| Transformer 没有序列偏置 | 位置编码提供了偏置，但比 RNN 弱 |
| 注意力可以完全代替 CNN/RNN | 局部特征（边缘、纹理）CNN 仍有优势；序列数据 RNN 更高效 |
| 多头注意力每个头学不同模式 | 实践中头之间常有冗余，可以剪枝 |
| 越大越好 | 有最优计算分配：模型大小 × 数据量存在 trade-off |

---

## 实践清单

- [ ] 理解 Q/K/V 的物理含义：Query 是"找什么"，Key 是"有什么"，Value 是"给什么"
- [ ] 记住注意力复杂度 $O(T^2 d)$，T=1024 时约 10^6 大小，T=8192 时约 6.7×10^7
- [ ] Pre-Norm vs Post-Norm 选择：新项目一律 Pre-Norm
- [ ] 长序列考虑 FlashAttention、稀疏注意力、线性注意力
- [ ] 小数据集使用预训练模型（BERT/GPT）微调，不要从头训练

---

## 延伸阅读

- [原始论文] Attention Is All You Need (Vaswani et al., 2017)
- [知识图谱节点](/learning/deep-learning/architectures/transformer/) — 本笔记的精简版
- [注意力机制](/learning/deep-learning/architectures/attention-mechanism/) — 深入理解 QKV
- The Annotated Transformer (Harvard NLP)
- 3Blue1Brown 可视化 Transformer 系列

---
layout: single
title: "卷积神经网络 CNN"
permalink: /learning/deep-learning/architectures/cnn/
classes: wide
---

## 一句话定义
CNN 通过局部连接与参数共享建模空间局部相关性。

## 问题设定
- 输入：网格结构数据（图像、视频）。
- 输出：分类/回归/特征表示。
- 假设：局部平移不变性。
- 边界：全局依赖建模能力有限。

## 数学表述
卷积：
$$
 (X * W)_{i,j} = \sum_{u,v} X_{i+u, j+v} W_{u,v}
$$

## 算法解释
- 卷积核提取局部特征。
- 逐层堆叠扩大感受野。

## 优化与实现细节
- 目标来源：ERM/MLE。
- 数值要点：使用归一化与残差结构稳定训练。

## 关联与边界
- 对比 MLP：CNN 更适合空间结构。
- 对比 ViT：ViT 依赖大数据和注意力。
- 边界：对非网格结构不适用。

## 失败模式
- 过深导致梯度衰减。
- 数据不足导致过拟合。

## 最小伪代码
```text
Input: image X
Apply conv -> activation -> pooling
Repeat for layers
Return logits
```

## 决策清单
- [ ] 输入具有局部空间结构
- [ ] 数据量足够支撑卷积特征
- [ ] 与 ViT/MLP baseline 对比

## 个人备注
TODO

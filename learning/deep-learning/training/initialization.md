---
layout: single
title: "初始化 Initialization"
permalink: /learning/deep-learning/training/initialization/
classes: wide
---

## 一句话定义
初始化通过控制参数分布来稳定梯度传播并加速收敛。

## 问题设定
- 输入：网络结构、激活函数。
- 输出：参数初值 $W,b$。
- 假设：梯度传播对尺度敏感。
- 边界：不恰当初始化会导致梯度爆炸/消失。

## 数学表述
Xavier 初始化（tanh）：
$$
W_{ij} \sim \mathcal{U}\left(-\sqrt{\frac{6}{n_{in}+n_{out}}}, \sqrt{\frac{6}{n_{in}+n_{out}}}\right)
$$
He 初始化（ReLU）：
$$
W_{ij} \sim \mathcal{N}\left(0, \frac{2}{n_{in}}\right)
$$

## 算法解释
- 让前向/反向信号方差在层间保持稳定。

## 优化与实现细节
- 目标来源：方差传播分析。
- 数值要点：与激活函数匹配；偏置多用零初始化。

## 关联与边界
- 与归一化强相关；归一化可缓解初始化敏感性。
- 边界：残差结构降低初始化风险。

## 失败模式
- 过大方差导致梯度爆炸。
- 过小方差导致梯度消失。

## 最小伪代码
```text
Input: layer sizes, activation
Select Xavier or He
Sample weights
```

## 决策清单
- [ ] 激活函数已匹配初始化
- [ ] 观察梯度/激活统计
- [ ] 与归一化配套

## 个人备注
TODO

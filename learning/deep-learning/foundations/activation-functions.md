---
layout: single
title: "激活函数 Activation Functions"
permalink: /learning/deep-learning/foundations/activation-functions/
classes: wide
---

## 一句话定义
激活函数引入非线性，使神经网络能表达非线性映射。

## 问题设定
- 输入：线性变换输出 $z$。
- 输出：激活 $a = \phi(z)$。
- 假设：激活可导或可取次导。
- 边界：不恰当激活导致训练不稳定。

## 数学表述
常见激活：
$$
\text{ReLU}(z)=\max(0,z),\quad \sigma(z)=\frac{1}{1+e^{-z}},\quad \tanh(z)
$$

## 算法解释
- 决定梯度流形与信号传播。
- ReLU 缓解梯度消失但可能“死亡”。

## 优化与实现细节
- 目标来源：非线性表示能力。
- 选择：ReLU/LeakyReLU 用于深层，tanh/sigmoid 用于门控。
- 数值要点：饱和区梯度小。

## 关联与边界
- 与归一化、初始化强相关。
- 边界：激活选择影响可训练性与表达。

## 失败模式
- Sigmoid 饱和导致梯度消失。
- ReLU 死亡导致通道失活。

## 最小伪代码
```text
Input: z
Return phi(z)
```

## 决策清单
- [ ] 深度与激活类型匹配
- [ ] 梯度流动可接受
- [ ] 与归一化/初始化协调

## 个人备注
TODO

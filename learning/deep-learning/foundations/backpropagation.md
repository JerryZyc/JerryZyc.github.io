---
layout: single
title: "反向传播 Backpropagation"
permalink: /learning/deep-learning/foundations/backpropagation/
classes: wide
---

## 一句话定义
反向传播是利用链式法则高效计算复合函数梯度的算法。

## 问题设定
- 输入：计算图、损失函数 $L$。
- 输出：各参数梯度 $\nabla_\theta L$。
- 假设：计算图可微。
- 边界：不可微点需次梯度或近似。

## 数学表述
对复合函数 $L = f(g(h(\theta)))$：
$$
\frac{\partial L}{\partial \theta} = \frac{\partial L}{\partial f} \cdot \frac{\partial f}{\partial g} \cdot \frac{\partial g}{\partial h} \cdot \frac{\partial h}{\partial \theta}
$$

## 算法解释
- 前向计算保存中间值。
- 反向按拓扑序传播梯度。

## 优化与实现细节
- 目标来源：链式法则。
- 实现：自动微分（反向模式）。
- 数值要点：避免梯度消失/爆炸。

## 关联与边界
- 对比数值微分：反向传播更精确且高效。
- 对比符号微分：反向传播适合大规模计算图。
- 边界：非可微操作需替代或平滑。

## 失败模式
- 梯度消失或爆炸。
- 计算图断裂导致梯度为零。

## 最小伪代码
```text
Forward pass: compute activations
Backward pass: propagate gradients by chain rule
Update parameters
```

## 决策清单
- [ ] 计算图可微
- [ ] 梯度稳定性已考虑
- [ ] 自动微分框架可靠

## 个人备注
TODO

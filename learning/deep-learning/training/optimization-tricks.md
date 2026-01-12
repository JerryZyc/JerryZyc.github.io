---
layout: single
title: "优化技巧 Optimization Tricks"
permalink: /learning/deep-learning/training/optimization-tricks/
classes: wide
---

## 一句话定义
优化技巧通过改进学习率、动量与调度策略提升收敛速度与稳定性。

## 问题设定
- 输入：优化器与学习率策略。
- 输出：更稳定的训练过程。
- 假设：梯度噪声与曲率会影响收敛。
- 边界：技巧依赖任务与模型规模。

## 数学表述
动量：
$$
 v_{t+1} = \mu v_t + \nabla f(\theta_t), \quad \theta_{t+1} = \theta_t - \eta v_{t+1}
$$
学习率调度（余弦）：
$$
\eta_t = \eta_{min} + \frac{1}{2}(\eta_{max}-\eta_{min})(1+\cos(\pi t/T))
$$

## 算法解释
- 动量加速一致方向、抑制震荡。
- 调度避免后期震荡。

## 优化与实现细节
- 数值要点：warmup、梯度裁剪、权重衰减区分 L2。

## 关联与边界
- 与优化器选择（SGD/Adam）直接相关。
- 边界：过多技巧叠加可能适得其反。

## 失败模式
- 学习率过大导致发散。
- 调度与 batch size 不匹配。

## 最小伪代码
```text
Select optimizer and lr schedule
Train with warmup and decay
Monitor loss/gradients
```

## 决策清单
- [ ] 学习率范围已验证
- [ ] 调度策略适配训练时长
- [ ] 监控梯度稳定性

## 个人备注
TODO

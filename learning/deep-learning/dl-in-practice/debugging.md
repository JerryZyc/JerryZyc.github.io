---
layout: single
title: "调试 Debugging"
permalink: /learning/deep-learning/dl-in-practice/debugging/
classes: wide
---

## 一句话定义
调试是定位训练异常与性能异常的系统性流程。

## 问题设定
- 输入：训练日志、指标曲线、样本。
- 输出：问题定位与修复策略。
- 假设：异常可通过可观测信号定位。
- 边界：复杂系统常需逐层排查。

## 数学表述
核心是监控损失与梯度统计量，例如：
$$
\|\nabla \theta\|_2,\quad \mathbb{E}[\ell],\quad \text{Var}(\ell)
$$

## 算法解释
- 从数据管道、模型、优化器三层排查。
- 先保证过拟合小样本再扩展。

## 优化与实现细节
- 数值要点：固定随机种子、逐步简化组件。

## 关联与边界
- 与过拟合、数值稳定性强相关。
- 边界：日志不足时需增加监控。

## 失败模式
- 问题定位偏离导致无效修复。
- 一次性改动过多导致混淆。

## 最小伪代码
```text
Check data -> check model -> check optimizer
Overfit small batch
Scale up
```

## 决策清单
- [ ] 小样本可过拟合
- [ ] 梯度与损失稳定
- [ ] 数据管道无异常

## 个人备注
TODO

---
layout: single
title: "评估指标 Evaluation Metrics"
permalink: /learning/machine-learning/fundamentals/evaluation-metrics/
classes: wide
---

## 一句话定义
评估指标将模型输出映射为可比较的量化分数，必须与任务目标一致。

## 问题设定
- 输入：预测 $\hat{y}$ 与真实标签 $y$。
- 输出：标量评分或指标集合。
- 假设：评价标准与业务目标一致。
- 边界：不匹配指标会误导模型选择。

## 数学表述
- 回归：$\text{MSE} = \frac{1}{n} \sum_i (y_i - \hat{y}_i)^2$。
- 分类：准确率 $\frac{1}{n} \sum_i \mathbf{1}(y_i=\hat{y}_i)$，或 F1、AUC。

## 算法解释
- 不同指标对应不同权衡（精度/召回/风险）。
- 指标选择影响模型调优方向。

## 优化与实现细节
- 目标来源：统计误差或业务损失。
- 选择：不平衡数据优先 F1/AUC。
- 数值要点：阈值选择与校准。

## 关联与边界
- 与损失函数相关但不等同。
- 边界：优化指标与评估指标不一致会导致错配。

## 失败模式
- 仅用准确率忽略不平衡。
- 过度调参导致指标过拟合。

## 最小伪代码
```text
Input: y_true, y_pred
Compute metric by task
Report with confidence interval if possible
```

## 决策清单
- [ ] 指标与业务目标一致
- [ ] 不平衡时使用合适指标
- [ ] 指标稳定性验证

## 个人备注
TODO

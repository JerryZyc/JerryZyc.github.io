---
layout: single
title: "问题类型 Problem Types"
permalink: /learning/machine-learning/fundamentals/problem-types/
classes: wide
---

## 一句话定义
机器学习问题类型由监督信号与目标形式决定，常见为回归、分类、聚类与表示学习。

## 问题设定
- 输入：$x$ 或 $(x,y)$。
- 输出：连续值、离散标签或潜在表示。
- 假设：数据分布可被建模。
- 边界：不同类型目标函数与评估指标不可混用。

## 数学表述
- 回归：$y \in \mathbb{R}$，最小化 $\ell(\hat{y}, y)$。
- 分类：$y \in \{1,\dots,C\}$，最小化交叉熵。
- 聚类：最小化组内距离或最大化似然。

## 算法解释
- 回归强调数值预测。
- 分类强调决策边界与概率。
- 聚类强调结构发现与相似性度量。

## 优化与实现细节
- 目标来源：ERM/MLE。
- 指标：回归用 MSE/MAE，分类用准确率/F1/ROC，聚类用 NMI/ARI。
- 数值要点：损失与指标要匹配任务。

## 关联与边界
- 回归与分类可通过链接函数互相转换。
- 聚类与密度估计紧密相关。
- 边界：监督 vs 无监督决定可用信息量。

## 失败模式
- 任务定义错误导致指标不反映真实目标。
- 用分类指标评估回归或相反。

## 最小伪代码
```text
Input: data D, task type
Choose model and loss by task
Train model
Evaluate with matching metric
```

## 决策清单
- [ ] 目标变量类型明确
- [ ] 损失与评估指标一致
- [ ] 与相邻任务边界清晰

## 个人备注
TODO

---
layout: single
title: "超参调优 Hyperparameter Tuning"
permalink: /learning/machine-learning/ml-in-practice/hyperparameter-tuning/
classes: wide
---

## 一句话定义
超参调优是在固定模型族下寻找性能最优的超参数组合。

## 问题设定
- 输入：超参数空间 $\Lambda$，评估指标 $m$。
- 输出：近似最优超参数 $\lambda^*$。
- 假设：评估过程可重复且稳定。
- 边界：搜索成本与预算限制明显。

## 数学表述

$$
\lambda^* = \arg\max_{\lambda \in \Lambda} \; m(\mathcal{M}_\lambda; \mathcal{D}_{val})
$$

## 算法解释
- 网格搜索适合低维、随机搜索适合高维。
- 贝叶斯优化利用历史试验进行代理建模。

## 优化与实现细节
- 目标来源：验证集指标。
- 方法：交叉验证、早停、逐步缩小空间。
- 数值要点：避免过拟合验证集。

## 关联与边界
- 与模型选择和评估指标强相关。
- 边界：训练资源不足会限制搜索质量。

## 失败模式
- 过度调参导致验证集过拟合。
- 评估噪声大导致搜索方向错误。

## 最小伪代码
```text
Define search space
For each trial:
  Train model
  Evaluate on validation
Select best hyperparameters
```

## 决策清单
- [ ] 搜索空间定义合理
- [ ] 评估流程可重复
- [ ] 验证集或交叉验证避免泄漏

## 个人备注
TODO

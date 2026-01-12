---
layout: single
title: "训练-测试划分 Train Test Split"
permalink: /learning/machine-learning/fundamentals/train-test-split/
classes: wide
---

## 一句话定义
训练-测试划分用于估计模型泛化能力，避免在同一数据上评估导致的乐观偏差。

## 问题设定
- 输入：完整数据集 $\mathcal{D}$。
- 输出：训练集与测试集。
- 假设：样本独立同分布。
- 边界：时序数据需保持时间顺序。

## 数学表述
划分比例：$\mathcal{D} = \mathcal{D}_{train} \cup \mathcal{D}_{test}$，且 $\mathcal{D}_{train} \cap \mathcal{D}_{test} = \emptyset$。

## 算法解释
- 将模型训练与评估解耦。
- 评估时仅使用测试集一次。

## 优化与实现细节
- 常用比例 8/2 或 7/3。
- 小数据集使用交叉验证。
- 数值要点：防止泄漏（特征、标准化、数据增强）。

## 关联与边界
- 与交叉验证、数据泄漏紧密相关。
- 边界：在线学习需滚动验证。

## 失败模式
- 数据泄漏导致测试偏高。
- 过小测试集导致评估不稳定。

## 最小伪代码
```text
Shuffle data
Split into train/test
Train on train
Evaluate on test
```

## 决策清单
- [ ] 划分符合数据生成机制
- [ ] 测试集只使用一次
- [ ] 无数据泄漏

## 个人备注
TODO

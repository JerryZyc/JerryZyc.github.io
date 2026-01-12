---
layout: single
title: "尺度定律 Scaling Laws"
permalink: /learning/deep-learning/dl-in-practice/scaling-laws/
classes: wide
---

## 一句话定义
尺度定律描述模型规模、数据规模与计算预算之间的幂律关系。

## 问题设定
- 输入：模型参数规模 $N$、数据量 $D$、计算量 $C$。
- 输出：性能随规模变化的趋势估计。
- 假设：在足够大规模下近似幂律。
- 边界：小规模下不成立。

## 数学表述
经验幂律：
$$
\mathcal{L} \approx a N^{-\alpha} + b D^{-\beta} + c
$$

## 算法解释
- 性能提升遵循边际收益递减。

## 优化与实现细节
- 数值要点：模型-数据-算力需匹配，否则浪费。

## 关联与边界
- 与算力预算规划强相关。
- 边界：幂律系数依任务而异。

## 失败模式
- 规模不匹配导致性能不增反降。
- 盲目扩大模型造成训练不稳定。

## 最小伪代码
```text
Estimate scaling curve
Allocate budget for N, D, C
Train accordingly
```

## 决策清单
- [ ] 规模与预算匹配
- [ ] 数据质量可支撑扩大
- [ ] 训练稳定性保障

## 个人备注
TODO

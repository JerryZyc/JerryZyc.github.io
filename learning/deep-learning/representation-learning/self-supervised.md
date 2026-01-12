---
layout: single
title: "自监督 Self Supervised"
permalink: /learning/deep-learning/representation-learning/self-supervised/
classes: wide
---

## 一句话定义
自监督通过构造代理任务在无标签数据上学习可迁移表示。

## 问题设定
- 输入：未标注数据 $x$。
- 输出：表示模型 $f_\theta$。
- 假设：代理任务与下游任务相关。
- 边界：代理任务设计不当会学到无关特征。

## 数学表述
通用形式：
$$
\min_{\theta} \; \mathbb{E}_{x \sim \mathcal{D}} \; \ell(g(f_\theta(x)), \tilde{x})
$$
其中 $\tilde{x}$ 为构造的预测目标。

## 算法解释
- 通过预测缺失片段、对比样本或重构来学习。

## 优化与实现细节
- 数值要点：任务设计与增强策略决定表示质量。

## 关联与边界
- 与对比学习、掩码建模同属自监督范式。
- 边界：对下游任务迁移不一定有效。

## 失败模式
- 代理任务过于简单导致表示退化。
- 训练分布与目标任务偏离。

## 最小伪代码
```text
Design pretext task
Train model to solve task
Transfer representation to downstream
```

## 决策清单
- [ ] 代理任务与目标相关
- [ ] 数据规模足够
- [ ] 迁移评估完成

## 个人备注
TODO

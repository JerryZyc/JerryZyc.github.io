---
layout: single
title: "课程学习 Curriculum Learning"
permalink: /learning/reinforcement-learning/rl-in-practice/curriculum-learning/
classes: wide
---

## 一句话定义
课程学习通过从易到难组织训练分布，提高学习稳定性与样本效率。

## 问题设定
- 输入：任务难度维度与采样策略。
- 输出：逐步提升的训练任务序列。
- 假设：任务可分级。
- 边界：不当课程导致策略偏差。

## 数学表述
课程可以表示为分布序列 $p_k(\mathcal{T})$：
$$
\mathcal{T}_1 \rightarrow \mathcal{T}_2 \rightarrow \cdots
$$

## 算法解释
- 先解决简单任务再扩展到复杂任务。

## 优化与实现细节
- 数值要点：课程切换阈值与自动调度。

## 关联与边界
- 与奖励设计、探索策略强相关。
- 边界：训练分布与测试分布偏离。

## 失败模式
- 课程过于保守导致泛化不足。
- 课程过激导致训练崩溃。

## 最小伪代码
```text
Initialize easy task distribution
Train until threshold
Increase difficulty
```

## 决策清单
- [ ] 难度维度可控
- [ ] 课程切换标准明确
- [ ] 泛化评估充分

## 个人备注
TODO

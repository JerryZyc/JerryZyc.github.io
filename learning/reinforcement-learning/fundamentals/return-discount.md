---
layout: single
title: "回报与折扣 Return Discount"
permalink: /learning/reinforcement-learning/fundamentals/return-discount/
classes: wide
---

## 一句话定义
折扣因子控制未来回报的重要性，决定长期规划与稳定性权衡。

## 问题设定
- 输入：回报序列 $r_t$。
- 输出：折扣回报 $G_t$。
- 假设：回报可累积且有衰减。
- 边界：$\gamma$ 过大易不稳定，过小短视。

## 数学表述
$$
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}
$$

## 算法解释
- $\gamma$ 越大越重视长期收益。

## 优化与实现细节
- 数值要点：无穷和可用截断回报近似。

## 关联与边界
- 与稳定性与收敛性相关。
- 边界：有限时域任务可用 $\gamma=1$。

## 失败模式
- 过大 $\gamma$ 导致方差过高。
- 过小 $\gamma$ 导致策略短视。

## 最小伪代码
```text
Compute discounted return G_t
```

## 决策清单
- [ ] 任务时域清晰
- [ ] 折扣因子与稳定性匹配
- [ ] 方差可接受

## 个人备注
TODO

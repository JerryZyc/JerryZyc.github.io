---
layout: single
title: "蒙特卡洛 Monte Carlo"
permalink: /learning/reinforcement-learning/model-free-rl/monte-carlo/
classes: wide
---

## 一句话定义
蒙特卡洛方法通过完整回合样本估计回报并进行价值或策略评估。

## 问题设定
- 输入：轨迹 $\tau = (s_0,a_0,r_0,\dots)$。
- 输出：价值估计或策略。
- 假设：可采样完整回合。
- 边界：高方差，需足够样本。

## 数学表述
回报：
$$
G_t = \sum_{k=0}^{T-t-1} \gamma^k r_{t+k}
$$
价值估计：
$$
V^\pi(s) \approx \frac{1}{N(s)} \sum_{i: s_i=s} G_i
$$

## 算法解释
- 无需模型，直接用回合样本估计期望。

## 优化与实现细节
- 目标来源：样本均值近似期望。
- 数值要点：首次访问/每次访问 MC；方差大。

## 关联与边界
- 对比 TD：MC 使用完整回合，TD 用自举。
- 边界：回合很长时效率低。

## 失败模式
- 回合长度大导致估计不稳定。
- 高方差导致收敛慢。

## 最小伪代码
```text
Generate episodes
For each state in episode:
  Update V with return G
```

## 决策清单
- [ ] 可采样完整回合
- [ ] 方差可接受
- [ ] 与 TD 对比

## 个人备注
TODO

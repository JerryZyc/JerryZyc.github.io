---
layout: single
title: "部分可观测马尔可夫决策过程 POMDP"
permalink: /learning/reinforcement-learning/fundamentals/pomdp/
classes: wide
---

## 一句话定义
POMDP 在 MDP 基础上引入观测函数，处理状态不可完全观测的决策问题。

## 问题设定
- 输入：$S,A,P,R,O,Z$。
- 输出：策略 $\pi(a\mid o)$ 或 $\pi(a\mid b)$。
- 假设：观测仅部分反映状态。
- 边界：状态估计或记忆成为关键。

## 数学表述
观测模型：
$$
Z(o\mid s,a)
$$

Belief 更新：
$$
b'(s') = \eta \, Z(o'\mid s',a) \sum_{s} P(s'\mid s,a) b(s)
$$

## 算法解释
- 决策基于 belief state 而非真实状态。

## 优化与实现细节
- 数值要点：需要状态估计或递归记忆模型。

## 关联与边界
- 对比 MDP：引入观测不确定性。
- 边界：高维 belief 空间难以求解。

## 失败模式
- 观测噪声导致策略不稳定。
- 记忆模型不足以恢复状态。

## 最小伪代码
```text
Maintain belief b(s)
Update belief with observations
Select action by policy
```

## 决策清单
- [ ] 观测模型可用或可估计
- [ ] 有状态估计或记忆结构
- [ ] 评估部分可观测影响

## 个人备注
TODO

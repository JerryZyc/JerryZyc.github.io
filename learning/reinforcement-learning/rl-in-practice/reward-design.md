---
layout: single
title: "奖励设计 Reward Design"
permalink: /learning/reinforcement-learning/rl-in-practice/reward-design/
classes: wide
---

## 一句话定义
奖励设计决定智能体的学习目标与行为偏好，是 RL 成功与否的关键工程环节。

## 问题设定
- 输入：任务目标与环境状态。
- 输出：奖励函数 $R(s,a,s')$。
- 假设：奖励能够表达任务意图。
- 边界：不当奖励导致策略偏差或欺骗性行为。

## 数学表述
回报：
$$
G_t = \sum_{k=0}^\infty \gamma^k r_{t+k}
$$
奖励塑形：
$$
R'(s,a,s') = R(s,a,s') + F(s') - F(s)
$$

## 算法解释
- 稀疏奖励适合明确终止条件。
- 稠密奖励加速学习但可能引入偏差。

## 优化与实现细节
- 数值要点：奖励尺度影响梯度与稳定性；需归一化或裁剪。

## 关联与边界
- 与信用分配、探索直接相关。
- 边界：奖励塑形不当会改变最优策略。

## 失败模式
- 奖励黑客（reward hacking）。
- 探索不足导致陷入局部最优。

## 最小伪代码
```text
Define task goal
Design reward function
Validate with rollouts
```

## 决策清单
- [ ] 奖励与任务目标一致
- [ ] 避免可被利用的漏洞
- [ ] 奖励尺度稳定

## 个人备注
TODO

---
layout: single
title: "SARSA"
permalink: /learning/reinforcement-learning/model-free-rl/sarsa/
classes: wide
---

## 一句话定义
SARSA 使用在策略采样更新动作价值函数。

## 问题设定
- 输入：转移 $(s,a,r,s',a')$。
- 输出：$Q(s,a)$。
- 假设：策略用于采样与更新一致。
- 边界：学习较保守。

## 数学表述
更新：
$$
Q(s,a) \leftarrow Q(s,a) + \alpha \big(r + \gamma Q(s',a') - Q(s,a)\big)
$$

## 算法解释
- 与 Q-learning 相比更稳定但收敛慢。

## 优化与实现细节
- 数值要点：探索策略影响目标。

## 关联与边界
- 对比 Q-learning：SARSA 在策略，Q-learning 离策略。

## 失败模式
- 探索不足导致次优策略。
- 学习率不当导致不稳定。

## 最小伪代码
```text
For each transition:
  target = r + gamma * Q(s',a')
  Q(s,a) = Q(s,a) + alpha * (target - Q(s,a))
```

## 决策清单
- [ ] 需要在策略更新
- [ ] 探索策略稳定
- [ ] 与 Q-learning 基线对比

## 个人备注
TODO

---
layout: single
title: "Q 学习 Q Learning"
permalink: /learning/reinforcement-learning/model-free-rl/q-learning/
classes: wide
---

## 一句话定义
Q 学习通过离策略 TD 更新逼近最优动作价值函数。

## 问题设定
- 输入：转移 $(s,a,r,s')$。
- 输出：$Q(s,a)$。
- 假设：可探索足够覆盖状态-动作。
- 边界：函数逼近时可能不稳定。

## 数学表述
更新：
$$
Q(s,a) \leftarrow Q(s,a) + \alpha \big(r + \gamma \max_{a'} Q(s',a') - Q(s,a)\big)
$$

## 算法解释
- 使用贪婪目标动作自举。

## 优化与实现细节
- 数值要点：探索策略（$\epsilon$-greedy）。

## 关联与边界
- 对比 SARSA：SARSA 为在策略更新。
- 边界：离策略 + 函数逼近可能发散。

## 失败模式
- 过度贪婪导致欠探索。
- 近似误差引发发散。

## 最小伪代码
```text
For each transition:
  target = r + gamma * max_a' Q(s',a')
  Q(s,a) = Q(s,a) + alpha * (target - Q(s,a))
```

## 决策清单
- [ ] 探索策略合理
- [ ] 状态-动作覆盖充分
- [ ] 函数逼近稳定性控制

## 个人备注
TODO

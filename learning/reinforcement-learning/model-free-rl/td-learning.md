---
layout: single
title: "TD 学习 TD Learning"
permalink: /learning/reinforcement-learning/model-free-rl/td-learning/
classes: wide
---

## 一句话定义
时序差分通过自举更新价值估计，结合 MC 与 DP 的优点。

## 问题设定
- 输入：在线样本 $(s_t,a_t,r_t,s_{t+1})$。
- 输出：价值函数估计。
- 假设：可逐步采样。
- 边界：估计偏差来自自举。

## 数学表述
TD(0) 误差：
$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
$$
更新：
$$
V(s_t) \leftarrow V(s_t) + \alpha \delta_t
$$

## 算法解释
- 使用下一步估计替代完整回合回报。

## 优化与实现细节
- 数值要点：步长 $\alpha$ 控制稳定性。

## 关联与边界
- 对比 MC：TD 方差低但有偏。
- 对比 DP：TD 不需模型。

## 失败模式
- 自举误差累积。
- 步长不当导致不稳定。

## 最小伪代码
```text
For each transition:
  delta = r + gamma V(s') - V(s)
  V(s) = V(s) + alpha * delta
```

## 决策清单
- [ ] 在线更新需求明确
- [ ] 步长与稳定性可控
- [ ] 估计偏差可接受

## 个人备注
TODO

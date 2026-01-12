---
layout: single
title: "深度 Q 网络 DQN"
permalink: /learning/reinforcement-learning/deep-rl/dqn/
classes: wide
---

## 一句话定义
DQN 用神经网络近似 $Q(s,a)$，结合经验回放与目标网络稳定离策略学习。

## 问题设定
- 输入：状态 $s$，动作 $a$。
- 输出：近似动作价值 $Q_\theta(s,a)$。
- 假设：可获得交互样本，状态可表示为向量或图像。
- 边界：连续动作需改用其他算法（如 DDPG/SAC）。

## 数学表述
损失函数（目标网络）：
$$
\mathcal{L}(\theta) = \mathbb{E}\big[(r + \gamma \max_{a'} Q_{\theta^-}(s',a') - Q_\theta(s,a))^2\big]
$$

## 算法解释
- 经验回放打破样本相关性。
- 目标网络降低目标漂移。

## 优化与实现细节
- 目标来源：离策略 TD 误差。
- 数值要点：使用固定频率更新目标网络；优先回放提升效率。

## 关联与边界
- 对比 Q-learning：DQN 以函数逼近实现。
- 对比 Double DQN：减轻过估计偏差。
- 边界：对超参数敏感。

## 失败模式
- 过估计导致不稳定。
- 目标网络更新过快导致发散。

## 最小伪代码
```text
Initialize Q, target Q-
Repeat:
  Sample batch from replay
  Compute target with Q-
  Update Q by TD loss
  Periodically update Q-
```

## 决策清单
- [ ] 离散动作空间
- [ ] 经验回放与目标网络实现正确
- [ ] 与 Double/Dueling 变体对比

## 个人备注
TODO

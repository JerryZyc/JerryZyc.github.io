---
layout: single
title: "软演员-评论家 SAC"
permalink: /learning/reinforcement-learning/deep-rl/sac/
classes: wide
---

## 一句话定义
SAC 通过最大化回报与熵的加权和，实现高样本效率的离策略学习。

## 问题设定
- 输入：策略 $\pi_\theta$、Q 函数 $Q_\phi$。
- 输出：最大熵最优策略。
- 假设：连续动作空间。
- 边界：离策略训练需稳定的目标网络。

## 数学表述
最大熵目标：
$$
J(\pi) = \sum_t \mathbb{E}[r_t + \alpha \mathcal{H}(\pi(\cdot\mid s_t))]
$$
软 Q 更新：
$$
Q(s,a) = r + \gamma \mathbb{E}_{a'\sim\pi}[Q(s',a') - \alpha \log \pi(a'\mid s')]
$$

## 算法解释
- 熵项鼓励探索并提升鲁棒性。

## 优化与实现细节
- 数值要点：温度 $\alpha$ 可自适应调整。

## 关联与边界
- 对比 DDPG：SAC 更稳定但计算量更大。
- 边界：离策略训练需经验回放。

## 失败模式
- 熵权重不当导致策略过度随机或过度确定。
- Q 过估计导致不稳定。

## 最小伪代码
```text
Sample replay
Update Q networks
Update policy with entropy term
```

## 决策清单
- [ ] 连续动作场景
- [ ] 需要高样本效率
- [ ] 温度参数可调

## 个人备注
TODO

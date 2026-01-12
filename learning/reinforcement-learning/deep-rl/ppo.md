---
layout: single
title: "近端策略优化 PPO"
permalink: /learning/reinforcement-learning/deep-rl/ppo/
classes: wide
---

## 一句话定义
PPO 通过裁剪目标函数限制策略更新幅度，提升训练稳定性。

## 问题设定
- 输入：旧策略 $\pi_{\theta_{old}}$ 与新策略 $\pi_\theta$。
- 输出：更新后的策略。
- 假设：策略可微且可采样。
- 边界：仍为 on-policy，样本效率有限。

## 数学表述
概率比率：
$$
r_t(\theta) = \frac{\pi_\theta(a_t\mid s_t)}{\pi_{\theta_{old}}(a_t\mid s_t)}
$$
裁剪目标：
$$
L^{\text{clip}} = \mathbb{E}[\min(r_t A_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon) A_t)]
$$

## 算法解释
- 裁剪限制策略改变幅度，避免破坏性更新。

## 优化与实现细节
- 数值要点：优势归一化与多轮小批次更新。

## 关联与边界
- 对比 TRPO：PPO 更易实现但约束更弱。
- 边界：对超参数敏感。

## 失败模式
- $\epsilon$ 设置不当导致学习停滞或不稳定。
- Advantage 估计噪声大。

## 最小伪代码
```text
Collect rollouts
Compute advantages
Optimize clipped objective
```

## 决策清单
- [ ] 需要稳定的 on-policy 方法
- [ ] 采样效率可接受
- [ ] 超参数已调节

## 个人备注
TODO

---
layout: single
title: "多智能体 Multi Agent RL"
permalink: /learning/reinforcement-learning/advanced-topics/multi-agent-rl/
classes: wide
---

## 一句话定义
多智能体强化学习研究多个策略在共享环境中协作或竞争的学习问题。

## 问题设定
- 输入：多智能体状态与动作空间。
- 输出：各智能体策略。
- 假设：环境对单个智能体非平稳。
- 边界：训练不稳定、信用分配难。

## 数学表述
联合策略：
$$
\pi(a_1,\dots,a_n\mid s) = \prod_{i=1}^n \pi_i(a_i\mid o_i)
$$

## 算法解释
- 需要解决协作/竞争与通信问题。

## 优化与实现细节
- 数值要点：集中训练分散执行（CTDE）。

## 关联与边界
- 与信用分配和稳定性问题紧密相关。
- 边界：规模扩大导致指数复杂度。

## 失败模式
- 环境非平稳导致策略振荡。
- 协作信号稀疏导致学习缓慢。

## 最小伪代码
```text
Train agents with centralized critic
Deploy decentralized policies
```

## 决策清单
- [ ] 交互结构明确（协作/竞争）
- [ ] 采用 CTDE 或通信机制
- [ ] 可扩展性评估

## 个人备注
TODO

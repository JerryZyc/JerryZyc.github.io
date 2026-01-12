---
layout: single
title: "记忆与递归 Memory Recurrence"
permalink: /learning/reinforcement-learning/advanced-topics/memory-recurrence/
classes: wide
---

## 一句话定义
记忆与递归结构用于在部分可观测环境中保留历史信息。

## 问题设定
- 输入：观测序列 $o_t$。
- 输出：隐状态 $h_t$ 或记忆表示。
- 假设：历史信息对决策关键。
- 边界：长记忆学习难度高。

## 数学表述
递归更新：
$$
 h_t = f(h_{t-1}, o_t)
$$

## 算法解释
- 使用 RNN/LSTM/Transformer 形成隐式 belief。

## 优化与实现细节
- 数值要点：梯度稳定与截断 BPTT。

## 关联与边界
- 与 POMDP 强相关。
- 边界：记忆不足导致策略退化。

## 失败模式
- 梯度消失导致记忆衰退。
- 记忆漂移导致错误策略。

## 最小伪代码
```text
For each timestep:
  h = f(h, o)
  a = pi(h)
```

## 决策清单
- [ ] 任务部分可观测
- [ ] 选择合适记忆结构
- [ ] 训练稳定性保证

## 个人备注
TODO

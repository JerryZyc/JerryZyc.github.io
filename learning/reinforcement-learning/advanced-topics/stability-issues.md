---
layout: single
title: "稳定性问题 Stability Issues"
permalink: /learning/reinforcement-learning/advanced-topics/stability-issues/
classes: wide
---

## 一句话定义
稳定性问题指 RL 训练易发散、退化或高度敏感于超参数。

## 问题设定
- 输入：训练过程与超参数。
- 输出：稳定性诊断与缓解策略。
- 假设：函数逼近与自举引入不稳定。
- 边界：部分问题无法完全消除不稳定。

## 数学表述
不稳定通常表现为价值估计误差累积：
$$
\|Q_{t+1} - Q_t\| \gg 0
$$

## 算法解释
- Bootstrapping + 函数逼近 + 离策略构成“致命三角”。

## 优化与实现细节
- 数值要点：目标网络、双重估计、正则化。

## 关联与边界
- 与离策略方法、函数逼近强相关。
- 边界：稳定性与样本效率常有权衡。

## 失败模式
- 训练崩溃或价值爆炸。
- 策略退化为随机。

## 最小伪代码
```text
Monitor Q/return variance
Apply target networks and clipping
```

## 决策清单
- [ ] 识别三角风险
- [ ] 稳定化措施到位
- [ ] 监控发散指标

## 个人备注
TODO

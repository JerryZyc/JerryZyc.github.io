---
layout: single
title: "信用分配 Credit Assignment"
permalink: /learning/reinforcement-learning/advanced-topics/credit-assignment/
classes: wide
---

## 一句话定义
信用分配解决长期回报中哪些动作对结果贡献最大的因果问题。

## 问题设定
- 输入：长期回报信号。
- 输出：各时间步或模块的贡献估计。
- 假设：回报信号可拆解。
- 边界：长时延导致方差高。

## 数学表述
TD 误差为一种局部信用信号：
$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
$$

## 算法解释
- 通过回溯或优势函数分配信用。
- 使用 eligibility traces 或 GAE 改善。

## 优化与实现细节
- 数值要点：GAE 平衡偏差与方差。

## 关联与边界
- 与稀疏奖励、长时序任务强相关。
- 边界：过长延迟仍难以准确分配。

## 失败模式
- 信用延迟导致学习缓慢。
- 错误信用分配导致策略崩溃。

## 最小伪代码
```text
Compute advantage estimates
Use as credit signal for policy update
```

## 决策清单
- [ ] 奖励稀疏程度可控
- [ ] 采用 GAE 或其他平衡方法
- [ ] 评估信用分配稳定性

## 个人备注
TODO

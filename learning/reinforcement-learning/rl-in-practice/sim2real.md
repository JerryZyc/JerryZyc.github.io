---
layout: single
title: "仿真到现实 Sim2real"
permalink: /learning/reinforcement-learning/rl-in-practice/sim2real/
classes: wide
---

## 一句话定义
Sim2real 旨在将仿真中学到的策略迁移到真实系统并保持性能。

## 问题设定
- 输入：仿真策略与真实环境。
- 输出：可部署策略。
- 假设：仿真与现实存在可补偿差异。
- 边界：建模误差大时迁移失败。

## 数学表述
域随机化：
$$
\theta \sim p(\theta), \quad s \sim \mathcal{T}_\theta
$$

## 算法解释
- 通过随机化仿真参数提升鲁棒性。
- 结合系统辨识或在线微调。

## 优化与实现细节
- 数值要点：随机化范围需覆盖真实分布。

## 关联与边界
- 与 domain adaptation、系统辨识相关。
- 边界：真实环境不可安全探索时受限。

## 失败模式
- 仿真误差导致策略崩溃。
- 现实噪声未覆盖。

## 最小伪代码
```text
Randomize sim parameters
Train policy
Deploy and evaluate
```

## 决策清单
- [ ] 仿真误差范围已评估
- [ ] 随机化参数覆盖真实分布
- [ ] 安全验证到位

## 个人备注
TODO

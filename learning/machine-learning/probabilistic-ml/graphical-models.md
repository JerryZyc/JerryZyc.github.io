---
layout: single
title: "图模型 Graphical Models"
permalink: /learning/machine-learning/probabilistic-ml/graphical-models/
classes: wide
---

## 一句话定义
图模型用图结构表示变量依赖关系，从而实现复杂分布的分解与高效推断。

## 问题设定
- 输入：随机变量集合 $\{X_i\}$ 与依赖结构。
- 输出：联合分布因子分解与推断/学习算法。
- 假设：条件独立关系可由图表示。
- 边界：图结构错设会误导推断。

## 数学表述
贝叶斯网络分解：
$$
p(x_1,\dots,x_n) = \prod_{i=1}^n p(x_i\mid \text{pa}(x_i))
$$
马尔可夫随机场分解：
$$
p(x) = \frac{1}{Z} \prod_{c \in \mathcal{C}} \psi_c(x_c)
$$

## 算法解释
- 结构表示条件独立。
- 推断可通过消息传递或采样。

## 优化与实现细节
- 目标来源：最大似然或贝叶斯结构学习。
- 求解器：变量消元、信念传播、MCMC。
- 数值要点：大规模图推断复杂度高。

## 关联与边界
- 对比 GMM：图模型更通用，GMM 是特定混合模型。
- 对比 HMM：HMM 是链结构贝叶斯网络。
- 边界：图结构学习困难，推断可 NP-hard。

## 失败模式
- 错误独立假设导致系统偏差。
- 高维图推断不可扩展。

## 最小伪代码
```text
Input: graph structure, local factors
Run belief propagation or sampling
Return marginal/conditional queries
```

## 决策清单
- [ ] 变量依赖可明确建模
- [ ] 推断算法可扩展
- [ ] 结构学习有足够先验或数据

## 个人备注
TODO

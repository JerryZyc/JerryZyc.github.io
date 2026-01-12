---
layout: single
title: "EM 算法 EM Algorithm"
permalink: /learning/machine-learning/probabilistic-ml/em-algorithm/
classes: wide
---

## 一句话定义
EM 通过交替优化隐变量后验与参数，在含隐变量的似然问题中实现坐标上升。

## 问题设定
- 输入：观测数据 $\mathcal{D}$，含隐变量模型 $p(x,z\mid\theta)$。
- 输出：参数 $\theta$。
- 假设：隐变量可引入并改善模型表达。
- 边界：非凸，易陷局部最优。

## 数学表述
E 步：
$$
Q(\theta\mid\theta^{(t)}) = \mathbb{E}_{p(z\mid x,\theta^{(t)})}[\log p(x,z\mid\theta)]
$$
M 步：
$$
\theta^{(t+1)} = \arg\max_{\theta} Q(\theta\mid\theta^{(t)})
$$

## 算法解释
- E 步计算隐变量后验；M 步最大化期望完全数据对数似然。
- 每次迭代提升数据似然下界。

## 优化与实现细节
- 目标来源：MLE with latent variables。
- 求解器：E/M 往往有闭式更新。
- 数值要点：初始化敏感；收敛到局部极值。

## 关联与边界
- 与 GMM：GMM 训练的标准算法。
- 与变分推断：EM 是变分方法的特例。
- 边界：当 E 步不可解析时需近似。

## 失败模式
- 局部最优或退化解（如协方差塌缩）。
- 初始化差导致慢收敛。

## 最小伪代码
```text
Input: data X, model p(x,z|theta)
Initialize theta
Repeat:
  E-step: compute posterior of z
  M-step: maximize expected complete log-likelihood
Return theta
```

## 决策清单
- [ ] 模型包含隐变量且可分解
- [ ] E/M 步可解析或可近似
- [ ] 初始化策略有效

## 个人备注
TODO

---
layout: single
title: "贝叶斯推断 Bayesian Inference"
permalink: /learning/machine-learning/probabilistic-ml/bayesian-inference/
classes: wide
---

## 一句话定义
贝叶斯推断通过后验分布 $p(\theta\mid\mathcal{D})$ 量化参数不确定性，并用于预测。

## 问题设定
- 输入：数据 $\mathcal{D}$、先验 $p(\theta)$。
- 输出：后验 $p(\theta\mid\mathcal{D})$ 与预测分布。
- 假设：模型与先验可表达数据生成过程。
- 边界：复杂模型后验不可解析需近似。

## 数学表述
贝叶斯公式：
$$
p(\theta\mid\mathcal{D}) = \frac{p(\mathcal{D}\mid\theta) p(\theta)}{p(\mathcal{D})}
$$
预测分布：
$$
p(y\mid x, \mathcal{D}) = \int p(y\mid x,\theta) p(\theta\mid\mathcal{D}) \, d\theta
$$

## 算法解释
- 后验整合先验与数据。
- 预测通过后验平均降低过拟合。

## 优化与实现细节
- 目标来源：后验推断。
- 求解器：共轭解析解、MCMC、变分推断。
- 数值要点：后验近似质量影响预测。

## 关联与边界
- 对比 MAP：贝叶斯给出分布而非点估计。
- 对比频率学派：频率学派以参数固定、样本随机为假设。
- 边界：先验敏感，小样本时影响更大。

## 失败模式
- 先验不合理导致后验偏差。
- 近似推断质量不足。
- 计算成本过高。

## 最小伪代码
```text
Input: D, prior p(theta)
Compute posterior p(theta|D)
Predict by integrating over theta
```

## 决策清单
- [ ] 需要不确定性量化
- [ ] 先验可解释且可辩护
- [ ] 近似推断误差可接受

## 个人备注
TODO

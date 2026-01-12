---
layout: single
title: "MLE 与 MAP"
permalink: /learning/machine-learning/probabilistic-ml/mle-map/
classes: wide
---

## 一句话定义
MLE 最大化似然，MAP 最大化后验，后者等价于在 MLE 目标上加入先验正则。

## 问题设定
- 输入：观测数据 $\mathcal{D} = \{x_i\}_{i=1}^n$ 或 $\{(x_i,y_i)\}$。
- 输出：参数 $\theta$。
- 假设：数据由模型 $p(x\mid\theta)$ 或 $p(y\mid x,\theta)$ 生成。
- 边界：模型错设时两者都可能偏差。

## 数学表述
MLE：
$$
\hat{\theta}_{\text{MLE}} = \arg\max_{\theta} \; p(\mathcal{D} \mid \theta)
$$

MAP：
$$
\hat{\theta}_{\text{MAP}} = \arg\max_{\theta} \; p(\mathcal{D} \mid \theta) p(\theta)
$$

等价的最小化形式：
$$
\hat{\theta}_{\text{MAP}} = \arg\min_{\theta} \; -\log p(\mathcal{D} \mid \theta) - \log p(\theta)
$$

## 算法解释
- MLE 仅依赖数据。
- MAP 将先验作为正则约束，缓解小样本过拟合。

## 优化与实现细节
- 目标来源：概率模型的似然与先验。
- 求解器：与模型相同（闭式/梯度/EM）。
- 数值要点：先验选取影响偏差与方差。

## 关联与边界
- MAP 与正则化：高斯先验对应 $\ell_2$，拉普拉斯先验对应 $\ell_1$。
- 与贝叶斯推断：MAP 是后验点估计，不给出不确定性。
- 边界：先验错误时会系统性偏移。

## 失败模式
- 过强先验导致欠拟合。
- 似然模型错设导致估计偏差。

## 最小伪代码
```text
Input: data D, likelihood p(D|theta), prior p(theta)
Optimize log p(D|theta) [+ log p(theta)]
Return theta
```

## 决策清单
- [ ] 先验是否有依据
- [ ] 样本量是否足够支持 MLE
- [ ] 是否需要不确定性（如需要应做完整贝叶斯）

## 个人备注
TODO

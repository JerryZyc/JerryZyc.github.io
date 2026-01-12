---
layout: single
title: "什么是机器学习 What Is ML"
permalink: /learning/machine-learning/fundamentals/what-is-ml/
classes: wide
---

## 一句话定义
机器学习是在给定数据与假设空间下，通过优化目标函数学习可泛化的参数或规则的过程。

## 问题设定
- 输入：数据集 $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^n$ 或仅 $\{x_i\}_{i=1}^n$。
- 输出：模型参数 $\theta$ 或决策函数 $f_\theta$。
- 假设：样本来自未知分布 $P(x,y)$ 或 $P(x)$；训练与测试分布一致或可校正。
- 边界：不处理无数据可学或目标不可识别的任务。

## 数学表述
监督学习常用经验风险最小化（ERM）：
$$
\min_{\theta} \; \frac{1}{n} \sum_{i=1}^n \ell(f_\theta(x_i), y_i) + \lambda \Omega(\theta)
$$
其中 $\ell$ 为损失函数，$\Omega$ 为正则项。

## 算法解释
- 通过优化目标函数选择参数，使训练误差与模型复杂度取得平衡。
- 学习结果依赖于假设空间、损失函数与优化器。

## 优化与实现细节
- 目标来源：ERM 或 MLE/MAP。
- 求解器：梯度法、二阶法或闭式解（若存在）。
- 复杂度：与样本数 $n$、特征维度 $d$、模型结构相关。
- 数值要点：特征缩放、正则化与稳定的损失实现。

## 关联与边界
- 对比统计建模：ML 更关注预测与泛化。
- 对比优化：ML 目标函数含统计假设与泛化要求。
- 边界：若训练分布与部署分布漂移严重，泛化失效。

## 失败模式
- 训练/测试分布不一致（distribution shift）。
- 过拟合或欠拟合。
- 数据噪声或标注错误导致偏差。

## 最小伪代码
```text
Input: dataset D, model f_theta, loss l
Initialize theta
Repeat:
  Compute gradients of loss
  Update theta
Return theta
```

## 决策清单
- [ ] 数据分布与部署分布一致或可校正
- [ ] 目标函数与业务指标一致
- [ ] 过拟合风险可控

## 个人备注
TODO

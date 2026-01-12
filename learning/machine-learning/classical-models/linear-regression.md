---
layout: single
title: "线性回归 Linear Regression"
permalink: /learning/machine-learning/classical-models/linear-regression/
classes: wide
---

## 一句话定义
线性回归通过最小化平方误差来估计线性映射 $y \approx x^\top w + b$，在 i.i.d. 高斯噪声假设下等价于 MLE。

## 问题设定
- 输入：特征向量 $x \in \mathbb{R}^d$，数据集 $\{(x_i, y_i)\}_{i=1}^n$。
- 输出：参数 $w \in \mathbb{R}^d$，偏置 $b \in \mathbb{R}$。
- 假设：参数线性；误差 $\epsilon_i$ i.i.d. 且零均值；MLE 推导中假设 $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$。
- 边界：连续目标的监督回归；无链接函数时不适用于离散分类。

## 数学表述
定义模型 $\hat{y}_i = x_i^\top w + b$，残差 $r_i = y_i - \hat{y}_i$。

**来自经验风险最小化（最小二乘）：**
$$
\min_{w,b} \; \frac{1}{2n} \sum_{i=1}^n (y_i - x_i^\top w - b)^2
$$

**来自 MLE（高斯噪声）：**
假设 $y_i = x_i^\top w + b + \epsilon_i$，$\epsilon_i \sim \mathcal{N}(0, \sigma^2)$。负对数似然与平方损失成正比，得到相同目标。

闭式解（当 $X^\top X$ 可逆，且 $y$ 已中心化或偏置已吸收）：
$$
\hat{w} = (X^\top X)^{-1} X^\top y
$$

## 算法解释
- 解一个凸二次目标。
- 等价于将 $y$ 投影到 $X$ 的列空间。
- 在 Gauss-Markov 假设下得到 BLUE。

## 优化与实现细节
- 目标来源：高斯噪声下的 MLE 或最小二乘 ERM。
- 求解器：正规方程（小 $d$），QR/SVD（数值稳定），或梯度法（大规模）。
- 复杂度：正规方程 $O(nd^2 + d^3)$；QR $O(nd^2)$；SGD 每轮 $O(nd)$。
- 数值要点：避免显式求逆；当 $X^\top X$ 条件数差时使用 QR/SVD 或 ridge 正则化。

## 关联与边界
- 对比 ridge：加入 $\lambda \|w\|_2^2$ 处理多重共线性并改善条件数。
- 对比 lasso：使用 $\ell_1$ 惩罚获得稀疏解，解的结构改变。
- 对比 logistic：二分类目标下更换似然与损失。
- 边界：参数线性；输入非线性关系需特征映射或非线性模型。

## 失败模式
- 多重共线性导致 $w$ 不稳定。
- 异常点主导平方损失。
- 异方差或非高斯噪声破坏 MLE 等价性。
- 训练域外外推不可靠。

## 最小伪代码
```text
Input: X in R^{n x d}, y in R^{n}
Add bias column if needed
Compute w = solve((X^T X), X^T y) using QR/SVD
Return w
```

## 决策清单
- [ ] 目标是连续值且线性假设可接受
- [ ] 已检查特征缩放与多重共线性
- [ ] 已处理异常点或评估鲁棒替代
- [ ] 已与 ridge/lasso 基线对比

## 个人备注
TODO

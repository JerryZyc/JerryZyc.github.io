---
layout: single
title: "凸性 Convexity"
permalink: /learning/machine-learning/optimization/convexity/
classes: wide
---

## 一句话定义
凸性保证任何局部最优即全局最优，并使一阶方法具有可证明的收敛性质。

## 问题设定
- 输入：目标函数 $f(\theta)$ 与可行域 $\mathcal{C}$。
- 输出：凸性判定与优化性质。
- 假设：$f$ 二阶可微或次可微。
- 边界：非凸问题无法保证全局最优。

## 数学表述
凸性定义：
$$
\forall \theta_1,\theta_2,\; \forall \lambda\in[0,1],\; f(\lambda\theta_1+(1-\lambda)\theta_2) \le \lambda f(\theta_1)+(1-\lambda)f(\theta_2)
$$
若 $\nabla^2 f(\theta) \succeq 0$，则 $f$ 凸。

## 算法解释
凸问题允许用一阶或二阶方法可靠求解，超参数调优更稳定。

## 优化与实现细节
- 判别：Hessian 半正定或凸性闭包（和、仿射变换、最大值）。
- 数值要点：凸性不等于易解，大规模仍需高效算法。

## 关联与边界
- 对比非凸：非凸可能有多个局部极小与鞍点。
- 对比强凸：强凸提供更快收敛率。
- 边界：深度学习多数目标非凸。

## 失败模式
- 误判凸性导致错误收敛保证。
- 过度依赖凸性忽视数值条件数问题。

## 最小伪代码
```text
Input: f
Check convexity by Hessian PSD or known structure
Choose solver accordingly
```

## 决策清单
- [ ] 凸性判定依据明确
- [ ] 需要全局最优保证
- [ ] 计算代价可接受

## 个人备注
TODO

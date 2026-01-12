---
layout: single
title: "梯度下降 Gradient Descent"
permalink: /learning/machine-learning/optimization/gradient-descent/
classes: wide
---

## 一句话定义
梯度下降通过沿负梯度方向迭代更新参数，以最小化可微目标函数。

## 问题设定
- 输入：可微目标函数 $f(\theta)$，初始参数 $\theta_0$。
- 输出：近似最优解 $\theta^*$。
- 假设：$f$ 连续可微，梯度可计算或可估计。
- 边界：非凸问题只能保证到达局部极小或鞍点。

## 数学表述
基本更新：
$$
\theta_{t+1} = \theta_t - \eta_t \nabla f(\theta_t)
$$
其中 $\eta_t$ 为步长。

## 算法解释
梯度提供最快下降方向；步长控制收敛速度与稳定性。不同变体（SGD、动量、Adam）在噪声与曲率下表现不同。

## 优化与实现细节
- 目标来源：一阶最优化。
- 步长选择：常数步长、衰减步长或自适应步长。
- 数值要点：特征缩放改善条件数；梯度裁剪防止爆炸。

## 关联与边界
- 对比牛顿法：牛顿法利用二阶信息，收敛更快但成本更高。
- 对比坐标下降：坐标下降适合稀疏或可分结构。
- 边界：当 $f$ 非光滑或梯度噪声大时需替代方法。

## 失败模式
- 步长过大导致发散。
- 步长过小导致收敛过慢。
- 鞍点附近梯度过小导致停滞。

## 最小伪代码
```text
Input: f, grad f, theta0, step size eta
Repeat:
  theta = theta - eta * grad f(theta)
Until convergence
Return theta
```

## 决策清单
- [ ] 梯度可计算或可估计
- [ ] 步长策略已验证
- [ ] 目标函数条件数可接受

## 个人备注
TODO

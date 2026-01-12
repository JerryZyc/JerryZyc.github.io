---
layout: single
title: "泛化 Generalization"
permalink: /learning/deep-learning/training/generalization/
classes: wide
---

## 一句话定义
泛化是模型在未见数据上的性能，与模型容量、数据分布和正则化共同决定。

## 问题设定
- 输入：训练误差与验证误差。
- 输出：泛化误差估计。
- 假设：训练/验证分布一致。
- 边界：分布漂移导致泛化失效。

## 数学表述
泛化间隙：
$$
\Delta = R_{test}(f) - R_{train}(f)
$$

## 算法解释
- 过拟合意味着 $\Delta$ 大。
- 通过正则化与数据增强降低 $\Delta$。

## 优化与实现细节
- 数值要点：交叉验证与早停。

## 关联与边界
- 与偏差-方差分解相关。
- 边界：OOD 场景需域适应或不确定性估计。

## 失败模式
- 训练过度导致泛化下降。
- 过度调参导致验证集过拟合。

## 最小伪代码
```text
Train model
Track train/val gap
Apply regularization if needed
```

## 决策清单
- [ ] 训练/验证分布一致
- [ ] 过拟合已检测
- [ ] 正则化与数据增强有效

## 个人备注
TODO

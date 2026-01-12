---
layout: single
title: "泛化 Generalization"
permalink: /learning/cross-cutting-concepts/generalization/
classes: wide
---

## 一句话定义
泛化描述模型在未见数据上的性能表现及其与训练误差的差距。

## 问题设定
- 输入：训练/测试误差。
- 输出：泛化误差与间隙。
- 假设：训练与测试分布一致。
- 边界：分布漂移时泛化失效。

## 数学表述
泛化间隙：
$$
\Delta = R_{test}(f) - R_{train}(f)
$$

## 算法解释
- 通过正则化、数据增强和模型选择控制 $\Delta$。

## 优化与实现细节
- 数值要点：交叉验证与早停。

## 关联与边界
- 与偏差-方差、正则化紧密相关。
- 边界：OOD 需域适应或不确定性估计。

## 失败模式
- 过拟合导致 $\Delta$ 增大。
- 验证集过拟合。

## 最小伪代码
```text
Train model
Compute train/test gap
Apply regularization if needed
```

## 决策清单
- [ ] 分布一致性评估
- [ ] 过拟合监控
- [ ] 选择合适正则化

## 个人备注
TODO

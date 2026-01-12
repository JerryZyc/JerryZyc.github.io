---
layout: single
title: "信息论 Information Theory"
permalink: /learning/cross-cutting-concepts/information-theory/
classes: wide
---

## 一句话定义
信息论量化不确定性与信息量，是编码、表示学习与对比学习的重要工具。

## 问题设定
- 输入：随机变量分布 $P(X)$。
- 输出：熵、互信息等度量。
- 假设：分布可定义。
- 边界：互信息估计在高维困难。

## 数学表述
熵：
$$
H(X)=-\sum_x p(x)\log p(x)
$$
互信息：
$$
I(X;Y)=\sum_{x,y} p(x,y) \log \frac{p(x,y)}{p(x)p(y)}
$$

## 算法解释
- 熵衡量不确定性。
- 互信息衡量变量依赖。

## 优化与实现细节
- 数值要点：对比学习常通过下界估计互信息。

## 关联与边界
- 与表示学习、对比学习密切相关。
- 边界：估计偏差大。

## 失败模式
- 估计方法不稳定。
- 样本不足导致偏差。

## 最小伪代码
```text
Estimate distribution
Compute entropy or MI
```

## 决策清单
- [ ] 估计方法可行
- [ ] 样本量足够
- [ ] 数值稳定

## 个人备注
TODO

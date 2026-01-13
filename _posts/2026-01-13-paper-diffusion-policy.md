---
title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
date: 2026-01-13
categories: [paper]
tags: [diffusion, imitation-learning, manipulation, visuomotor, transformer, receding-horizon]
paper:
  venue: "arXiv"
  year: "2024"
  authors: "Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song"
  pdf: "/assets/papers/diffusion-policy.pdf"
status: reading
---

## Title + 摘要
本文提出 Diffusion Policy，将机器人 visuomotor policy 表示为**条件去噪扩散过程**，在动作空间中迭代采样生成动作序列。作者在 4 个基准、15 个任务上评估，平均提升 46.9%，并展示在真实机器人上的多任务操作能力。核心优势包括：对多模态动作分布的表达、适配高维动作序列、训练更稳定。为让扩散模型适用于实时控制，文中引入**receding horizon**、**视觉条件化**以及**时间序列扩散 Transformer**等关键设计。

## 1. Problem Setting（任务/场景/假设）
将模仿学习视作学习条件分布 $p(a|o)$。传统回归式策略在多模态行为、长时序相关以及精确控制方面表现不稳。本文目标是在视觉观测条件下，生成**高维动作序列**，并保持多模态表达与稳定训练。

## 2. Motivation & Key Challenges
- 多模态行为：同一观测下存在多种合理动作。
- 高维动作序列：单步动作无法表达稳定的时序行为。
- 训练稳定性：能量模型或隐式策略往往需要负采样，训练不稳。

## 3. Method Overview（系统框图 + 文字解释）
扩散策略在动作序列空间中进行 K 步去噪，并通过视觉观测条件化。

```
Observation window O_t (last T_o steps)
        |
        +--> Visual encoder -> Obs Emb
                         |
Action noise A_t^K ------+--> Diffusion Net (CNN+FiLM or Transformer)
                         |
                      A_t^0 (denoised action sequence)
        |
Execute first T_a actions, then receding horizon replan
```

## 4. Core Components（逐模块，带公式/伪代码/维度）

### 4.1 DDPM 去噪生成（动作序列）
从高斯噪声开始，迭代去噪得到动作序列：

$$
x_{k-1} = \alpha_k \left(x_k - \lambda_k \, \epsilon_\theta(x_k, k) + \mathcal{N}(0, \sigma_k^2 I)\right)
$$

可视为带噪的梯度下降：

$$
x' = x - \lambda \nabla E(x)
$$

其中 $\epsilon_\theta$ 近似梯度场。

### 4.2 DDPM 训练目标
随机选 $k$ 并对 $x_0$ 加噪：

$$
\mathcal{L} = \mathrm{MSE}\left(\epsilon_k, \epsilon_\theta(x_0 + \epsilon_k, k)\right)
$$

该目标等价于最小化 DDPM 生成分布与数据分布的 KL 上界。

### 4.3 视觉条件化扩散（策略建模）
策略学习条件分布 $p(A_t | O_t)$，修改去噪公式：

$$
A_{t,k-1} = \alpha_k \left(A_{t,k} - \lambda_k \, \epsilon_\theta(O_t, A_{t,k}, k) + \mathcal{N}(0, \sigma_k^2 I)\right)
$$

训练损失对应变为：

$$
\mathcal{L} = \mathrm{MSE}\left(\epsilon_k, \epsilon_\theta(O_t, A_{t,0} + \epsilon_k, k)\right)
$$

### 4.4 Receding Horizon 控制
在时间步 $t$，模型输入最近 $T_o$ 步观测，预测 $T_p$ 步动作，只执行前 $T_a$ 步：

- $T_o$：观测窗口长度  
- $T_p$：动作预测长度  
- $T_a$：执行长度（每执行 $T_a$ 重新规划）

这样既能维持时序一致性，又能保持对新观测的响应。

### 4.5 网络结构选项
**CNN + FiLM**：观测特征对每层卷积做通道级调制。  
**Transformer**：将观测嵌入输入交叉注意力层，动作 token 使用因果注意力以保持序列因果性。

## 5. Experiments & Results（结果表格、消融、失败案例）
**总体表现**：在 4 个基准 15 个任务上平均提升 46.9%，包括模拟与真实场景、2DoF 至 6DoF、刚体与流体任务。  
**真实机器人**：在 Push-T 与多种双臂任务中展示稳健性能。  
**消融结论（文字版）**：
- 较大的动作预测长度有助于平滑与多模态行为表达。
- 视觉条件化显著提升推理速度，并使端到端训练更可行。
- 训练稳定性优于隐式能量模型，减少负采样带来的不稳定。

## 6. Discussion（优势/局限）
**优势**
- 多模态动作分布建模自然，避免回归平均化。
- 直接预测动作序列，保持时间一致性。
- 训练稳定，超参数敏感度低。

**局限**
- 推理仍需多步去噪，实时性受步数 K 影响。
- 需要较大演示数据量以覆盖复杂动作分布。

## 7. My Takeaways（个人总结）
1) 用扩散模型来建模动作序列，比单步回归更适合高维连续控制。  
2) 视觉条件化是关键工程点，能把扩散推理开销控制在可用范围。  
3) Receding horizon 让“长规划+短反馈”兼得，是部署到真实机器人的重要桥梁。  

## References
- [1] Cheng Chi et al. *Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*. arXiv:2303.04137v5, 2024.

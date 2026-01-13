---
title: "World Model-based Perception for Visual Legged Locomotion"
date: 2026-01-13
categories: [paper]
tags: [locomotion, world-model, mbrl, rssm, vision, sim2real]
paper:
  venue: "arXiv"
  year: "2024"
  authors: "Hang Lai, Jiahang Cao, Jiafeng Xu, Hongtao Wu, Yunfeng Lin, Tao Kong, Yong Yu, Weinan Zhang"
  pdf: "/assets/papers/wmp-locomotion.pdf"
status: reading
---

## Title + 摘要
本文提出 World Model-based Perception (WMP)，通过世界模型把高维视觉观测压缩为可用于控制的低维隐变量，从而避免“特权信息教师-学生”框架的性能上限和信息鸿沟。方法使用 RSSM 在仿真中学习可预测未来感知的隐状态，并把该隐状态输入到视觉 locomotion 策略中。作者强调世界模型即使只用仿真训练，也能在真实机器人上预测合理的轨迹感知，帮助策略做决策。实验覆盖 Slope、Stair、Gap、Climb、Crawl、Tilt 等地形，WMP 在仿真中接近 Teacher 的回报，在真机 A1 上可通过更困难的间隙与障碍（如 Gap 85cm、Climb 55cm、Crawl 22cm），整体表现优于学生策略与其它基线。

## 1. Problem Setting（任务/场景/假设）
将视觉四足移动建模为 POMDP：

$$
\pi^* = \arg\max_\pi \mathbb{E}\left[\sum_{t=0}^\infty \gamma^t r(s_t, a_t)\right]
$$

观测由本体感觉与深度图构成，特权信息只在仿真可得：

$$
o_t := (o_t^{prop}, d_t)
$$

$$
s_t := (o_t, s_t^{pri})
$$

目标是在视觉部分可用、特权信息不可用的现实环境中，学习可迁移的控制策略。

## 2. Motivation & Key Challenges
- 直接从像素端到端强化学习数据效率低，且前向相机需要记忆历史观测来感知脚下地形。
- 特权学习的 teacher/student 有不可避免的性能差距，且特权信息设计难以泛化到复杂地形（例如 gap 边界、低矮遮挡）。
- 动物直觉上会建立“世界模型”进行预测，暗示用模型压缩历史观测可能更自然、更高效。

## 3. Method Overview（系统框图 + 文字解释）
WMP 采用“世界模型 + 策略”的单阶段学习。世界模型低频更新隐状态，策略高频输出动作。

```
Depth Image d_t + Proprio o_t^prop
        |        |
        |        +--> Encoder q_phi -> z_t (posterior)
        |                              |
        +--> RSSM f_phi --------------> h_t (deterministic)
                        |              |
                        +--> Prior p_phi(z_t | h_t)
                        +--> Decoder p_phi(o_t | h_t, z_t)

Policy: a_{t+i} ~ pi_theta(o_{t+i}^prop, stopgrad(h_t)), i in [0, k-1]
Critic: V_psi(o_{t+i}, stopgrad(h_t), s_{t+i}^pri)
```

关键点：世界模型每 k 个控制步更新一次，节省感知与计算开销，并让隐状态承担“记忆/预测”功能。

## 4. Core Components（逐模块，带公式/伪代码/维度）

### 4.1 RSSM 世界模型（结构与变量）
RSSM 由四部分组成：

$$
h_t = f_\phi(h_{t-k}, z_{t-k}, a_{t-k:t-1})
$$

$$
z_t \sim q_\phi(\cdot | h_t, o_t), \quad \hat{z}_t \sim p_\phi(\cdot | h_t)
$$

$$
\hat{o}_t \sim p_\phi(\cdot | h_t, z_t)
$$

- $h_t$：确定性隐状态（GRU 更新）
- $z_t$：随机隐状态（posterior）
- $\hat{z}_t$：先验预测（prior）
- $\hat{o}_t$：重建观测

### 4.2 RSSM 训练目标（重建 + KL）
对长度为 $L$ 的序列最小化：

$$
\mathcal{L}(\phi) = \mathbb{E}\left[\sum_{t=nk}^{nk+L} -\ln p_\phi(o_t | z_t, h_t) + \beta \, \mathrm{KL}\left(q_\phi(\cdot|h_t,o_t) \,\|\, p_\phi(\cdot|h_t)\right)\right]
$$

含义：
- 重建项确保 $z_t$ 包含足够观测信息；
- KL 项对齐 posterior 与 prior，使模型可在缺失观测时进行开环预测。

### 4.3 策略学习（利用隐状态）
策略在每个世界模型周期内复用同一 $h_t$：

$$
a_{t+i} \sim \pi_\theta(\cdot | o^{prop}_{t+i}, \mathrm{sg}(h_t)), \quad i \in [0, k-1]
$$

critic 允许访问特权信息以稳定训练（非对称 actor-critic）：

$$
v(s_{t+i}) = V_\psi(o_{t+i}, \mathrm{sg}(h_t), s^{pri}_{t+i})
$$

### 4.4 关节控制（PD）
动作 $a_t$ 输出关节目标位置偏移，PD 控制为：

$$
\tau = K_p(q_d - q) + K_d(\dot{q}_d - \dot{q})
$$

其中 $q_d = q^{stand} + a_t$，$\dot{q}_d = 0$。

### 4.5 奖励设计（追踪 + 风格）
速度追踪奖励（简化的方向追踪）：

$$
r_{tracking} = \exp\left(\min(v_{xy}^{cmd}, v_{xy}^{cmd} + 0.1) - v_{xy}^2 / \sigma\right)
$$

风格奖励采用 AMP：

$$
r_{style}(s, s') = \max\left[0, 1 - 0.25(D_\psi(s, s') - 1)^2\right]
$$

判别器训练目标：

$$
\min_\psi \; \mathbb{E}_{(s,s')\sim D_{ref}}(D_\psi-1)^2 + \mathbb{E}_{(s,s')\sim \pi_\theta}(D_\psi+1)^2 + \frac{w_{gp}}{2}\mathbb{E}_{D_{ref}}\|\nabla_\psi D_\psi\|^2
$$

## 5. Experiments & Results（结果表格、消融、失败案例）
**仿真结果**：在 Slope、Stair、Gap、Climb、Tilt、Crawl 等地形上，WMP 的回报接近 Teacher，显著优于 Student 与 Blind。尤其在 Gap/Climb/Crawl 等需要提前感知的地形，Student 和 Blind 出现明显退化，WMP 仍保持稳定。

**真机结果**（Unitree A1）：
- Gap 85cm（约 2.1x 机身长度）
- Climb 55cm（约 2.2x 机身高度）
- Crawl 22cm（约 0.8x 机身高度）

整体表明模型学到的隐状态可跨 sim-to-real，为控制提供有效的先验信息。

## 6. Ablations & Sensitivity
- **世界模型更新间隔 $k$**：$k$ 越小仿真回报越高，但计算与感知成本更高；作者选择 $k=5$ 作为准确性与实时性的折中。
- **训练序列长度 $L$**：约 1s 的历史就能达到较好效果，最终使用 6.4s 训练长度以覆盖长程依赖。
- **去除 depth 或 proprio**：去除 depth 的 world model 相当于 blind 策略，性能显著下降，说明视觉建模是关键。

## 7. 真实世界预测分析
世界模型在真实数据上仍能预测合理的未来深度图像，尤其在关键障碍前表现良好，暗示 latent-space 的预测具有一定 sim-to-real 泛化能力。

## 8. Discussion（优势/局限）
**优势**
- 单阶段训练，避免 teacher/student 信息鸿沟。
- 世界模型提供低维、可预测的隐状态，有效解决部分可观测问题。
- sim-to-real 迁移效果强，适用于复杂地形。

**局限**
- 世界模型仍完全依赖仿真数据，现实差异可能导致预测偏差。
- 模型频率与计算开销仍是部署瓶颈（需权衡 k）。
- 没有使用模型进行 imagination rollout，训练效率可能仍受限于仿真采样。

## 9. My Takeaways（个人总结）
1) 视觉 locomotion 的关键不是更强的 CNN，而是“能预测的隐状态”来做时间对齐与先验推断。  
2) RSSM 的 KL 约束是保证开环预测能力的核心，实质上在逼近“短期世界模型”。  
3) 相比特权学习，WMP 把“记忆+预测”显式化，更贴近动物认知机制。  
4) 若要进一步提升，混合真实数据训练世界模型或引入基于模型的 imagination 可能是下一个方向。  

## References
- [1] Hang Lai et al. *World Model-based Perception for Visual Legged Locomotion*. arXiv:2409.16784v1, 2024.

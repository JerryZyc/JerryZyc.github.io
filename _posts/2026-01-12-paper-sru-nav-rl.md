---
title: "Spatially-Enhanced Recurrent Memory for Long-Range Mapless Navigation"
date: 2026-01-12
categories: [paper]
tags: [navigation, reinforcement-learning, rnn, attention, sim2real]
paper:
  venue: "arXiv"
  year: "2025"
  authors: "Fan Yang, Per Frivik, David Hoeller, Chen Wang, Cesar Cadena, Marco Hutter"
  pdf: "/assets/papers/sru-nav-rl.pdf"
status: reading
---

## Title + 摘要
本文研究长程无地图导航的核心难题：在仅有前向深度观测的条件下，如何在动态视角变化中形成稳定的空间记忆，从而实现规划与避障。作者指出传统 RNN（LSTM/GRU）擅长时间记忆却不擅长空间配准，导致对历史观测的空间对齐能力不足，难以形成长期空间表征。为此提出 Spatially-Enhanced Recurrent Unit (SRU)，在标准门控循环单元中引入空间变换项，使其隐式学习视角变化下的空间对齐。基于 SRU，作者构建双层空间注意力 + SRU 的端到端 RL 架构，并结合深度编码器预训练、深度噪声模型、DML 与时序一致 Dropout 等训练策略，实现更稳定的长程导航训练。实验表明 SRU 在多种环境下成功率显著提升（整体约 +23.5%，对 EMHP 与堆叠历史观测基线提升约 29.6% 与 105.0%），并在真实场景中实现零样本 sim-to-real 部署。本文对“隐式记忆能否替代显式建图”的问题给出强有力的工程化答案。

## 1. Problem Setting（任务/场景/假设）
任务是长程、无地图导航。机器人仅能获取自身视角的深度图与少量本体信息，在未知环境中到达目标。形式化为 POMDP：

$$
(S, A, T, R, O, Z, \gamma)
$$

其中：
- $S$ 为状态集合，$A$ 为动作空间
- $T$ 为状态转移，$R$ 为奖励
- $O$ 为观测集合，$Z$ 为观测模型
- $\gamma$ 为折扣因子

由于观测是自我坐标系的局部深度图，单帧无法充分反映全局环境，必须依靠序列记忆形成可规划的隐式地图。

## 2. Motivation & Key Challenges（为什么难）
- 纯端到端 RNN 虽能捕捉时间依赖，但难以进行空间配准，无法把不同视角下的观测对齐成一致空间表征。
- 传统显式建图带来系统延迟与额外复杂度，不适合高速或复杂动力学平台。
- 长程稀疏奖励会导致“晚出发”策略或过拟合局部策略，需要额外正则化。

## 3. Method Overview（系统框图 + 文字解释）
架构采用“感知编码 + 双层注意力 + SRU 记忆 + MLP 动作头”。

```
Depth Image --> Encoder (RegNet+FPN) --> Self-Attn --> Cross-Attn --> SRU --> MLP --> Action
                                  ^                       |
                                  |                       +-- Proprioceptive state + Goal
```

核心思想：注意力机制压缩并选择关键空间特征，SRU 负责长期隐式地图记忆与空间对齐，MLP 输出线速度与角速度控制指令。

## 4. Core Components（逐模块，带公式/伪代码/维度）

### 4.1 Perception / Encoder（输入输出维度）
输入为前向深度图 $I_t$，经过 RegNet + FPN 得到特征图：

$$
F_t \in \mathbb{R}^{C \times H \times W}
$$

其中 $C$ 为通道数，$H,W$ 为空间尺寸。随后经自注意力与交叉注意力压缩为：

$$
\hat{F}_t \in \mathbb{R}^{C \times 1}
$$

**变量表**

<table>
  <thead>
    <tr>
      <th>符号</th>
      <th>含义</th>
      <th>维度</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$I_t$</td>
      <td>深度图观测</td>
      <td>$H_0 \times W_0$</td>
    </tr>
    <tr>
      <td>$F_t$</td>
      <td>编码特征图</td>
      <td>$C \times H \times W$</td>
    </tr>
    <tr>
      <td>$\hat{F}_t$</td>
      <td>压缩特征</td>
      <td>$C \times 1$</td>
    </tr>
  </tbody>
</table>

### 4.2 Spatial Attention（Self-Attn + Cross-Attn）
先对视觉特征做空间自注意力，再用机器人状态作为 Query 做交叉注意力压缩：

$$
\text{Attn}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d}}\right)V
$$

- **Self-Attn**：$Q=K=V$ 来自 $F_t$ 的空间 token，增强全局空间关系。
- **Cross-Attn**：$Q$ 来自本体状态 $o^{prop}_t$ 与目标位置 $p_t$，$K,V$ 来自视觉 token，用于“状态引导”的视觉压缩。

**变量表**

<table>
  <thead>
    <tr>
      <th>符号</th>
      <th>含义</th>
      <th>维度</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$Q,K,V$</td>
      <td>注意力输入</td>
      <td>$d \times n$</td>
    </tr>
    <tr>
      <td>$o^{prop}_t$</td>
      <td>本体状态</td>
      <td>$d_{prop}$</td>
    </tr>
    <tr>
      <td>$p_t$</td>
      <td>相对目标</td>
      <td>$d_{goal}$</td>
    </tr>
  </tbody>
</table>

### 4.3 Memory (SRU)（对比 LSTM/GRU 的关键改动）
SRU 在传统门控结构中引入空间变换项 $s_t$，用于隐式对齐观测视角：

$$
s_t = W_{xs} x_t + b_s
$$

SRU-LSTM 的核心更新为：

$$
g_t = \tanh\left(s_t \odot W_{xg} x_t + W_{hg} h_{t-1} + b_g\right)
$$

SRU-GRU 的候选状态为：

$$
\tilde{h}_t = \tanh\left(s_t \odot W_{xh} x_t + W_{hh}(r_t \odot h_{t-1}) + b_h\right)
$$

SRU-Ours 在此基础上增加门控修正以缓解饱和：

$$
r_t = i_t \odot \left(1 - (1 - f_t)^2\right) + (1 - i_t) \odot f_t^2
$$

$$
c_t = r_t \odot c_{t-1} + (1 - r_t) \odot g_t
$$

**直觉**：$s_t$ 作为“视角变换因子”，让隐状态更新时显式考虑空间对齐，减少“把不同视角直接叠加”的误差。

### 4.4 RL Training Design（奖励、dropout、DML、非对称 actor-critic）
总体奖励：

$$
r_t = \alpha_1 r_t^{task} - \alpha_2 r_t^{reg} - \alpha_3 r_t^{pen}
$$

其中任务奖励采用稀疏时间窗 + 随机检查机制：

$$
r_t^{task} = \frac{\mathbf{1}(t > T_{max}-T_r \;\lor\; \text{random} < \delta_{check})}{1 + \|p_t\|_\sigma}
$$

动作平滑正则：

$$
a_t^m = \lambda a_{t-1} + (1-\lambda) a_t
$$

$$
r_t^{reg} = \beta_1 \|a_t - a_t^m\| + \beta_2 \|j_t^{acc}\|
$$

惩罚项：

$$
r_t^{pen} = \eta_1 \mathbf{1}(\text{collision}) + \eta_2 \max(0, |\theta_t| - \theta_{safe})
$$

**训练策略**
- **Asymmetric Actor-Critic**：actor 接收噪声深度观测，critic 使用更稳定的状态信息，提升训练稳定性。
- **DML (Deep Mutual Learning)**：双策略互蒸馏，使用 KL 散度作为额外正则，抑制早期陷入次优策略。
- **TC-Dropout**：保持时间维度一致的 dropout mask，稳定序列记忆训练。

## 5. Experiments & Results（结果表格、消融、失败案例）
**结果概览**：SRU 系列在多环境成功率显著提升，尤其在需要长程记忆的场景。

| Model | Maze | Pillar | Stair | Pit | Overall |
| --- | --- | --- | --- | --- | --- |
| GRU | 68.1 | 73.6 | 35.7 | 66.7 | 61.0 |
| LSTM | 70.3 | 78.2 | 33.1 | 72.7 | 63.5 |
| SRU-GRU | 73.1 | 78.8 | 74.1 | 74.8 | 75.2 |
| SRU-LSTM | 75.9 | 76.7 | 79.3 | 74.1 | 76.5 |
| SRU-Ours | 76.0 | 81.0 | 82.8 | 75.6 | 78.9 |

**失败案例（论文描述）**
- LSTM 在迷宫中反复进入死胡同，无法回忆已走过的路径。
- LSTM 在坑洞环境中无法记住视野外的坑洞位置，导致再次掉入。

## 6. Discussion（优势/局限）
**优势**
- SRU 提升空间记忆能力，在长程导航中显著提高成功率。
- 无需显式建图，降低系统延迟与复杂度。
- 结合注意力与 DML/TC-Dropout，训练更稳定。

**局限**
- 仍受循环记忆衰减影响，超长时间跨度记忆可能不足。
- 依赖深度观测与预训练编码器，感知噪声仍会影响性能。

## 7. Reproducibility Checklist（超参数、训练设置、代码结构、硬件）
- 环境：NVIDIA IsaacLab，包含迷宫、随机柱、楼梯、坑洞等场景
- 观测：前向深度传感器（FoV 105° x 78°，10m 量程）
- 控制频率：导航策略 5 Hz，底层控制 50 Hz
- 策略：PPO + Asymmetric Actor-Critic
- 正则化：DML、TC-Dropout
- 预训练：RegNet+FPN 深度编码器，TartanAir 合成深度 + 噪声模型

## 8. My Takeaways（个人总结）
1) 在“隐式建图”问题上，单纯换 RNN 结构难以解决空间对齐问题，但引入显式空间变换项能显著改善。
2) 注意力机制不仅压缩信息量，更重要的是让状态驱动视觉选择，提升记忆效率。
3) DML 与 TC-Dropout 对序列学习非常关键，避免记忆学习早期崩坏。
4) 若我做长程导航/探索任务，可优先尝试“注意力 + SRU + 稀疏奖励 + DML”组合。

## References
- [1] Fan Yang et al. *Spatially-Enhanced Recurrent Memory for Long-Range Mapless Navigation via End-to-End Reinforcement Learning*. arXiv:2506.05997v2, 2025.

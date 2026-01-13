---
title: "Flying on Point Clouds with Reinforcement Learning"
date: 2026-01-13
categories: [paper]
tags: [drone, lidar, point-cloud, reinforcement-learning, sim2real]
paper:
  venue: "arXiv"
  year: "2025"
  authors: "Guangtong Xu, Tianyue Wu, Zihan Wang, Qianhao Wang, Fei Gao"
  pdf: "/assets/papers/flying-point-clouds-rl.pdf"
status: reading
---

## Title + 摘要
本文研究如何用机载 3D 激光雷达点云与 sim-to-real 强化学习，实现四旋翼在复杂障碍环境中的低时延自主飞行。作者提出一种**任务相关的点云表示**：将历史点云在机体坐标系下按角度分区，用“最近点距离/未知区域距离”作为每个分区的数值输入，既保留细障碍感知，又降低维度以支持 RL 训练。策略以 50Hz 输出推力与角速度指令，结合动力学随机化与轻量级仿真，使仿真训练的策略能在真实无人机上绕过细小障碍并安全穿行。

## 1. Problem Setting（任务/场景/假设）
目标是让四旋翼仅依赖机载激光雷达与本体信息，在障碍环境中飞向目标点。策略学习为 RL：在部分可观测环境下，利用历史点云与状态估计，输出低层控制指令（推力与 bodyrates）。

## 2. Motivation & Key Challenges
- 传统栅格/占据图对细障碍易“被稀释”，难以保留小目标。
- 原始点云维度巨大，直接 RL 学习代价高且 sim-to-real 难。
- 高速飞行要求低时延控制，不宜重依赖规划与跟踪层级。

## 3. Method Overview（系统框图 + 文字解释）
核心是“点云分区表示 + MLP 策略”。点云通过历史帧对齐后分区编码，再与速度、姿态、目标方向等融合，输出推力与角速度。

```
History point clouds (k frames) -> body frame align
      -> angular partitions (n=3200) -> per-bin distance/unknown
      -> MLP encoder -> fusion with v, q, g, last action
      -> MLP policy -> thrust T + bodyrates ω
```

## 4. Core Components（逐模块，带公式/伪代码/维度）

### 4.1 点云分区表示（任务相关压缩）
将历史 k 帧点云对齐到当前时刻机体坐标系，把周围空间按角度划分为 n 个分区（n=3200，角分辨率约 4.5°）。每个分区取**最近点距离**，并截断到 10m。若分区无点，则用未知区域距离 $d_{unknown}$ 构造：

$$
x_i = 20 - d_{unknown}, \quad 0 < d_{unknown} < 10
$$

该表示既区分“已观测/未知”，又保留细障碍信息。

### 4.2 观测与动作
**观测**：点云表示（3200 维） + 速度、姿态、相对目标方向、上一步动作等。  
**动作**：推力 $T$ 与角速度 $\omega = [\omega_x, \omega_y, \omega_z]$，50Hz 直接下发飞控。

### 4.3 奖励函数
奖励由多项组成：

$$
r = r_{forward} + r_{thrust} + r_{smooth} + r_{maxspeed} + r_z + r_{ESDF} + r_{collision} + r_{yaw}
$$

关键项包括：

$$
r_{forward} = \|p_{goal} - p\| - \|p_{goal} - p_{last}\|
$$

$$
r_{thrust} = \|T - g\|
$$

$$
r_{smooth} = \|\omega\| + \|a - a_{last}\|
$$

$$
r_{maxspeed} = -\exp(\max(0,\|v\| - v_{max})) + 1
$$

$$
r_{ESDF} = \lambda (1 - e^{-kd})
$$

$$
r_{yaw} = \frac{x_{body} \cdot v}{\|v\|}
$$

其中 $d$ 为最近障碍距离，$x_{body}$ 为机体 x 轴方向。

### 4.4 网络结构
MLP 编码器将 3200 维外感知输入编码到 128 维隐状态，再与其他向量融合，输出 4 维动作。Actor/Critic 不共享权重。

## 5. Experiments & Results（结果与对比）
仿真评估显示该点云表示相比占据图输入更易于 PPO 从零开始学习，训练回报更稳定。对比 Fast-Planner、EGO-Planner 等系统，在不同速度约束下表现出更高成功率与更“容易”的轨迹。

## 6. Sim-to-Real 实验
真实飞行中可安全穿越箱体、电缆、稀疏树林等环境。作者强调：轻量级仿真 + 动力学随机化 + 雷达分区表示，使得策略能有效迁移到实体平台。

## 7. Discussion（优势/局限）
**优势**
- 点云表示兼顾细障碍感知与低维可学性。
- 低层控制接口（推力/角速度）带来更高频控制能力。
- sim-to-real 成本低，训练效率高。

**局限**
- 远距离小障碍可能被“放大”近似，存在信息损失。
- 依赖稳定的本地状态估计与传感器标定。

## 8. Reproducibility Checklist（复现要点）
- RL：PPO，1024 环境并行采样。
- 动力学随机化：推力/角速度扰动（约 ±10%/±8%），阻力系数大范围扰动。
- 点云分区：n=3200，历史 k 帧融合，10Hz 输入构造。
- 控制频率：50Hz 低层推力与 bodyrates。

## 9. My Takeaways（个人总结）
1) 对点云做“任务相关”的角度分区是关键，避免了通用下采样的盲区。  
2) 让 RL 直接输出低层控制指令，可减少规划/跟踪延迟，适配高速飞行。  
3) sim-to-real 的关键不是更复杂仿真，而是合理输入表示 + 适度随机化。  

## References
- [1] Guangtong Xu et al. *Flying on Point Clouds with Reinforcement Learning*. arXiv:2503.00496, 2025.

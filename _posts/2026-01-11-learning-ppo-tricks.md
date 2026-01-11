---
title: "PPO Tricks for Stable Training"
date: 2026-01-11
categories: [learning]
tags: [rl, ppo, policy, stability]
---

## Key Concepts
- Clip ratio and value loss balance.
- Advantage normalization and reward scaling.
- Early stopping based on KL divergence.

## Common Pitfalls
- Too large learning rate causes policy collapse.
- Value function overfits when minibatches are too small.

## Practical Checklist
- Normalize advantages per batch.
- Track KL and stop epochs if it spikes.
- Use entropy bonus to avoid premature convergence.

## Quick Reference
```python
# Pseudocode for PPO update loop
for epoch in range(k_epochs):
    logp_new = policy(obs, act)
    ratio = exp(logp_new - logp_old)
    loss_clip = -min(ratio * adv, clip(ratio, 1-eps, 1+eps) * adv)
    loss = loss_clip + vf_coef * value_loss - ent_coef * entropy
```

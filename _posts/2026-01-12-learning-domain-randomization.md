---
title: "Domain Randomization for Sim2Real"
date: 2026-01-12
categories: [learning]
tags: [sim2real, domain-randomization, perception]
---

## Key Concepts
- Randomize visual, dynamics, and sensor parameters.
- Use curriculum to expand ranges gradually.

## Common Pitfalls
- Randomization too wide makes policy underfit.
- Mismatch between randomized assets and target robot.

## Practical Checklist
- Start with camera and lighting randomization.
- Add dynamics later (mass, friction, delay).
- Track real-world success rate per setting.

## Math Note
Reward shaping often uses:
$$
r_t = \alpha r_{task} + \beta r_{stability}
$$

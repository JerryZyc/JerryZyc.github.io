---
title: "Project Retrospective: Grasping in Clutter"
date: 2026-01-16
categories: [work]
tags: [project, manipulation, sim2real]
---

## Background
Bin picking in a cluttered scene with partial observability.

## Goals
- Achieve 80 percent success rate on 20 objects.
- End-to-end pipeline with perception and grasping.

## Approach
- Train grasp proposals in simulation.
- Fine-tune on real data with domain randomization.
- Integrate with a motion planner and force feedback.

## Results
- Reached 76 percent in the lab with stable runtime.

## Lessons Learned
- Dataset bias dominated early failures.
- Calibration drift required weekly checks.

## Next Actions
- Expand object set and improve camera poses.

---
layout: single
title: "高斯混合模型 Gaussian Mixture"
permalink: /learning/machine-learning/classical-models/gaussian-mixture/
classes: wide
---

## One-line definition
A Gaussian mixture model represents data as a weighted sum of Gaussians and fits parameters by MLE via EM.

## Problem setting
- Inputs: data points $\{x_i\}_{i=1}^n$, $x_i \in \mathbb{R}^d$.
- Outputs: mixture weights $\pi_k$, means $\mu_k$, covariances $\Sigma_k$.
- Assumptions: data generated from a finite mixture of Gaussians.
- Boundary: assumes Gaussian components; model selection needed for $K$.

## Mathematical formulation
$$
p(x) = \sum_{k=1}^K \pi_k \mathcal{N}(x \mid \mu_k, \Sigma_k)
$$

Log-likelihood:
$$
\max_{\{\pi,\mu,\Sigma\}} \; \sum_{i=1}^n \log \sum_{k=1}^K \pi_k \mathcal{N}(x_i \mid \mu_k, \Sigma_k)
$$

EM updates with responsibilities $r_{ik}$ (E-step) and closed-form M-step.

## Algorithmic interpretation
- Soft clustering with probabilistic assignments.
- EM performs coordinate ascent on the evidence lower bound.

## Optimization & implementation details
- Objective source: MLE for mixture model.
- Solver: EM (non-convex, local optimum).
- Complexity: $O(n K d^2)$ for full covariance; diagonal reduces cost.
- Numerical notes: covariance regularization (add $\epsilon I$), prevent component collapse, good initialization (k-means).

## Connections & boundaries
- Compared to k-means: k-means is a hard-assignment, spherical covariance limit.
- Compared to HMM: GMM ignores temporal structure; HMM adds state transitions.
- Boundary: high-dimensional data can cause singular covariance and overfitting.

## Failure modes
- Singular covariance when a component collapses onto a point.
- Overfitting with large $K$.
- Sensitivity to initialization.
- Non-Gaussian clusters poorly modeled.

## Minimal pseudo-code
```text
Input: X, K
Initialize pi_k, mu_k, Sigma_k
Repeat:
  E-step: r_ik ∝ pi_k N(x_i | mu_k, Sigma_k)
  M-step: update pi_k, mu_k, Sigma_k using r_ik
Return parameters
```

## Decision checklist
- [ ] K selected by validation or information criteria
- [ ] Covariance type chosen (full/diag/spherical)
- [ ] Initialization and regularization in place
- [ ] Compared to k-means baseline

## Personal notes
TODO

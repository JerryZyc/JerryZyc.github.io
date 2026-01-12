---
layout: single
title: "支持向量机 SVM"
permalink: /learning/machine-learning/classical-models/svm/
classes: wide
---

## One-line definition
A support vector machine finds a maximum-margin linear separator by solving a convex QP with hinge loss, optionally using kernels.

## Problem setting
- Inputs: $x \in \mathbb{R}^d$, labels $y \in \{-1, +1\}$.
- Outputs: parameters $w, b$ (and support vectors in kernelized form).
- Assumptions: linear separability (hard margin) or approximate separability (soft margin).
- Boundary: binary classification; multiclass requires one-vs-rest or structured formulations.

## Mathematical formulation
**Soft-margin primal:**
$$
\min_{w,b,\xi} \; \frac{1}{2}\|w\|_2^2 + C \sum_{i=1}^n \xi_i
$$
subject to
$$
y_i (w^\top x_i + b) \ge 1 - \xi_i, \; \xi_i \ge 0
$$

Equivalent unconstrained form with hinge loss:
$$
\min_{w,b} \; \frac{1}{2}\|w\|_2^2 + C \sum_{i=1}^n \max(0, 1 - y_i(w^\top x_i + b))
$$

Dual (kernelized) uses $K(x_i, x_j)$ with support vectors.

## Algorithmic interpretation
- Maximizes geometric margin; only support vectors define the decision boundary.
- Kernel trick enables nonlinear decision boundaries without explicit feature maps.

## Optimization & implementation details
- Objective source: margin maximization with hinge loss.
- Solver: SMO for dual; primal SGD for large-scale linear SVM.
- Complexity: kernel SVM typically $O(n^2)$ memory and time; linear SVM scales with $O(nd)$.
- Numerical notes: feature scaling is critical; choose $C$ (and kernel params) via validation.

## Connections & boundaries
- Compared to logistic regression: SVM optimizes margin, logistic optimizes log-likelihood.
- Compared to perceptron: SVM adds margin and convex objective.
- Compared to kernel ridge: different loss (hinge vs squared), different robustness.
- Boundary: kernel SVM is expensive for large $n$; linear SVM for high-dimensional sparse data.

## Failure modes
- Poor kernel or hyperparameters cause under/overfitting.
- Overlap and noise reduce margin effectiveness.
- Unscaled features distort margin geometry.
- Large $n$ makes kernel SVM infeasible.

## Minimal pseudo-code
```text
Input: X, y in {-1, +1}
Initialize w, b
Repeat:
  For each (x_i, y_i):
    if y_i (w^T x_i + b) < 1:
      w = w - eta (w - C y_i x_i)
    else:
      w = w - eta w
Return w, b
```

## Decision checklist
- [ ] Linear vs kernel SVM chosen based on data size
- [ ] Features scaled
- [ ] C (and kernel params) tuned
- [ ] Compared to logistic regression baseline

## Personal notes
TODO

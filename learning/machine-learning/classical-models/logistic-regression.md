---
layout: single
title: "逻辑回归 Logistic Regression"
permalink: /learning/machine-learning/classical-models/logistic-regression/
classes: wide
---

## One-line definition
A logistic regression model estimates $P(y=1\mid x)$ via $\sigma(w^\top x + b)$ and fits parameters by MLE for Bernoulli labels.

## Problem setting
- Inputs: feature vector $x \in \mathbb{R}^d$, dataset $\{(x_i, y_i)\}_{i=1}^n$ with $y_i \in \{0,1\}$.
- Outputs: parameters $w \in \mathbb{R}^d$, bias $b \in \mathbb{R}$.
- Assumptions: conditional Bernoulli; log-odds is linear in $x$.
- Boundary: binary classification; multiclass needs softmax (multinomial logistic).

## Mathematical formulation
Define $\sigma(t) = 1 / (1 + e^{-t})$ and $p_i = \sigma(w^\top x_i + b)$.

**From MLE (Bernoulli likelihood):**
$$
\max_{w,b} \; \sum_{i=1}^n \left[y_i \log p_i + (1-y_i) \log(1-p_i)\right]
$$

Equivalent minimization of negative log-likelihood (cross-entropy):
$$
\min_{w,b} \; -\sum_{i=1}^n \left[y_i \log p_i + (1-y_i) \log(1-p_i)\right]
$$

Optionally add $\ell_2$ regularization: $\lambda \|w\|_2^2$.

## Algorithmic interpretation
- Convex optimization with a linear decision boundary $w^\top x + b = 0$.
- Learns calibrated probabilities under correct model assumptions.

## Optimization & implementation details
- Objective source: MLE for Bernoulli labels.
- Solver: Newton/IRLS for small to medium $d$; L-BFGS or SGD for large-scale.
- Complexity: Newton step $O(nd^2 + d^3)$; SGD $O(nd)$ per epoch.
- Numerical notes: use log-sum-exp tricks; clip probabilities; standardize features.

## Connections & boundaries
- Compared to linear regression: linear regression minimizes squared loss for continuous targets; logistic uses log-likelihood for Bernoulli labels.
- Compared to SVM: SVM maximizes margin with hinge loss; logistic provides probabilistic outputs.
- Compared to naive Bayes: logistic is discriminative; naive Bayes is generative.
- Boundary: linear log-odds; if relation is nonlinear, use feature maps or nonlinear models.

## Failure modes
- Perfectly separable data yields unbounded weights without regularization.
- Class imbalance biases decision threshold.
- Multicollinearity leads to unstable coefficients.
- Outliers with extreme features can dominate gradients.

## Minimal pseudo-code
```text
Input: X in R^{n x d}, y in {0,1}^n
Initialize w, b
Repeat until convergence:
  p = sigmoid(X w + b)
  grad_w = X^T (p - y) + 2 lambda w
  grad_b = sum(p - y)
  Update w, b
Return w, b
```

## Decision checklist
- [ ] Labels are Bernoulli and log-odds linearity is acceptable
- [ ] Class imbalance handled (weights or threshold)
- [ ] Regularization chosen to prevent separation
- [ ] Compared to SVM and tree-based baselines

## Personal notes
TODO

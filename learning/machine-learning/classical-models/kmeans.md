---
layout: single
title: "K-means 聚类 K-means"
permalink: /learning/machine-learning/classical-models/kmeans/
classes: wide
---

## One-line definition
K-means partitions data into $K$ clusters by minimizing within-cluster squared Euclidean distance to centroids.

## Problem setting
- Inputs: data points $\{x_i\}_{i=1}^n$, $x_i \in \mathbb{R}^d$.
- Outputs: centroids $\{\mu_k\}_{k=1}^K$ and assignments $z_i \in \{1,\dots,K\}$.
- Assumptions: spherical clusters, similar variance, Euclidean distance meaningful.
- Boundary: requires $K$; not suitable for non-spherical or manifold clusters.

## Mathematical formulation
$$
\min_{\{\mu_k\}, \{z_i\}} \; \sum_{i=1}^n \|x_i - \mu_{z_i}\|_2^2
$$

## Algorithmic interpretation
- Alternating minimization: assign to nearest centroid, then update centroids.
- Equivalent to EM for GMM with equal spherical covariances and hard assignments.

## Optimization & implementation details
- Objective source: within-cluster SSE.
- Solver: Lloyd's algorithm (local optimum).
- Complexity: $O(n K d)$ per iteration.
- Numerical notes: use k-means++ initialization; multiple restarts; standardize features.

## Connections & boundaries
- Compared to GMM: GMM uses soft assignments and covariance; k-means is a hard, spherical limit.
- Compared to spectral clustering: k-means assumes Euclidean geometry, spectral can capture non-convex structure.
- Boundary: sensitive to scale and outliers; requires pre-processing.

## Failure modes
- Poor initialization yields bad local minima.
- Different feature scales distort assignments.
- Outliers pull centroids.
- Empty clusters during updates.

## Minimal pseudo-code
```text
Input: X, K
Initialize centroids mu_k
Repeat:
  Assign z_i = argmin_k ||x_i - mu_k||^2
  Update mu_k = mean of points assigned to k
Return mu_k, z
```

## Decision checklist
- [ ] K chosen with validation or domain prior
- [ ] Features scaled
- [ ] k-means++ and multiple restarts used
- [ ] Compared to GMM or density-based clustering

## Personal notes
TODO


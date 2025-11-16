"""
    # Problem Statement

You are building an AI system that processes data through multiple transformation layers. Each layer applies a matrix transformation to the input. The system stability depends on the eigenvalues of these transformation matrices.

Consider a sequence of 2×2 matrices where each matrix is generated using the following rule:

**Matrix Generation Rule:**

- M₁ is the starting matrix [[2, 1], [1, 2]]
- For n ≥ 2: Mₙ = (Mₙ₋₁ + Mₙ₋₁ᵀ) / 2

Where Mᵀ denotes the transpose of M.

**Your Task:**

1. Generate the first 100 matrices in this sequence
2. For each matrix, compute both eigenvalues (λ₁ and λ₂)
3. Calculate the "eigenvalue product sum" S = Σ(λ₁ × λ₂) for all 100 matrices
4. Find how many matrices in the sequence have their maximum eigenvalue greater than 2.5

**Additional Challenge:**

A matrix is considered "stable" for AI training if:

- Both eigenvalues are positive (the matrix is positive definite)
- The ratio of the largest to smallest eigenvalue (condition number) is less than 10

Count how many of the first 100 matrices are "stable" according to this definition.

**Output Format:**

Your program should output:

1. The eigenvalue product sum S (rounded to 2 decimal places)
2. The count of matrices with maximum eigenvalue > 2.5
3. The count of "stable" matrices

**Example (First 3 matrices):**

Matrix M₁ = [[2, 1], [1, 2]]

- Eigenvalues: λ₁ = 3.0, λ₂ = 1.0
- Product: 3.0

Matrix M₂ = [[2, 1], [1, 2]] (symmetric, so unchanged)

- Eigenvalues: λ₁ = 3.0, λ₂ = 1.0
- Product: 3.0

Matrix M₃ = [[2, 1], [1, 2]] (will remain the same)

- Eigenvalues: λ₁ = 3.0, λ₂ = 1.0
- Product: 3.0

---

## Hints

1. The operation (M + Mᵀ) / 2 creates a symmetric matrix
2. Symmetric matrices always have real eigenvalues
3. The determinant of a matrix equals the product of its eigenvalues
4. NumPy's `np.linalg.eig()` returns eigenvalues in no particular order
5. Think about what happens when you keep averaging a matrix with its transpose
"""

M1 = [[2, 1], [1, 2]]
import numpy as np


def generate_matrix(n):
    if n == 1:
        return np.array(M1)
    else:
        M_prev = generate_matrix(n - 1)
        M_transpose = M_prev.T
        M_n = (M_prev + M_transpose) / 2
        return M_n


if __name__ == "__main__":
    sequence = [generate_matrix(i) for i in range(1, 101)]
    product_sum = 0
    max_eigenvalue_count = 0
    stable_matrix_count = 0
    for i in range(100):
        eigenvalues, _ = np.linalg.eig(sequence[i])
        lambda1, lambda2 = eigenvalues[eigenvalues.argsort()[::-1]]
        product_sum += lambda1 * lambda2
        if lambda1 > 2.5:
            max_eigenvalue_count += 1
        if lambda1 > 0 and lambda2 > 0 and (lambda1 / lambda2) < 10:
            stable_matrix_count += 1
    print(f"Eigenvalue Product Sum S: {product_sum:.2f}")
    print(f"Count of matrices with max eigenvalue > 2.5: {max_eigenvalue_count}")
    print(f"Count of stable matrices: {stable_matrix_count}")

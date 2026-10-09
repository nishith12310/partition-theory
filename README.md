# Partition Theory

A Python toolkit for exploring, enumerating, and visualizing **integer partitions** and **Ferrers diagrams**.

---

## Overview

In number theory and combinatorics, a **partition** of a positive integer $n$ is a way of writing $n$ as a sum of positive integers, where the order of summands does not matter:

$$n = \lambda_1 + \lambda_2 + \dots + \lambda_k \quad \text{where} \quad \lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_k \ge 1$$

Each $\lambda_i$ is called a **part** of the partition. The total number of partitions of $n$ is given by the partition function $p(n)$.

This repository provides clean, educational Python implementations to:
1. **Enumerate and count** all partitions of integers up to $n$ recursively.
2. **Visualize** partitions and their conjugates side-by-side using **Ferrers diagrams** with Matplotlib.

---

## Features

- **Partition Enumeration (`list_partitions.py`)**:
  - Recursively generates all partitions of integers from $n = 0$ to $n = 10$.
  - Enforces non-increasing order to prevent duplicate permutations (e.g., $4+3+2$ vs $2+3+4$).
  - Verifies generated partition counts against known values of $p(n)$.

- **Ferrers Diagram & Conjugates (`ferrers_diagram.py`)**:
  - Computes the **conjugate partition** (reading dots by columns instead of rows).
  - Renders side-by-side graphical Ferrers diagrams using Matplotlib dots.
  - Automatically exports the generated diagram as `ferrers_diagram.png`.
  - Validates that the input partition is non-empty, positive, and non-increasing.

---

## Project Structure

```text
partition-theory/
├── ferrers_diagram.py   # Visualizes partitions and their conjugates via Ferrers diagrams
├── list_partitions.py   # Recursively lists and counts integer partitions for n = 0..10
└── README.md            # Project documentation
```

---

## Mathematical Concepts

### 1. The Partition Function $p(n)$

The partition function $p(n)$ represents the number of distinct partitions of $n$. For small values of $n$:

| $n$ | Partitions | $p(n)$ |
|:---:|:---|:---:|
| **0** | `(empty)` | 1 |
| **1** | `1` | 1 |
| **2** | `2`, `1 + 1` | 2 |
| **3** | `3`, `2 + 1`, `1 + 1 + 1` | 3 |
| **4** | `4`, `3 + 1`, `2 + 2`, `2 + 1 + 1`, `1 + 1 + 1 + 1` | 5 |
| **5** | `5`, `4 + 1`, `3 + 2`, `3 + 1 + 1`, `2 + 2 + 1`, `2 + 1 + 1 + 1`, `1 + 1 + 1 + 1 + 1` | 7 |

### 2. Ferrers Diagrams

A Ferrers diagram represents a partition visually: each part is shown as a horizontal row of dots, ordered from largest to smallest.

For the partition $4 + 3 + 2$ of $9$:
```text
Row 1 (4 dots):  ●  ●  ●  ●
Row 2 (3 dots):  ●  ●  ●
Row 3 (2 dots):  ●  ●
```

### 3. Conjugate Partitions

The **conjugate** (or transpose) of a partition is obtained by reading the Ferrers diagram along its columns:
- Column 1 has 3 dots
- Column 2 has 3 dots
- Column 3 has 2 dots
- Column 4 has 1 dot

Hence, the conjugate of $4 + 3 + 2$ is $3 + 3 + 2 + 1$.

---

## Requirements & Installation

- **Python 3.8+**
- **Matplotlib** (required for `ferrers_diagram.py`)

Install dependencies via `pip`:

```bash
pip install matplotlib
```

*(Note: `list_partitions.py` uses only Python's standard library and has no external dependencies.)*

---

## Usage

### 1. Listing Partitions

Run `list_partitions.py` to generate and display all partitions for integers from $0$ to $10$:

```bash
python list_partitions.py
```

**Example Output Snippet:**

```text
Partitions of 4
    4
    3 + 1
    2 + 2
    2 + 1 + 1
    1 + 1 + 1 + 1
p(4) = 5

Partitions of 5
    5
    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1
p(5) = 7
```

### 2. Plotting Ferrers Diagrams

Run `ferrers_diagram.py` to display and save the Ferrers diagram for the configured partition:

```bash
python ferrers_diagram.py
```

**Console Output:**

```text
Partition: 4 + 3 + 2
Conjugate: 3 + 3 + 2 + 1
```

This will:
- Open an interactive window showing the partition and conjugate side-by-side.
- Save a high-resolution image to `ferrers_diagram.png`.

#### Customizing the Partition

To visualize a different partition, edit the `PARTITION` variable in [ferrers_diagram.py](file:///c:/Users/DELL/Documents/GitHub/partition-theory/ferrers_diagram.py#L18):

```python
PARTITION = [5, 4, 4, 2, 1]  # Must be positive integers in non-increasing order
```

---

## Contributing

Contributions and extensions are welcome! Potential enhancements include:
- Generating Young tableaux and hook-length formulas.
- Implementing Euler's pentagonal number theorem for computing $p(n)$ in $O(n^{1.5})$.
- Command-line argument support (`argparse`) for passing custom integers or partitions directly.

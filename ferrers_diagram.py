# Drawing a partition as a Ferrers diagram (dots), next to its conjugate
#
#  
# # Ferrers diagram: each part of the partition becomes a row of dots,
# with the longest row on top.  Example: 4 + 3 + 2
#
#     * * * *
#     * * *
#     * *
#
# Conjugate: read the same dots by COLUMNS instead of rows.
# The columns above have lengths 3, 3, 2, 1, so the conjugate is 3 + 3 + 2 + 1.

##############################################################################

import matplotlib.pyplot as plt

PARTITION = [4, 3, 2]


def conjugate(parts):
    return [sum(1 for p in parts if p >= c) for c in range(1, parts[0] + 1)]


def format_partition(parts):
    return " + ".join(map(str, parts))


def draw_diagram(ax, parts, title):
    for row, length in enumerate(parts):
        ax.plot(range(length), [-row] * length, "o", color="royalblue", markersize=22)
    ax.set_title(title, fontsize=14)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.7, max(parts) - 0.3)
    ax.set_ylim(-len(parts) + 0.3, 0.7)


def main():
    parts = PARTITION
    if not parts or any(a < b for a, b in zip(parts, parts[1:])) or parts[-1] < 1:
        raise ValueError("partition must be positive and non-increasing")

    conj = conjugate(parts)

    print(f"Partition: {format_partition(parts)}")
    print(f"Conjugate: {format_partition(conj)}")

    fig, (left, right) = plt.subplots(1, 2, figsize=(9, 5))
    draw_diagram(left, parts, f"Partition: {format_partition(parts)}")
    draw_diagram(right, conj, f"Conjugate: {format_partition(conj)}")
    fig.suptitle(f"Ferrers diagram of a partition of {sum(parts)}", fontsize=16, y=1.05)

    fig.savefig("ferrers_diagram.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()


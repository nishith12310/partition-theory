

# Listing and counting partitions of n, for n = 0 to 10
#
# A partition of n is a way of writing n as a sum of positive whole numbers,
# where the order does not matter.  Example: 4 + 3 + 2 is a partition of 9.
#
# To avoid counting the same partition twice (like 4+3+2 and 2+3+4),
# we always write the parts from biggest to smallest.

KNOWN_COUNTS = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]


def partitions(n, max_part):
    """Return all partitions of n with parts <= max_part, in non-increasing order."""
    if n == 0:
        return [[]]
    result = []
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            result.append([first] + rest)
    return result


def main():
    for n in range(11):
        parts = partitions(n, n)
        if len(parts) != KNOWN_COUNTS[n]:
            raise ValueError(f"p({n}): got {len(parts)}, expected {KNOWN_COUNTS[n]}")
        print(f"Partitions of {n}")
        for p in parts:
            print("    " + (" + ".join(map(str, p)) or "(empty)"))
        print(f"p({n}) = {len(parts)}")
        print()


if __name__ == "__main__":
    main()

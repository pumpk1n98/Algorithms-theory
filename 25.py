from collections import defaultdict


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[b] = a
        return True


def kruskal_with_order(n, edges):
    dsu = DSU(n)
    res = []

    for u, v, w in edges:
        if dsu.union(u, v):
            res.append((u, v, w))

    return res


def build_order(n, all_edges, mst_edges):
    """
    Строим допустимый порядок:
    - сначала ребра MST
    - потом остальные
    (веса не нарушаются → порядок допустим)
    """

    mst_set = {tuple(sorted((u, v))) for u, v, w in mst_edges}

    mst_part = []
    other_part = []

    for u, v, w in all_edges:
        if tuple(sorted((u, v))) in mst_set:
            mst_part.append((u, v, w))
        else:
            other_part.append((u, v, w))

    # порядок: MST-ребра первыми
    return mst_part + other_part


# =========================
# Демонстрация утверждения
# =========================

n = 5

all_edges = [
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 2),
    (0, 2, 2),
    (1, 3, 3)
]

# некоторое MST (одно из возможных)
mst_edges = [
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 2)
]

order = build_order(n, all_edges, mst_edges)

result = kruskal_with_order(n, order)

print("Полученное дерево Крускала:")
for e in result:
    print(e)

print("\nСовпадает ли с заданным MST?")
print(set(tuple(sorted((u, v))) for u, v, w in result) ==
      set(tuple(sorted((u, v))) for u, v, w in mst_edges))
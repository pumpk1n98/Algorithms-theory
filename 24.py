from collections import defaultdict, deque


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


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []              # все ребра графа
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w):
        # сохраняем ребро (для MST)
        self.edges.append((u, v, w))

        # и в список смежности (для проверок)
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def build_mst(self):
        """
        Строит MST алгоритмом Крускала.
        Возвращает новое дерево Graph.
        """

        # сортировка рёбер по весу (Крускал)
        edges = sorted(self.edges, key=lambda x: x[2])

        dsu = DSU(self.n)
        mst = Graph(self.n)

        for u, v, w in edges:
            # добавляем ребро, если не образует цикл
            if dsu.union(u, v):
                mst.add_edge(u, v, w)

        return mst


def is_still_mst(tree, v, w, new_cost):
    """
    Проверяет, остается ли дерево MST
    после добавления нового ребра (v, w, new_cost).
    """

    parent = {v: None}
    edge_weight = {}

    q = deque([v])

    while q:
        u = q.popleft()

        if u == w:
            break

        for to, weight in tree.adj[u]:
            if to not in parent:
                parent[to] = u
                edge_weight[to] = weight
                q.append(to)

    # максимум на пути v -> w
    current = w
    max_weight = -1

    while parent[current] is not None:
        max_weight = max(max_weight, edge_weight[current])
        current = parent[current]

    return new_cost >= max_weight


# =========================
# Пример использования
# =========================

g = Graph(5)

g.add_edge(0, 1, 2)
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 5)

# строим MST
tree = g.build_mst()

# проверка нового ребра
print(is_still_mst(tree, 0, 4, 6))  # True
print(is_still_mst(tree, 0, 4, 1))  # False

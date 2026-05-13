from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def add(self, u, v, w):
        self.g[u].append((v, w))
        self.g[v].append((u, w))


def is_mst(T, v, w, c):
    # BFS для поиска пути v -> w
    q = deque([v])
    p = {v: None}      # parent
    ew = {}            # вес ребра до вершины

    while q:
        u = q.popleft()

        if u == w:
            break

        for to, wt in T.g[u]:
            if to not in p:
                p[to] = u
                ew[to] = wt
                q.append(to)

    # ищем максимальный вес на пути
    mx = -1
    cur = w

    while p[cur] is not None:
        mx = max(mx, ew[cur])
        cur = p[cur]

    # если новое ребро не легче максимального,
    # то T остается MST
    return c >= mx


# ===== пример =====

T = Graph()

T.add(0, 1, 2)
T.add(1, 2, 3)
T.add(2, 3, 4)
T.add(3, 4, 5)

print(is_mst(T, 0, 4, 6))  # True
print(is_mst(T, 0, 4, 1))  # False
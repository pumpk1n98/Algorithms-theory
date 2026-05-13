from collections import defaultdict


class DSU:
    def __init__(self, n):
        # структура непересекающихся множеств (Union-Find)
        self.p = list(range(n))

    def find(self, x):
        # поиск представителя множества с компрессией пути
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        # объединение множеств; возвращает False, если цикл
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[b] = a
        return True


def kruskal(edges, n):
    # стандартный Крускал по заданному порядку рёбер
    dsu = DSU(n)
    res = []

    for u, v, w in edges:
        # добавляем ребро, если не образует цикл
        if dsu.union(u, v):
            res.append((u, v, w))

    return res


def build_order(all_edges, mst_edges):
    """
    Строим допустимый порядок обработки рёбер Крускалом.

    Идея доказательства:
    - рёбра MST ставим раньше остальных
    - веса при этом не нарушаются (упорядочение остаётся допустимым)
    """

    # множество рёбер MST (для быстрого поиска)
    mst_set = {tuple(sorted((u, v))) for u, v, w in mst_edges}

    mst_part = []    # рёбра, которые должны войти в MST
    other_part = []  # остальные рёбра графа

    for u, v, w in all_edges:
        edge = tuple(sorted((u, v)))

        # если ребро принадлежит заданному MST
        if edge in mst_set:
            mst_part.append((u, v, w))
        else:
            other_part.append((u, v, w))

    # сначала MST-рёбра, потом остальные
    # это и есть "подходящий" допустимый порядок Крускала
    return mst_part + other_part


# =========================
# Пример (демонстрация теоремы)
# =========================

n = 5

# все рёбра графа (не обязательно отсортированы)
all_edges = [
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 2),
    (0, 2, 2),
    (1, 3, 3)
]

# одно из возможных MST графа
mst_edges = [
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 2)
]

# строим "специальный" допустимый порядок
order = build_order(all_edges, mst_edges)

# запускаем Крускала в этом порядке
result = kruskal(order, n)

# вывод результата
print("Результат Крускала:")
for e in result:
    print(e)

# проверка: совпадает ли структура рёбер с заданным MST
result_set = {tuple(sorted((u, v))) for u, v, w in result}
mst_set = {tuple(sorted((u, v))) for u, v, w in mst_edges}

print("\nСовпадает ли с заданным MST?")
print(result_set == mst_set)

import itertools

def total_profit(order, r):
    """
    order — порядок продажи (индексы товаров)
    r — список коэффициентов убывания
    """
    profit = 0
    for t, j in enumerate(order):
        profit += 100 * (r[j] ** t)
    return profit

def brute_force_best_order(r):
    n = len(r)
    best_order = None
    best_profit = -1
    for perm in itertools.permutations(range(n)):
        profit = total_profit(perm, r)
        if profit > best_profit:
            best_profit = profit
            best_order = perm

    return best_order, best_profit
# пример
r = [0.9, 0.8, 0.95]
best_order, best_profit = brute_force_best_order(r)
print("Лучший порядок (индексы):", best_order)
print("Максимальная прибыль:", best_profit)

# для удобства — сами коэффициенты в этом порядке
print("В порядке продажи:", [r[i] for i in best_order])

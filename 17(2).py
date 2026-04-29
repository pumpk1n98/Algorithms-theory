def optimal_selling_order(r):
    # r — список коэффициентов уменьшения
    indexed = list(enumerate(r))
    
    # сортировка по возрастанию r_i
    indexed.sort(key=lambda x: x[1])
    
    # порядок продаж
    order = [i for i, _ in indexed]
    return order


# пример
r = [0.9, 0.8, 0.95]
print(optimal_selling_order(r))
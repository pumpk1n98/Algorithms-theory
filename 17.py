def optimal_purchase_order(r):
    # r — список коэффициентов роста
    indexed = list(enumerate(r))  # (индекс, значение)
    
    # сортировка по убыванию r_i
    indexed.sort(key=lambda x: x[1], reverse=True)
    
    # возвращаем порядок индексов покупок
    order = [i for i, _ in indexed]
    return order


# пример
r = [1.1, 1.05, 1.2]
print(optimal_purchase_order(r))
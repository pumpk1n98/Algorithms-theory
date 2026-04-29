from collections import deque

def is_consistent(n, edges):
    # Строим список смежности
    # adj[v] = список (сосед, тип связи)
    adj = [[] for _ in range(n)]
    
    for u, v, t in edges:
        adj[u].append((v, t))
        adj[v].append((u, t))
    
    # -1 = не покрашен, 0 и 1 = два вида (A и B)
    color = [-1] * n
    
    # Проверяем каждую компоненту связности
    for start in range(n):
        if color[start] != -1:
            continue
        
        # Начинаем BFS
        queue = deque([start])
        color[start] = 0
        
        while queue:
            u = queue.popleft()
            
            for v, t in adj[u]:
                if color[v] == -1:
                    # Если не покрашен — красим
                    if t == 0:  # одинаковые
                        color[v] = color[u]
                    else:       # разные
                        color[v] = 1 - color[u]
                    
                    queue.append(v)
                
                else:
                    # Проверяем на противоречие
                    if t == 0 and color[v] != color[u]:
                        return False
                    if t == 1 and color[v] == color[u]:
                        return False
    
    return True


# ==== ЧТЕНИЕ ВХОДА ====

n, m = map(int, input().split())

edges = []
for _ in range(m):
    i, j, t = map(int, input().split())
    # делаем индексацию с 0
    edges.append((i - 1, j - 1, t))

# ==== ВЫВОД ====

if is_consistent(n, edges):
    print("YES")
else:
    print("NO")
import heapq

def dijkstra(graph, start):

    # Если передана матрица смежности, конвертируем в список смежности
    if isinstance(graph, list):
        n = len(graph)
        adj = {i: {} for i in range(n)}
        for i in range(n):
            for j in range(n):
                w = graph[i][j]
                if w > 0:
                    adj[i][j] = w
        graph = adj

    INF = float('inf')
    dist = {v: INF for v in graph}
    prev = {v: None for v in graph}
    dist[start] = 0

    R = set()          # Множество результирующих вершин
    Q = []             # Множество кандидатов

    # ШАГ 1. В R добавляется n0, смежные в Q
    R.add(start)       # n0 в R
    for v, w in graph[start].items():     # просмотр смежных
        dist[v] = w                       # расстояние до n0
        prev[v] = start                   # запоминаем ребро
        heapq.heappush(Q, (w, v))         # добавляем в Q

    # ШАГ 2: Выбор вершины из Q
    while Q:
        d, u = heapq.heappop(Q)          # выбор ближайшей из Q
        if u in R:                       # при извлечении из Q, если уже в R → пропуск
            continue
        R.add(u)                         # добавление в R

        # ШАГ 3: Просмотр смежных вершин
        for v, w in graph[u].items():
            if v in R:                   # при просмотре соседей, если уже в R → пропуск
                continue
            new_d = d + w
            if new_d < dist[v]:          
                dist[v] = new_d          # обновляем расстояние
                prev[v] = u              # обновляем ссылку
                heapq.heappush(Q, (new_d, v))      # новая запись в Q
    # выход из цикла когда Q пуст
    
    return dist, prev

def get_path(prev, start, end):
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    return path if path and path[0] == start else []

# Пример использования 
if __name__ == "__main__":
    matrix = [
        [0, 2, 1, 0, 0],
        [2, 0, 4, 7, 0],
        [1, 4, 0, 3, 5],
        [0, 7, 3, 0, 6],
        [0, 0, 5, 6, 0]
    ]
    dist, prev = dijkstra(matrix, start=0)
    print("Кратчайшие расстояния от вершины 0:", dist)
    for v in sorted(dist.keys()):
        if v != 0 and dist[v] != float('inf'):
            print(f"Кратчайший путь от вершины 0 до вершины {v}: {get_path(prev, 0, v)}, расстояние: {dist[v]}")

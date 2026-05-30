import heapq

def dijkstra(graph, start):

    # Если передана матрица смежности → конвертируем в список смежности
    if isinstance(graph, list) and all(isinstance(row, list) for row in graph):
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
    Q = []             # Множество кандидатов (приоритетная очередь)

    # ШАГ 1 (PDF): В R добавляется n0, смежные в Q
    R.add(start)
    for v, w in graph[start].items():
        dist[v] = w
        prev[v] = start
        heapq.heappush(Q, (w, v))

    # ШАГ 2-4: Итеративная обработка
    while Q:
        d, u = heapq.heappop(Q)          # ШАГ 2: выбор ближайшей из Q
        if u in R:                       # Категория 1: уже в R → пропуск
            continue
        R.add(u)                         # ШАГ 2: добавление в R

        # ШАГ 3: просмотр смежных вершин
        for v, w in graph[u].items():
            if v in R:                   # Категория 1
                continue
            new_d = d + w
            if new_d < dist[v]:          # Категории 2 и 3
                dist[v] = new_d
                prev[v] = u
                heapq.heappush(Q, (new_d, v))

    return dist, prev

def get_path(prev, start, end):
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    return path if path and path[0] == start else []

# ==================== ПРИМЕР ====================
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

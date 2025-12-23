def floyd_warshall(graph):
    """
    Floyd–Warshall algoritması.
    Tüm düğüm çiftleri arasındaki en kısa yolları bulur.

    graph : NxN boyutunda ağırlık matrisi
            graph[i][j] = i -> j kenar ağırlığı
            Eğer kenar yoksa float("inf")

    return:
        En kısa yolların bulunduğu NxN matris
    """

    # Düğüm sayısı
    n = len(graph)

    # Mesafe matrisi kopyalanır (orijinal graph bozulmaz)
    dist = [row[:] for row in graph]

    # Dynamic Programming döngüsü (O(n^3))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # i -> k -> j yolu, mevcut i -> j yolundan kısa mı?
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

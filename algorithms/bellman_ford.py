def bellman_ford(vertices,edges,source):
    """
        Bellman-Ford algoritması.
        Tek kaynaklı en kısa yolu bulur ve negatif ağırlıklı döngüleri tespit eder.

        vertices : grafın düğüm sayısı
        edges    : (u, v, w) formatında kenar listesi
        source   : başlangıç düğümü

        return:
            source düğümünden diğer düğümlere olan en kısa mesafeler
        """
    #Başlangıçta tüm düğümlere olan mesafeler sonsuz kabul edilir
    distance=[float("inf")]*vertices

    #Kaynak düğümün mesafesi sıfırdır
    distance[source]=0

    #V-1 kez tüm kenarlar üzerinde relax işlemi yapılır
    for _ in range(vertices-1):
        for u,v,w in edges:
            #Eğer u düğümüne ulaşılabiliyorsa ve
            #u üzerinden v'ye daha kısa bir yol varsa güncelle
            if distance[u]!=float("inf") and distance[u]+w<distance[v]:
                distance[v]=distance[u]+w
    #Negatif ağırlıklı döngü kontrolü
    for u,v,w in edges:
        if distance[u]!=float("inf") and distance[u]+w<distance[v]:
            raise ValueError("Negative weight cycle detected")
    return distance
import random
from algorithms.floyd_warshall import floyd_warshall
from measurements.time_tracker import measure_time
from measurements.energy_tracker import measure_energy
from results.write_csv import write_csv_row


def generate_graph_matrix(n, density=0.3):
    """
    Rastgele yönlü ve ağırlıklı bir grafik üretir (matris formunda).

    n       : düğüm sayısı
    density : kenar olasılığı

    return:
        NxN ağırlık matrisi
    """

    INF = float("inf")
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0  # Kendine mesafe 0

    for i in range(n):
        for j in range(n):
            if i != j and random.random() < density:
                graph[i][j] = random.randint(1, 10)

    return graph


# Farklı boyutlardaki girişler (small / medium / large)
sizes = {
    "small": 50,
    "medium": 100,
    "large": 200
}

for label, n in sizes.items():

    graph = generate_graph_matrix(n)

    # Algoritma öncesi enerji ölçümü
    energy_before = measure_energy()

    # Zaman ölçümü
    time_result = measure_time(floyd_warshall, graph)

    # Algoritma sonrası enerji ölçümü
    energy_after = measure_energy()

    cpu_diff = energy_after["cpu_time_sec"] - energy_before["cpu_time_sec"]
    mem_diff = energy_after["memory_kb"] - energy_before["memory_kb"]

    print(f"\n--- {label.upper()} GRAPH (Floyd-Warshall) ---")
    print(f"Vertices: {n}")
    print(f"Time (s): {time_result['time_sec']:.6f}")

    # CPU zamanı farkı
    print(f"CPU Time (s): {cpu_diff:.6f}")

    # Bellek farkı (KB)
    print(f"Memory (KB): {mem_diff:.2f}")

    write_csv_row(
        algorithm="Floyd-Warshall",
        vertices=n,
        time_sec=time_result["time_sec"],
        cpu_time_sec=cpu_diff,
        memory_kb=mem_diff
    )

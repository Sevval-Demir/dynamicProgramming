import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from algorithms.floyd_warshall import floyd_warshall
from measurements.codecarbon_tracker import measure_with_codecarbon
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

    # Zaman + enerji ölçümü
    cc_result = measure_with_codecarbon(
        measure_time,
        floyd_warshall,
        graph
    )

    time_result = cc_result["result"]
    energy_kwh = cc_result["energy_kwh"]

    # Algoritma sonrası enerji ölçümü
    energy_after = measure_energy()

    cpu_diff = energy_after["cpu_time_sec"] - energy_before["cpu_time_sec"]

    memory_before_kb = energy_before["memory_kb"]
    memory_after_kb  = energy_after["memory_kb"]

    memory_diff_kb = max(0, memory_after_kb - memory_before_kb)

    write_csv_row(
        algorithm="Floyd-Warshall",
        vertices=n,
        time_sec=time_result["time_sec"],
        cpu_time_sec=cpu_diff,
        memory_before_kb=memory_before_kb,
        memory_after_kb=memory_after_kb,
        memory_diff_kb=memory_diff_kb,
        energy_kwh=energy_kwh
    )



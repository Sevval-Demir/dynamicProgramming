import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.floyd_warshall import floyd_warshall
from measurements.time_tracker import measure_time
from measurements.energy_tracker import measure_energy
from results.write_csv import write_csv_row


def generate_graph_matrix(n, density=0.3):
    """
    Rastgele yönlü ve ağırlıklı bir grafik üretir (matris formunda).
    """
    INF = float("inf")
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for i in range(n):
        for j in range(n):
            if i != j and random.random() < density:
                graph[i][j] = random.randint(1, 10)

    return graph


def run_floyd_experiment(vertices, density, level, repetition_id):
    graph = generate_graph_matrix(vertices, density)

    energy_before = measure_energy()

    time_result = measure_time(
        floyd_warshall,
        graph
    )

    energy_after = measure_energy()

    cpu_diff = energy_after["cpu_time_sec"] - energy_before["cpu_time_sec"]

    memory_before_kb = energy_before["memory_kb"]
    memory_after_kb = energy_after["memory_kb"]
    memory_diff_kb = max(0, memory_after_kb - memory_before_kb)

    energy_score = time_result["time_sec"] * memory_diff_kb

    write_csv_row(
        algorithm="Floyd-Warshall",
        input_level=level,
        vertices=vertices,
        edge_density=density,
        repetition_id=repetition_id,
        time_sec=time_result["time_sec"],
        cpu_time_sec=cpu_diff,
        memory_before_kb=memory_before_kb,
        memory_after_kb=memory_after_kb,
        memory_diff_kb=memory_diff_kb,
        energy_score=energy_score
    )


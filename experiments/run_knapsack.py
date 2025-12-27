import sys
import os
import random
from measurements.codecarbon_tracker import measure_with_codecarbon

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.knapsack_01 import knapsack_01
from measurements.time_tracker import measure_time
from measurements.energy_tracker import measure_energy
from results.write_csv import write_csv_row


def generate_knapsack_instance(n):
    weights = [random.randint(1, 20) for _ in range(n)]
    values = [random.randint(10, 100) for _ in range(n)]
    capacity = n * 2
    return weights, values, capacity


def run_knapsack_experiment(n_items, repetition_id):
    weights, values, capacity = generate_knapsack_instance(n_items)

    energy_before = measure_energy()

    cc_result = measure_with_codecarbon(
        knapsack_01,
        weights,
        values,
        capacity
    )

    time_result = measure_time(
        knapsack_01,
        weights,
        values,
        capacity
    )

    energy_after = measure_energy()

    cpu_diff = energy_after["cpu_time_sec"] - energy_before["cpu_time_sec"]

    memory_before_kb = energy_before["memory_kb"]
    memory_after_kb = energy_after["memory_kb"]
    memory_diff_kb = max(0, memory_after_kb - memory_before_kb)

    energy_impact_score = time_result["time_sec"] * memory_diff_kb

    write_csv_row(
        algorithm="Knapsack-01",
        vertices=n_items,              # ⚠️ aynı kolon kullanılıyor
        edge_density=0.0,              # ⚠️ grafik problemi olmadığı için 0
        repetition_id=repetition_id,
        time_sec=time_result["time_sec"],
        cpu_time_sec=cpu_diff,
        memory_before_kb=memory_before_kb,
        memory_after_kb=memory_after_kb,
        memory_diff_kb=memory_diff_kb,
        energy_impact_score=energy_impact_score,
        emissions_kg=cc_result["emissions_kg"]
    )

import sys
import os
import random
from measurements.codecarbon_tracker import measure_with_codecarbon

# Proje kök dizinini ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Algoritma
from algorithms.bellman_ford import bellman_ford

# Ölçüm modülleri
from measurements.time_tracker import measure_time
from measurements.energy_tracker import measure_energy

# CSV yazıcı
from results.write_csv import write_csv_row

from measurements.memory_tracker import measure_peak_memory

def generate_graph(vertices, density=0.3):
    """
    Rastgele yönlü ve ağırlıklı bir grafik üretir.

    vertices : düğüm sayısı
    density  : kenar olasılığı (0–1)

    return:
        (u, v, w) formatında kenar listesi
    """
    edges = []

    for u in range(vertices):
        for v in range(vertices):
            if u != v and random.random() < density:
                weight = random.randint(1, 10)
                edges.append((u, v, weight))

    return edges

SOURCE_NODE = 0

def run_bellman_experiment(vertices, density, repetition_id):
    edges = generate_graph(vertices, density)

    #  ZAMAN ve SİSTEM ÖLÇÜMÜ
    energy_before = measure_energy()

    #  SADECE ALGORİTMA CODECARBON İLE ÖLÇÜLÜR
    cc_result = measure_with_codecarbon(
        bellman_ford,
        vertices,
        edges,
        SOURCE_NODE
    )

    time_result = measure_time(
        bellman_ford,
        vertices,
        edges,
        SOURCE_NODE
    )

    mem_result = measure_peak_memory(
        bellman_ford,
        vertices,
        edges,
        SOURCE_NODE
    )

    peak_memory_kb = mem_result["peak_memory_kb"]

    energy_after = measure_energy()

    # -------------------------------------------------
    # METRİKLER
    # -------------------------------------------------
    cpu_diff = energy_after["cpu_time_sec"] - energy_before["cpu_time_sec"]

    memory_before_kb = energy_before["memory_kb"]
    memory_after_kb = energy_after["memory_kb"]
    memory_diff_kb = max(0, memory_after_kb - memory_before_kb)

    energy_impact_score = time_result["time_sec"] * memory_diff_kb

    write_csv_row(
        algorithm="Bellman-Ford",
        vertices=vertices,
        edge_density=density,
        repetition_id=repetition_id,
        time_sec=time_result["time_sec"],
        cpu_time_sec=cpu_diff,
        memory_before_kb=memory_before_kb,
        memory_after_kb=memory_after_kb,
        memory_diff_kb=memory_diff_kb,
        peak_memory_kb=peak_memory_kb,
        energy_impact_score=energy_impact_score,
        emissions_kg=cc_result["emissions_kg"]
    )


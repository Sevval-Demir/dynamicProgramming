import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random

# Algoritma
from algorithms.bellman_ford import bellman_ford

# Ölçüm modülleri
from measurements.time_tracker import measure_time
from measurements.energy_tracker import measure_energy
from measurements.codecarbon_tracker import measure_with_codecarbon

from results.write_csv import write_csv_row


def generate_graph(vertices, density=0.3):
    """
    Rastgele yönlü ve ağırlıklı bir grafik üretir.

    vertices : grafın düğüm sayısı
    density  : kenar yoğunluğu (0–1 arası olasılık)

    return:
        (u, v, w) formatında kenar listesi
    """

    edges = []

    # Tüm düğüm çiftleri için rastgele kenar üretimi
    for u in range(vertices):
        for v in range(vertices):
            if u != v and random.random() < density:
                weight = random.randint(1, 10)
                edges.append((u, v, weight))

    return edges


# Farklı boyutlardaki girişler (small / medium / large)
sizes = {
    "small": 200,
    "medium": 500,
    "large": 1000
}

# Her giriş boyutu için deney yapılır
for label, v in sizes.items():

    # Rastgele grafik oluştur
    edges = generate_graph(v)

    # Algoritma çalışmadan ÖNCE enerji ölçümü
    energy_before = measure_energy()

    # Algoritmanın çalışma süresi ölçülür
    cc_result = measure_with_codecarbon(
        measure_time,
        bellman_ford,
        v,
        edges,
        0
    )

    time_result = cc_result["result"]
    energy_kwh = cc_result["energy_kwh"]

    # Algoritma çalıştıktan SONRA enerji ölçümü
    energy_after = measure_energy()

    cpu_diff = energy_after["cpu_time_sec"] - energy_before["cpu_time_sec"]

    memory_before_kb = energy_before["memory_kb"]
    memory_after_kb = energy_after["memory_kb"]

    memory_diff_kb = max(0, memory_after_kb - memory_before_kb)

    # Sonuçların ekrana yazdırılması
    print(f"\n--- {label.upper()} GRAPH (Bellman-Ford) ---")
    print(f"Vertices: {v}")
    print(f"Time (s): {time_result['time_sec']:.6f}")

    # CPU zamanı farkı (enerjiye dolaylı gösterge)
    print(f"CPU Time (s): {cpu_diff:.6f}")

    # Bellek kullanım farkı (KB)
    print(f"Memory Before (KB): {memory_before_kb:.2f}")
    print(f"Memory After  (KB): {memory_after_kb:.2f}")
    print(f"Memory Diff   (KB): {memory_diff_kb:.2f}")

    write_csv_row(
        algorithm="Bellman-Ford",
        vertices=v,
        time_sec=time_result["time_sec"],
        cpu_time_sec=cpu_diff,
        memory_before_kb=memory_before_kb,
        memory_after_kb=memory_after_kb,
        memory_diff_kb=memory_diff_kb,
        energy_kwh=energy_kwh
    )


import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "results", "csv", "results.csv")


def write_csv_row(
    algorithm,
    vertices,
    edge_density,
    repetition_id,
    time_sec,
    cpu_time_sec,
    memory_before_kb,
    memory_after_kb,
    memory_diff_kb,
    peak_memory_kb,
    energy_impact_score,
    emissions_kg,
):
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    file_exists = os.path.isfile(CSV_PATH)

    with open(CSV_PATH, mode="a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "algorithm",
                "vertices",
                "edge_density",
                "repetition_id",
                "time_sec",
                "cpu_time_sec",
                "memory_before_kb",
                "memory_after_kb",
                "memory_diff_kb",
                "peak_memory_kb",
                "energy_impact_score",
                "emissions_kg",
            ])

        writer.writerow([
            algorithm,
            vertices,
            edge_density,
            repetition_id,
            round(time_sec, 6),
            round(cpu_time_sec, 6),
            round(memory_before_kb, 2),
            round(memory_after_kb, 2),
            round(memory_diff_kb, 2),
            round(peak_memory_kb, 2),
            round(energy_impact_score, 6),
            emissions_kg,
        ])

import csv
import os

# Proje kök dizinini bul
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(BASE_DIR, "results", "csv", "results.csv")

def write_csv_row(
    algorithm,
    vertices,
    time_sec,
    cpu_time_sec,
    memory_before_kb,
    memory_after_kb,
    memory_diff_kb,
    energy_kwh
):


    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

    file_exists = os.path.isfile(CSV_PATH)

    with open(CSV_PATH, mode="a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "algorithm",
                "vertices",
                "time_sec",
                "cpu_time_sec",
                "memory_kb"
                "energy_kwh"
            ])

        writer.writerow([
            algorithm,
            vertices,
            round(time_sec, 6),
            round(cpu_time_sec, 6),
            round(memory_before_kb, 2),
            round(memory_after_kb, 2),
            round(memory_diff_kb, 2),
            energy_kwh
        ])


import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------
# PATHS
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(BASE_DIR, "results", "csv", "results.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "results", "plots")

os.makedirs(PLOTS_DIR, exist_ok=True)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
df = pd.read_csv(CSV_PATH)

# -------------------------------------------------
# AVERAGE OVER REPETITIONS
# -------------------------------------------------
grouped = (
    df
    .groupby(["algorithm", "vertices"], as_index=False)
    .mean(numeric_only=True)
)

# -------------------------------------------------
# COLORS
# -------------------------------------------------
COLORS = {
    "Bellman-Ford": "#2563eb",
    "Floyd-Warshall": "#f97316",
    "Knapsack-01": "#16a34a"
}

# -------------------------------------------------
# GENERIC PLOT FUNCTION
# -------------------------------------------------
def plot_metric(y_col, y_label, filename, title, log_scale=False):
    plt.figure(figsize=(7, 5))

    for algo in grouped["algorithm"].unique():
        subset = grouped[grouped["algorithm"] == algo]
        subset = subset.sort_values("vertices")

        plt.plot(
            subset["vertices"],
            subset[y_col],
            marker="o",
            linewidth=2,
            label=algo,
            color=COLORS.get(algo, "gray")
        )

    plt.xlabel("Number of Vertices (n)")
    plt.ylabel(y_label)
    plt.title(title)

    if log_scale:
        plt.yscale("log")

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, filename))
    plt.close()

# -------------------------------------------------
# PLOTS
# -------------------------------------------------

# 1️⃣ Time Complexity
plot_metric(
    y_col="time_sec",
    y_label="Execution Time (seconds)",
    filename="time_vs_vertices.png",
    title="Time Complexity vs Number of Vertices"
)

# 2️⃣ Energy Complexity (THEORETICAL: E(n) ∝ T(n))
plot_metric(
    y_col="time_sec",
    y_label="Energy Complexity (Proportional to Time)",
    filename="energy_complexity_vs_vertices.png",
    title="Energy Complexity E(n) vs Number of Vertices"
)

# 3️⃣ Memory Usage
plot_metric(
    y_col="memory_diff_kb",
    y_label="Memory Usage Difference (KB)",
    filename="memory_vs_vertices.png",
    title="Memory Usage vs Number of Vertices"
)

# 4️⃣ Experimental Energy (CodeCarbon)
plot_metric(
    y_col="emissions_kg",
    y_label="CO₂ Emissions (kg)",
    filename="emissions_vs_vertices.png",
    title="Experimental Energy Consumption vs Number of Vertices",
    log_scale=True
)

# 5️⃣ Secondary Metric (Optional)
plot_metric(
    y_col="energy_impact_score",
    y_label="Energy Impact Score (Time × Memory)",
    filename="energy_impact_vs_vertices.png",
    title="Energy Impact Score vs Number of Vertices",
    log_scale=True
)

print("All plots generated successfully.")

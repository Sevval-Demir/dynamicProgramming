import streamlit as st
import sys
import os
import pandas as pd
import subprocess

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Energy-Aware Algorithm Analysis",
    page_icon="⚡",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "results", "csv", "results.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "results", "plots")

# -------------------------------------------------
# CUSTOM THEME (AYNEN KORUNDU)
# -------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f5f3ff, #ecfeff);
}
body {
    color: #1f2937;
    font-family: "Segoe UI", sans-serif;
}
h1 { color: #4338ca; font-weight: 800; }
h2 { color: #4f46e5; font-weight: 600; }
h3 { color: #6366f1; }
section[data-testid="stVerticalBlock"] {
    background-color: #f8fafc;
    padding: 28px;
    border-radius: 22px;
    margin-bottom: 28px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}
.stButton > button {
    background-color: #6366f1;
    color: white;
    border-radius: 16px;
    padding: 0.75em 1.6em;
    border: none;
    font-size: 15px;
    font-weight: 600;
    box-shadow: 0 8px 22px rgba(99,102,241,0.35);
}
.stButton > button:hover {
    background-color: #4f46e5;
}
[data-testid="metric-container"] {
    background-color: #eef2ff;
    border: 1px solid #c7d2fe;
    padding: 16px;
    border-radius: 16px;
}
[data-testid="metric-container"] label {
    color: #4338ca;
}
.stDataFrame {
    background-color: #f8fafc;
    border-radius: 14px;
}
hr {
    border: none;
    height: 1px;
    background-color: #c7d2fe;
    margin: 30px 0;
}
img {
    border-radius: 14px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("⚡ Energy-Aware Algorithm Analysis Dashboard")

st.markdown("""
**CSE303 / BYM303 – Algorithm Analysis Course Project**  
**Energy, Time and Memory Complexity of Dynamic Programming Algorithms**
""")

st.divider()

# -------------------------------------------------
# PARAMETER INPUT (SMALL / MEDIUM / LARGE)
# -------------------------------------------------
st.subheader("🔧 Experiment Parameters")

level = st.selectbox(
    "Input Size Level",
    ["Small", "Medium", "Large"]
)

LEVEL_CONFIG = {
    "Small":  {"v_min": 100, "v_max": 300,  "d_min": 0.1, "d_max": 0.3},
    "Medium": {"v_min": 400, "v_max": 700,  "d_min": 0.3, "d_max": 0.6},
    "Large":  {"v_min": 800, "v_max": 1200, "d_min": 0.6, "d_max": 0.9},
}

cfg = LEVEL_CONFIG[level]

st.info(
    f"Selected **{level}** level → "
    f"Vertices: {cfg['v_min']}–{cfg['v_max']}, "
    f"Density: {cfg['d_min']}–{cfg['d_max']}"
)

c1, c2, c3 = st.columns(3)

with c1:
    vertices = st.slider(
        "Number of Vertices",
        min_value=cfg["v_min"],
        max_value=cfg["v_max"],
        value=(cfg["v_min"] + cfg["v_max"]) // 2,
        step=50
    )

with c2:
    density = st.slider(
        "Edge Density",
        min_value=cfg["d_min"],
        max_value=cfg["d_max"],
        value=round((cfg["d_min"] + cfg["d_max"]) / 2, 2),
        step=0.05
    )

with c3:
    repetitions = st.number_input(
        "Repetitions",
        min_value=1,
        max_value=10,
        value=1
    )

st.divider()

# -------------------------------------------------
# HELPERS (YENİ EKLENEN)
# -------------------------------------------------
def generate_plots():
    plot_script = os.path.join(
        BASE_DIR, "results", "plots", "plot_results.py"
    )
    subprocess.run([sys.executable, plot_script], check=True)

# -------------------------------------------------
# RUN EXPERIMENTS
# -------------------------------------------------
st.subheader("⚙️ Run Experiments")

from experiments.run_bellman import run_bellman_experiment
from experiments.run_floyd import run_floyd_experiment

b1, b2 = st.columns(2)

with b1:
    if st.button("▶ Run Bellman–Ford"):
        for r in range(1, repetitions + 1):
            run_bellman_experiment(vertices, density, level, r)

        generate_plots()
        st.success("Bellman–Ford experiment completed and plots updated.")

with b2:
    if st.button("▶ Run Floyd–Warshall"):
        for r in range(1, repetitions + 1):
            run_floyd_experiment(vertices, density, level, r)

        generate_plots()
        st.success("Floyd–Warshall experiment completed and plots updated.")

st.divider()

# -------------------------------------------------
# RESULTS TABLE
# -------------------------------------------------
st.header("📄 Experimental Results")

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    st.dataframe(df, hide_index=True)

    st.divider()

    st.header("📌 Summary Metrics")
    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Max Vertices", int(df["vertices"].max()))
    with m2:
        st.metric("Max Execution Time (s)", round(df["time_sec"].max(), 2))
    with m3:
        st.metric("Max Energy Score", round(df["energy_score"].max(), 2))
else:
    st.warning("No results.csv found. Run experiments first.")

st.divider()

# -------------------------------------------------
# VISUAL ANALYSIS
# -------------------------------------------------
st.header("📈 Visual Analysis")

def show_plot(filename, title, width=520):
    path = os.path.join(PLOTS_DIR, filename)
    st.subheader(title)
    if os.path.exists(path):
        st.image(path, width=width)
    else:
        st.warning("Plot not found.")

c1, c2 = st.columns(2)

with c1:
    show_plot("time_vs_vertices.png", "Execution Time vs Number of Vertices")

with c2:
    show_plot("memory_vs_vertices.png", "Memory Usage vs Number of Vertices")

show_plot(
    "energy_score_vs_vertices.png",
    "Energy Score (Time × Memory) vs Number of Vertices"
)

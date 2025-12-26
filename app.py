import streamlit as st
import subprocess
import sys
import os
import pandas as pd

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
# CUSTOM DARK + COLORFUL THEME
# -------------------------------------------------
st.markdown("""
<style>

/* ===== APP BACKGROUND ===== */
.stApp {
    background: linear-gradient(
        135deg,
        #eef2ff,
        #f5f3ff,
        #ecfeff
    );
}

/* ===== GENERAL TEXT ===== */
body {
    color: #1f2937;
    font-family: "Segoe UI", sans-serif;
}

/* ===== HEADERS ===== */
h1 {
    color: #4338ca;
    font-weight: 800;
}

h2 {
    color: #4f46e5;
    font-weight: 600;
}

h3 {
    color: #6366f1;
}

/* ===== CONTENT CARDS ===== */
section[data-testid="stVerticalBlock"] {
    background-color: #f8fafc;
    padding: 28px;
    border-radius: 22px;
    margin-bottom: 28px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}

/* ===== BUTTONS ===== */
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

/* ===== METRICS ===== */
[data-testid="metric-container"] {
    background-color: #eef2ff;
    border: 1px solid #c7d2fe;
    padding: 16px;
    border-radius: 16px;
}

[data-testid="metric-container"] label {
    color: #4338ca;
}

/* ===== DATAFRAME ===== */
.stDataFrame {
    background-color: #f8fafc;
    border-radius: 14px;
}

/* ===== DIVIDER ===== */
hr {
    border: none;
    height: 1px;
    background-color: #c7d2fe;
    margin: 30px 0;
}

/* ===== IMAGES ===== */
img {
    border-radius: 14px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def run_script(script_path):
    full_path = os.path.join(BASE_DIR, script_path)
    subprocess.run([sys.executable, full_path], check=True)

def show_plot(filename, title, width=520):
    path = os.path.join(PLOTS_DIR, filename)
    st.subheader(title)
    if os.path.exists(path):
        st.image(path, width=width)
    else:
        st.warning("Plot not found. Please generate plots first.")

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
# CONTROLS
# -------------------------------------------------
st.header("⚙️ Experiment Controls")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶ Run Bellman–Ford"):
        run_script("experiments/run_bellman.py")
        st.success("Bellman–Ford experiments completed.")

with col2:
    if st.button("▶ Run Floyd–Warshall"):
        run_script("experiments/run_floyd.py")
        st.success("Floyd–Warshall experiments completed.")

with col3:
    if st.button("📈 Generate Plots"):
        run_script("results/plots/plot_results.py")
        st.success("Plots generated successfully.")

st.divider()

# -------------------------------------------------
# RESULTS TABLE
# -------------------------------------------------
st.header("📄 Experimental Results")

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)

    st.dataframe(df, hide_index=True)

    st.divider()

    # -------------------------------------------------
    # SUMMARY METRICS
    # -------------------------------------------------
    st.header("📌 Summary Metrics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Max Vertices", int(df["vertices"].max()))

    with c2:
        st.metric("Max Time (s)", round(df["time_sec"].max(), 2))

    with c3:
        st.metric("Max Memory (KB)", int(df["memory_diff_kb"].max()))

    with c4:
        st.metric("Max Energy (kWh)", f"{df['energy_kwh'].max():.2e}")

else:
    st.warning("No results.csv found. Run experiments first.")

st.divider()

# -------------------------------------------------
# PLOTS (COMPACT GRID)
# -------------------------------------------------
st.header("📈 Visual Analysis")

c1, c2 = st.columns(2)

with c1:
    show_plot("time_vs_vertices.png", "Execution Time vs Vertices")

with c2:
    show_plot("cpu_vs_vertices.png", "CPU Time vs Vertices")

c3, c4 = st.columns(2)

with c3:
    show_plot("memory_vs_vertices.png", "Memory Usage vs Vertices")

with c4:
    show_plot("energy_vs_vertices.png", "Energy Consumption vs Vertices")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption("Algorithm Analysis Project – Energy Complexity | 2025")

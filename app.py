import streamlit as st
import subprocess
import sys
import os
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Algorithm Analysis – Energy Complexity",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "results", "csv", "results.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "results", "plots")

# -------------------------------------------------
# DARK THEME (CUSTOM CSS)
# -------------------------------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: #e5e7eb;
    }

    h1, h2, h3, h4 {
        color: #f9fafb;
    }

    .stButton>button {
        background-color: #1e40af;
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        border: none;
        font-size: 16px;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
    }

    .stDataFrame {
        background-color: #020617;
    }

    hr {
        border: 1px solid #334155;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def run_script(script_path):
    full_path = os.path.join(BASE_DIR, script_path)
    subprocess.run([sys.executable, full_path], check=True)

def show_plot(filename, title):
    path = os.path.join(PLOTS_DIR, filename)
    st.subheader(title)
    if os.path.exists(path):
        st.image(path, width="stretch")
    else:
        st.warning("Plot not found. Please generate plots first.")

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("📊 Algorithm Analysis Dashboard")

st.markdown(
    """
    **CSE303 / BYM303 – Algorithm Analysis Course Project**  
    **Energy, Time and Memory Complexity Analysis of Dynamic Programming Algorithms**
    """
)

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

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

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
        st.metric("Max Memory Diff (KB)", int(df["memory_diff_kb"].max()))

    with c4:
        st.metric("Max Energy (kWh)", f"{df['energy_kwh'].max():.2e}")

else:
    st.warning("No results.csv found. Run experiments first.")

st.divider()

# -------------------------------------------------
# PLOTS
# -------------------------------------------------
st.header("📈 Visual Analysis")

show_plot("time_vs_vertices.png", "Execution Time vs Number of Vertices")
show_plot("cpu_vs_vertices.png", "CPU Time vs Number of Vertices")
show_plot("memory_vs_vertices.png", "Net Memory Usage vs Number of Vertices")
show_plot("energy_vs_vertices.png", "Energy Consumption vs Number of Vertices")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption(
    "Algorithm Analysis Project – Energy Complexity | Dynamic Programming | 2025"
)

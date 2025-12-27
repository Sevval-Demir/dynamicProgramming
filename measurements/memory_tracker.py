import tracemalloc

def measure_peak_memory(func, *args, **kwargs):
    """
    Algoritma çalışırken ulaşılan
    maksimum bellek kullanımını (KB) ölçer.
    """
    tracemalloc.start()

    result = func(*args, **kwargs)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_memory_kb = peak / 1024  # byte → KB

    return {
        "result": result,
        "peak_memory_kb": peak_memory_kb
    }

from codecarbon import EmissionsTracker
from codecarbon.output_methods.metrics.metric_docs import emissions_doc


from codecarbon import EmissionsTracker

def measure_with_codecarbon(func, *args, **kwargs):
    tracker = EmissionsTracker(
        project_name="dynamic_programming_energy",
        measure_power_secs=1,
        log_level="error",
        save_to_file=False
    )

    tracker.start()
    result = func(*args, **kwargs)
    emissions_kg = tracker.stop()   # SADECE BİR KEZ

    return {
        "emissions_kg": emissions_kg,
        "result": result
    }



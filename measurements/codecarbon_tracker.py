from codecarbon import EmissionsTracker

def measure_with_codecarbon(func, *args, **kwargs):
    """
    Verilen fonksiyonun çalışması sırasında
    CO2 emisyonunu ölçer (kg cinsinden).
    """

    tracker = EmissionsTracker(
        project_name="dynamic_programming_energy",
        measure_power_secs=1,
        log_level="error",
        save_to_file=False
    )

    tracker.start()
    result = func(*args, **kwargs)
    emissions_kg = tracker.stop()

    return {
        "emissions_kg": emissions_kg,
        "result": result
    }

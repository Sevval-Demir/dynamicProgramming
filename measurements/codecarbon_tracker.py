from codecarbon import EmissionsTracker
from codecarbon.output_methods.metrics.metric_docs import emissions_doc


def measure_with_codecarbon(func,*args,**kwargs):
    """
    Verilen fonksiyonun enerji tüketimini codecarbon ile ölçer
    return:
    emissions_kg : co2 eşdeğeri(kg)
    energy_kwh : tahmini enerji tüketimi (kWh)
    result . fonksiyon sonucu
    """
    tracker = EmissionsTracker(
        project_name="dynamic_programming_energy",
        measure_power_secs=1,
        log_level="error",
        save_to_file=False
    )

    tracker.start()
    result=func(*args,**kwargs)
    emissions_data=tracker.stop()

    energy_kwh = tracker.stop()

    return {
        "energy_kwh": energy_kwh,
        "result": result
    }



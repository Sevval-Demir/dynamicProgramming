import psutil
import os


def measure_energy():
    #Mevcut python süreci alınır
    process=psutil.Process(os.getpid())
    #CPU kullanım süreleri
    cpu_times=process.cpu_times()
    #Bellek kullanımı
    memory=process.memory_info().rss #byte ile

    return {
        "cpu_time_sec":cpu_times.user+cpu_times.system,
        "memory_kb":memory / 1024
    }
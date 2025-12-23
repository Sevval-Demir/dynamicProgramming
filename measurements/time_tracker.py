import time
#Verilen fonksiyonun çalışma süresini ölçer.
def measure_time(func,*args,**kwargs):
    #Yüksek hassasiyetli zaman ölçümü başlatılır
    start=time.perf_counter()
    #Algoritma çalıştırılır
    result=func(*args,**kwargs)
    #Zaman ölçümü bitirilir
    end=time.perf_counter()

    return{
        "time_sec":end-start,
        "result":result
    }
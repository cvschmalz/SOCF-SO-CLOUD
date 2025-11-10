from flask import Flask

import os
import psutil
import platform
import json

APP = Flask(__name__)

# CPU usage per core
print("CPU:", psutil.cpu_percent(percpu=True)[0], "%")
cpu = psutil.cpu_percent(percpu=True)[0] + " %"

# Mem (MB)
print("Memória usada:", psutil.virtual_memory().used // 1024 ** 2, "MB")
mem = psutil.virtual_memory().used // 1024 ** 2 + " MB"

# Get process PID
print(os.getpid())
pid = os.getpid()

# OS
print("Sistema operacional:", platform.platform())
current_os = platform.platform()

@APP.get("/info")
def info():
    return json.dumps([
        {
            'integrantes': [
                'Christine von Schmalz'
            ]
        }
    ])

@APP.get("/metricas")
def metricas(cpu, mem, pid, current_os):
    return json.dumps([
        {
            "PID": pid,
            "CPU": cpu,
            "Memória usada": mem,
            "Sistema operacional": current_os
        }
    ])
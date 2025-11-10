from flask import Flask

import os
import psutil
import platform
import json

APP = Flask(__name__)

@APP.get("/info")
def info():
    return json.dumps([
        {
            'integrantes': [
                'Christine von Schmalz',
                'Cecília Lucchesi Mardegan',
                'Erick Maestri de Souza'
            ]
        }
    ])

@APP.route("/metricas")
def metricas():
    process = psutil.Process(os.getpid())
    cpu_usage = psutil.cpu_percent(interval=0.1)
    mem_usage = process.memory_info().rss / (1024 * 1024)
    pid = process.pid
    current_os = platform.system() + " (" + platform.release() + ")"

    return json.dumps({
        "PID": pid,
        "Memoria usada": f"{mem_usage:.2f} MB",
        "CPU": f"{cpu_usage:.2f}%",
        "Sistema Operacional": current_os
    })

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
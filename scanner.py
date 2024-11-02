from flask import Flask, render_template
import os
import time
from datetime import datetime, timedelta

app = Flask(__name__)

# Lista de IPs a escanear
ips = ["192.168.1.254", "192.168.1.73", 
       "140.10.0.146","192.168.1.78","192.168.1.58"]

# Diccionario para almacenar el estado de cada IP y el último tiempo activo
ip_status = {ip: {'status': 'inactive', 'last_active': None} for ip in ips}

# Función para hacer ping a una IP y actualizar el estado en el diccionario
def ping_ip(ip):
    response = os.system(f"ping -c 1 -w2 {ip} > /dev/null 2>&1")
    if response == 0:
        ip_status[ip]['status'] = 'active'
        ip_status[ip]['last_active'] = datetime.now()
    else:
        # Si ya no responde, se actualiza a inactivo si ha pasado el tiempo
        if ip_status[ip]['last_active'] and datetime.now() - ip_status[ip]['last_active'] > timedelta(minutes=2):
            ip_status[ip]['status'] = 'inactive'

# Ruta principal
@app.route('/')
def network_scan():
    # Escanear las IPs
    for ip in ips:
        ping_ip(ip)
    
    # Filtrar los dispositivos activos en los últimos 2 minutos
    two_minutes_ago = datetime.now() - timedelta(minutes=2)
    active_ips = {
        ip: data for ip, data in ip_status.items()
        if data['status'] == 'active' and data['last_active'] >= two_minutes_ago
    }
    
    # Ordenar por última actividad
    active_ips = dict(sorted(active_ips.items(), key=lambda item: item[1]['last_active'], reverse=True))

    return render_template('index.html', active_ips=active_ips, ip_status=ip_status)

if __name__ == '__main__':
    app.run(debug=True)

import os
import platform
import ipaddress
from flask import Flask, render_template, request, flash
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para mostrar mensajes de flash

# Variables para almacenar el estado de las IPs
ip_status_storage = {}
previous_active_ips = set()

# Función para hacer ping a una IP
def ping_ip(ip):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    command = f"ping {param} -w 2 {ip}"
    response = os.system(command)
    return ip, response == 0  # Retornar la IP y su estado (True/False)

# Función para escanear una red basada en el rango CIDR
def scan_network(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        ip_status = {}
        
        # Usar ThreadPoolExecutor para hacer ping en paralelo
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = {executor.submit(ping_ip, str(ip)): str(ip) for ip in network.hosts()}
            for future in as_completed(futures):
                ip, status = future.result()
                ip_status[ip] = "active" if status else "inactive"
        
        return ip_status
    except ValueError:
        flash("Rango de IP inválido")
        return {}

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def network_scan():
    global previous_active_ips
    if request.method == 'POST':
        cidr = request.form.get('cidr')
        
        if cidr:
            current_ip_status = scan_network(cidr)  # Escanear la red y actualizar el estado
            
            # Filtrar las IPs activas e inactivas
            active_ips = {ip: status for ip, status in current_ip_status.items() if status == "active"}
            inactive_ips = {ip: status for ip, status in current_ip_status.items() if status == "inactive"}
            
            # Verificar si hay alguna IP que estaba activa y ahora está inactiva
            disconnected_ips = previous_active_ips - set(active_ips.keys())
            previous_active_ips = set(active_ips.keys())  # Actualizar las IPs activas

            # Solo se mostrará la IP que se ha desconectado
            if disconnected_ips:
                inactive_ips = {ip: "inactive" for ip in disconnected_ips}
            else:
                inactive_ips = {}

        else:
            flash('Por favor, ingrese un rango CIDR válido.')
            active_ips = {}
            inactive_ips = {}

    else:
        active_ips = {}
        inactive_ips = {}

    return render_template('index.html', active_ips=active_ips, inactive_ips=inactive_ips)

if __name__ == '__main__':
    app.run(debug=True)

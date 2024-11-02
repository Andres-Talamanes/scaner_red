# Network Scanner

Este proyecto es una aplicación de escaneo de red que permite monitorear el estado de conexión de dispositivos en una red local. Utilizando Python y Flask, el sistema verifica cuáles dispositivos están activos o inactivos, mostrando los dispositivos activos en los últimos 2 minutos en una interfaz web sencilla. Los dispositivos activos se destacan en verde, y los inactivos en gris, ofreciendo una visualización clara y en tiempo real del estado de la red.

## Índice

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Estructura de Archivos](#estructura-de-archivos)

## Características

- **Monitoreo de Dispositivos**: Identificación de dispositivos activos o inactivos en una red local mediante `ping`.
- **Visualización en tiempo real**: Página web que muestra en verde los dispositivos activos y en gris los inactivos.
- **Filtro de actividad reciente**: Muestra solo los dispositivos que estuvieron activos en los últimos 2 minutos, resaltando los cambios recientes.
- **Interfaz intuitiva**: Basada en Flask, con una estructura simple y amigable para todos los usuarios.

## Tecnologías Utilizadas

- **Python**: Para la lógica del escáner de red y la gestión de conexiones.
- **Flask**: Framework web que permite crear y servir la interfaz de usuario.
- **HTML & CSS**: Para construir y estilizar la interfaz de la página.

## Requisitos

Asegúrate de tener las siguientes herramientas instaladas:

- **Python 3.x**
- **Flask** (puedes instalarlo con `pip install flask`)

## Configuración

1. Clona el repositorio o descarga los archivos en tu máquina.
2. Instala las dependencias con:
   ```
   pip install flask
   ```
3. Configura las direcciones IP que deseas escanear en el archivo scanner.py:
```
ips = ["192.168.1.254", "192.168.1.73"]
```

## Ejecución
Para iniciar el escáner de red, ejecuta el siguiente comando en la terminal:

```
python3 scanner.py
```

Esto iniciará un servidor local de Flask. Abre tu navegador y dirígete a http://127.0.0.1:5000 para ver la interfaz de monitoreo de red.

## Estructura de Archivos
1. scanner.py: Contiene la lógica principal de escaneo y el servidor Flask.
2. templates/index.html: La plantilla HTML que define la interfaz del usuario.
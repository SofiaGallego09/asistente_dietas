import os
import subprocess

app_path = os.path.join("asistente_dietas", "app.py")

if not os.path.exists(app_path):
    print(" No se encontró el archivo app.py. Verifica la ruta.")
else:
    print("Iniciando NutriSmart...\n")
    print(" Cuando veas el mensaje 'Running on http://127.0.0.1:5000', abre ese enlace en tu navegador.\n")
    subprocess.run(["python", app_path])

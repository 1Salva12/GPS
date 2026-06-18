Proyecto GPS Autómatas

Cómo ejecutar en PowerShell:

1. Entra a la carpeta del proyecto.
2. Crea entorno virtual si no existe:
   python -m venv .venv
3. Actívalo:
   .\.venv\Scripts\Activate.ps1
4. Instala dependencias:
   pip install -r requirements.txt
5. Configura las variables de entorno necesarias (ver ejemplo en .env.example):
   set GOOGLE_API_KEY=tu_clave_de_google
   set PRECIO_GASOLINA=23.99
   set PRECIO_DIESEL=24.58
6. Ejecuta:
   python app.py
7. Abre:
   http://127.0.0.1:5000

Despliegue en Vercel:
1. Sube este repositorio a GitHub.
2. Crea un proyecto en Vercel y conecta el repositorio.
3. En Settings > Environment Variables añade:
   - GOOGLE_API_KEY
   - PRECIO_GASOLINA
   - PRECIO_DIESEL
4. Haz deploy.

Pruebas rápidas:
- Origen: Jilotepec
- Destino: CDMX
- Origen: Jilotepec
- Destino: Querétaro
- Origen: Jilotepec
- Destino: San Juan del Río

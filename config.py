import os

# ─────────────────────────────────────────────
#  CONFIGURACIÓN GENERAL
#  Las claves sensibles deben configurarse en el entorno del despliegue.
#  En Windows: set GOOGLE_API_KEY=tu_clave
#  En Mac/Linux: export GOOGLE_API_KEY=tu_clave
# ─────────────────────────────────────────────
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "").strip()

# Precios combustible en MXN por litro (actualiza según PEMEX)
PRECIO_GASOLINA = float(os.environ.get("PRECIO_GASOLINA", "23.99"))
PRECIO_DIESEL   = float(os.environ.get("PRECIO_DIESEL",   "24.58"))

if not GOOGLE_API_KEY:
    import warnings
    warnings.warn(
        "⚠️  GOOGLE_API_KEY no está definida. "
        "Define la variable de entorno antes de iniciar la app o del despliegue.",
        RuntimeWarning
    )

# Velocidad promedio por tipo de carretera (km/h) — para estimación de tiempo
VELOCIDAD_PROMEDIO = {
    "autopista":  110,
    "carretera":   80,
    "ciudad":      40,
    "default":     60,
}
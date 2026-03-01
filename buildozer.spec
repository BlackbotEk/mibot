[app]
# (Puntos básicos)
title = SAETA_Bot
package.name = saetabot
package.domain = org.saeta
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 1.0.0

# REQUISITOS: Se añade pyjnius para que Python controle funciones de Android
requirements = python3,kivy,android,pyjnius

orientation = portrait
fullscreen = 0

# PERMISOS MAESTROS: Necesarios para el Panel Flotante y Lectura de Pantalla
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, BIND_ACCESSIBILITY_SERVICE, WRITE_EXTERNAL_STORAGE, FOREGROUND_SERVICE

# ACEPTAR LICENCIAS AUTOMÁTICAMENTE (Evita errores en GitHub Actions)
android.accept_sdk_license = True

# CONFIGURACIÓN DE ANDROID
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

# --- CONFIGURACIÓN CRÍTICA PARA EL BOT INVISIBLE ---

# 1. Declara el servicio de accesibilidad para que aparezca en Ajustes del celular
android.services = accessibility_service:MyAccessibilityService.py

# 2. Configura los metadatos para que Android sepa que el bot puede hacer clics y leer texto
android.meta_data = android.accessibilityservice=xml/accessibility_service_config

# 3. Permite que la app dibuje sobre otras (Overlay del Panel)
android.manifest.intent_filters = [("org.saeta.saetabot.MyAccessibilityService", "android.accessibilityservice.AccessibilityService")]

[buildozer]
log_level = 2
warn_on_root = 1

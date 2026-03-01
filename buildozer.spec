[app]
# (Puntos básicos)
title = SAETA_Bot
package.name = saetabot
package.domain = org.saeta
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 1.0.0

# REQUISITOS CORREGIDOS: Removido pyjnius que causa problemas
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# PERMISOS: Necesarios para el Panel Flotante y Lectura de Pantalla
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, BIND_ACCESSIBILITY_SERVICE, WRITE_EXTERNAL_STORAGE, FOREGROUND_SERVICE

# ACEPTAR LICENCIAS AUTOMÁTICAMENTE
android.accept_sdk_license = True

# CONFIGURACIÓN DE ANDROID
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

# CONFIGURACIÓN PARA EL BOT

# 1. Declara el servicio de accesibilidad
android.services = MyAccessibilityService

# 2. Configuración de metadatos
android.meta_data = android.accessibilityservice=xml/accessibility_service_config

[buildozer]
log_level = 2
warn_on_root = 1
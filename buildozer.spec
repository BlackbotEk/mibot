[app]
# (Puntos básicos)
title = SAETA_Bot
package.name = saetabot
package.domain = org.saeta
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 1.0.0

# REQUISITOS: Solo lo necesario para Kivy y Android
requirements = python3,kivy,android

orientation = portrait
fullscreen = 0

# PERMISOS: Reducidos a lo esencial
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# ACEPTAR LICENCIAS AUTOMÁTICAMENTE
android.accept_sdk_license = True

# CONFIGURACIÓN DE ANDROID
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

# META-DATOS
android.gradle_dependencies = 

[buildozer]
log_level = 2
warn_on_root = 1

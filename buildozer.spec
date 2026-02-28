[app]
title = SAETA_Bot
package.name = saetabot
package.domain = org.saeta
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# REQUISITOS CRÍTICOS: Se añade jnius para comunicar Python con Java (Android)
requirements = python3,kivy,android,pyjnius

orientation = portrait
fullscreen = 0

# PERMISOS PARA BOT: Internet, Dibujar sobre apps y Almacenamiento
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, BIND_ACCESSIBILITY_SERVICE, WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1


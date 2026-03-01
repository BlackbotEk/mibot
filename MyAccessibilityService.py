from jnius import autoclass, cast
from android.runnable import run_on_ui_thread

PythonService = autoclass('org.renpy.android.PythonService')
service = PythonService.mService

class MyAccessibilityService:
    def __init__(self):
        self.enabled = False
    
    def on_service_connected(self):
        print("Servicio de Accesibilidad Conectado")
        self.enabled = True
    
    def on_service_disconnected(self):
        print("Servicio de Accesibilidad Desconectado")
        self.enabled = False

# Instancia global
accessibility_service = MyAccessibilityService()
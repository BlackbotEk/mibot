from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class SaetaPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Titulo del Bot
        self.add_widget(Label(text='SAETA BOT INVISIBLE', font_size='22sp', color=(0, 1, 0, 1), bold=True))

        # Configuracion de Velocidad
        self.add_widget(Label(text='VELOCIDAD (1:Ninja | 4:Sniper)'))
        self.modo_reaccion = Slider(min=1, max=4, value=4, step=1)
        self.add_widget(self.modo_reaccion)

        # Filtro de Rentabilidad
        self.add_widget(Label(text='MIN. PRECIO POR KM ($)'))
        self.precio_km = Slider(min=0.5, max=5.0, value=1.5, step=0.1)
        self.add_widget(self.precio_km)

        # Boton de Inicio
        self.btn_start = Button(text='ACTIVAR ESCANER', background_color=(0, 0.7, 0, 1), font_size='20sp')
        self.btn_start.bind(on_press=self.run_bot)
        self.add_widget(self.btn_start)

    def run_bot(self, instance):
        print(f"Buscando viajes... Modo: {self.modo_reaccion.value} | MIN: ${self.precio_km.value}/km")
        instance.text = "BUSCANDO VIAJES..."
        instance.background_color = (0.7, 0.7, 0.1, 1)

class SaetaApp(App):
    def build(self):
        return SaetaPanel()

if __name__ == '__main__':
    SaetaApp().run()

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inicializar la aplicación de Firebase
cred = credentials.Certificate("")
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})

ref = db.reference('/Devices')
print(ref)

def cambiar_valor_clave(nombre_clave):
    resultado = ref.get()
    valor_actual = resultado[nombre_clave]
    nuevo_valor = not valor_actual
    ref.update({nombre_clave: nuevo_valor})
    print(f"Se cambió el valor de {nombre_clave} a {nuevo_valor}")
    return None

class Ui(ScreenManager):
    def button_pressed(self, button_id):
        names = ["Desk Lights", "Central Lights", "Room Lights", "Speaker", "LEDs RGB", "PC", "3D Printer", "AAC"]
        nombre_clave = names[button_id]
        resultado = ref.get()
        valor_actual = resultado[nombre_clave]
        nuevo_valor = not valor_actual
        ref.update({nombre_clave: nuevo_valor})
        return None

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_string('''
<ui>:
    MDScreen:
        name: "screen_principal"
        md_bg_color: 80/255, 0/255, 130/255, 0.5
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint: 1, 0.2
                orientation: "horizontal"
                padding: "10dp"
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    line_color: 1,0,1,1
                    MDLabel:
                        text: "APLICACION DE TECNOLOGIA"
                        halign : "center"
                        pos_hint: {"center_y": 0.5}
                    MDSwitch:
                        pos_hint: {"center_y": 0.5}
                        on_active: 
                            app.change_style(*args)
            MDGridLayout:
                cols: 4
                size_hint: 1, .5
                padding: ["10dp","10dp","10dp","10dp"]
                spacing: "10dp"
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image1.png'
                        background_down: 'image1.png'    
                        on_release: root.button_pressed(6)
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image2.png'
                        background_down: 'image2.png' 
                        on_release: root.button_pressed(7)
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image3.png'
                        background_down: 'image3.png' 
                        on_release: root.button_pressed(1)
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image4.png'
                        background_down: 'image4.png' 
                        on_release: root.button_pressed(2)
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image5.png'
                        background_down: 'image5.png' 
                        on_release: root.button_pressed(4)
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image6.png'
                        background_down: 'image6.png' 
                        on_release: root.button_pressed(5)
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image7.png'
                        background_down: 'image7.png' 
                        on_release: root.button_pressed(0)
                MDCard:
                    radius: "10dp"
                    padding: "20dp"
                    Button:
                        size_hint: 1, 1
                        background_normal: 'image8.png'
                        background_down: 'image8.png' 
                        on_release: root.button_pressed(3)''')
        return Ui()
    
    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style = "Light"
        else:            
            self.theme_cls.theme_style = "Dark"

if __name__=="__main__":
    MainApp().run()

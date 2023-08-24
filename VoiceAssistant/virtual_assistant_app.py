import speech_recognition as speech
import pyttsx3
import pywhatkit
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random

#Base de datos 
# Inicializar la aplicación de Firebase
cred = credentials.Certificate("")
firebase_admin.initialize_app(cred, {'databaseURL': ''})

ref = db.reference('/Devices')

def cambiar_valor_clave(nombre_clave):
    resultado = ref.get()
    valor_actual = resultado[nombre_clave]
    nuevo_valor = not valor_actual
    ref.update({nombre_clave: nuevo_valor})
    print(f"Se cambió el valor de {nombre_clave} a {nuevo_valor}")
    return None

# Nombre del asistente
name='luna'

# Permite reconocer la voz
listener = speech.Recognizer()

engine = pyttsx3.init()

"""RATE DEL ASISTENTE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 165)

"""VOZ DEL ASISTENTE"""
voice_engine = engine.getProperty('voices')
engine.setProperty('voice', voice_engine[0].id)

# Selecciona una palabra de forma aleatoria
def random_choice():
    lista = ['Te escucho', 'Dime tu orden', 'Estoy escuchándote', 'Dime']
    seleccion = random.choice(lista)
    return seleccion

# Meotodo que permite al asistente hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Metodo que ejecuta al asistente
def run():
    try:
        with speech.Microphone() as source:
            voice = listener.listen(source, timeout=4)
            recognizer = listener.recognize_google(voice, language='es-MX')
            recognizer = recognizer.lower()
            print(recognizer)
            orden = recognizer
            if "enciende" in recognizer:
                dispositivos = ["escritorio","centrales","luces","parlante","leds","computadora","impresora","aire"]
                coincidencia = list(set(list(orden.split(" "))) & set(dispositivos))
                names = ["Desk Lights", "Central Lights", "Room Lights", "Speaker", "LEDs RGB", "PC", "3D Printer", "AAC"]
                resultado = ref.get()
                valor_actual = resultado[names[dispositivos.index(coincidencia[0])]]
                if valor_actual==False:
                    ref.update({names[dispositivos.index(coincidencia[0])]: True})
                else:
                    talk('Ya esta encendido')
            elif "apaga" in recognizer:
                dispositivos = ["escritorio","centrales","luces","parlante","leds","computadora","impresora","aire"]
                coincidencia = list(set(list(orden.split(" "))) & set(dispositivos))
                names = ["Desk Lights", "Central Lights", "Room Lights", "Speaker", "LEDs RGB", "PC", "3D Printer", "AAC"]
                resultado = ref.get()
                valor_actual = resultado[names[dispositivos.index(coincidencia[0])]]
                if valor_actual==True:
                    ref.update({names[dispositivos.index(coincidencia[0])]: False})
                else:
                    talk('Ya esta apagado')

            else:
                pass
    except:
        engine.stop()
        pass
        
    
def main():
    while True:
        try:
            with speech.Microphone() as source:
                print('Escuchando...')
                voice = listener.listen(source, timeout=5)
                recognizer = listener.recognize_google(voice, language='es-MX')
                recognizer = recognizer.lower()
                if name in recognizer:
                    talk(random_choice())
                    run()
        except:
            pass

if __name__ == "__main__":
    main()

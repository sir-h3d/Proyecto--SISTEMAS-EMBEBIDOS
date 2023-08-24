import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

bot = telebot.TeleBot("")
cred = credentials.Certificate("")
firebase_admin.initialize_app(cred, {'databaseURL': ''})
ref = db.reference('/')

@bot.message_handler()
def handle_command(message):
    command = message.text.lower()  # Obtener el comando en minúsculas
    dispositivos = ["escritorio", "centrales", "luces", "parlante", "leds", "computadora", "impresora", "aire"]
    names = ["Desk Lights", "Central Lights", "Room Lights", "Speaker", "LEDs RGB", "PC", "3D Printer", "AAC"]
    entrada = command.split(" ")
    if len(entrada)>1:
        commando = entrada[0]
        dispositivo = entrada[1]
        dispositivos = ["escritorio","centrales","luces","parlante","leds","computadora","impresora","aire"] 
        if dispositivo in dispositivos:
            pos = dispositivos.index(dispositivo)
            if "enciende"==commando:
                resultado = ref.get()
                valor_actual = resultado[names[pos]]
                if valor_actual==False:
                    ref.update({names[pos]: True})
                    bot.reply_to(message, f"Encendiendo {dispositivo}")
                else:
                    bot.reply_to(message, f"Ya esta encendido")
            elif "apaga"==commando:
                resultado = ref.get()
                valor_actual = resultado[names[pos]]
                if valor_actual==True:
                    ref.update({names[pos]: False})
                    bot.reply_to(message, f"Apagando {dispositivo}")
                else:
                    bot.reply_to(message, f"Ya esta apagado")
        else:
            bot.reply_to(message, "Dispositivo no registrado.")
    if command=="dispositivos":
        cadena = ""
        resultado = ref.get()
        for i in range(len(dispositivos)):
            estado = resultado[names[i]]
            if estado== False:
                estado = "Apagado"
            else:
                estado = "Encendido"
            cadena += f"{i+1}.- {dispositivos[i]}: {estado}\n"
        bot.reply_to(message, cadena)
if __name__ == "__main__":
    bot.polling(none_stop=True)

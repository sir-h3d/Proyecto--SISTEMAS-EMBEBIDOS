# Proyecto ESP32 con Control de Relés y Firebase

Este proyecto se basa en el uso de una ESP32 para controlar una serie de relés en función de los datos almacenados en Firebase. También integra una serie de interfaces para controlar estos dispositivos, incluyendo un bot de Telegram, una asistente de voz, una aplicación para dispositivos Wear OS y una interfaz grafica en python.

## Descripción

El proyecto utiliza una ESP32 para leer datos desde Firebase y controlar relés en función de estos datos. Los dispositivos pueden ser controlados a través de varios medios, como un bot de Telegram, una asistente de voz y una aplicación de Wear OS.

## Funcionalidades

- La ESP32 se conecta a Firebase para leer datos de estado de dispositivos.
- Los relés se controlan en tiempo real en función de los datos de Firebase.
- Un bot de Telegram permite el control de los dispositivos a través de comandos.
- Una asistente de voz permite controlar los dispositivos mediante comandos de voz.
- Una aplicación para dispositivos Wear OS proporciona una interfaz de control sencilla.

## Configuración del Hardware

Asegúrate de conectar correctamente la ESP32 a los relés y configurar los pines GPIO según tus necesidades. También debes asegurarte de tener una conexión activa a Internet para que la ESP32 pueda comunicarse con Firebase.

## Configuración de Firebase

1. Crea un proyecto en Firebase y configura una base de datos en tiempo real.
2. Obtén el archivo de configuración JSON de Firebase y colócalo en la carpeta de tu proyecto.
3. Configura las credenciales en el código de la ESP32 y en el codigo de la interfaz uqe vayas a utilizar para controlar los estados de los dispositivos.

## Requisitos Previos
1. Una placa ESP32 debidamente configurada y conectada.
2. Acceso a Internet para que la ESP32 pueda comunicarse con Firebase.
3. Instalacion de los programas necesarios para modificar y desplegar el codigo (En mi caso Android Studio, Python 3.11)
4. Instalación de las bibliotecas necesarias en tu entorno de desarrollo.
5. Para el uso de la aplicacion de WearOs, es necesario clonar el siguiente repositorio "git clone https://github.com/android/codelab-compose-for-wear-os.git
cd compose-for-wear-os" y luego reemplazar los archivos almacenados el la carpeta de WearOSApp de este repositorio

## Instalación
1. Clona o descarga este repositorio a tu entorno de desarrollo.
2. Asegúrate de tener el IDE de Arduino configurado para trabajar con la ESP32 o tambien se puede utilizar PlatformIO en el caso de Visual Studio Code.
4. Configura los pines GPIO según tu hardware.
5. Carga el programa en tu ESP32.
6. Acondiciona la interfaz a utilizar a tu gusto

## Uso
Puedes controlar los dispositivos de la siguiente manera:
1. Bot de Telegram: Envía comandos al bot de Telegram para controlar los dispositivos. Consulta la documentación del bot para conocer los comandos disponibles.
2. Asistente de Voz: Utiliza comandos de voz para controlar los dispositivos. Asegúrate de tener el entorno adecuado configurado.
3. Aplicación Wear OS: Instala la aplicación en tu dispositivo Wear OS y utiliza la interfaz de control para gestionar los dispositivos.
4. Interfaz grafica en Python: Puedes encender y apagar los dispositivos solo dando click en el icono correspondiente. 

Autor: Henry De la torre

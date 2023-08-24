#include <Arduino.h>
#include <WiFi.h>
#include <FirebaseESP32.h>
#include <ArduinoJson.h>

#define DEVICE_UID "1X"
#define WIFI_SSID1 ""
#define WIFI_PASSWORD1 ""
#define API_KEY ""
#define DATABASE_URL ""

FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;
FirebaseJson json;

void Wifi_Init() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID1,WIFI_PASSWORD1);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
  digitalWrite(2,HIGH);   
}

void firebase_init() {
  // Configure Firebase API Key
  config.api_key = API_KEY;
  // Configure Firebase Realtime Database URL
  config.database_url = DATABASE_URL;
  // Enable WiFi reconnection
  Firebase.reconnectWiFi(true);
  // Sign in to Firebase Anonymously
  if (Firebase.signUp(&config, &auth, "", "")) {
    Serial.println("Successful connection to Firebase");
  } else {
    Serial.printf("Failed, %s\n", config.signer.signupError.message.c_str());
  }
  // Initialize the Firebase library
  Firebase.begin(&config, &auth);
}

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(14, OUTPUT);
  pinMode(27, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(33, OUTPUT);
  pinMode(32, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(2, OUTPUT);
  Wifi_Init();
  firebase_init();
}

void read_data() {
  StaticJsonDocument<200> pines;
  pines["3D Printer"] = 33;
  pines["AAC"] = 32;
  pines["Central Lights"] = 12;
  pines["Desk Lights"] = 13;
  pines["LEDs RGB"] = 26;
  pines["PC"] = 25;
  pines["Room Lights"] = 14;
  pines["Speaker"] = 27;
  if (Firebase.ready()) {
    if (Firebase.getJSON(fbdo, "/Devices", &json)) {
  DynamicJsonDocument doc(1024);
  String diccionario;
  json.toString(diccionario);
  DeserializationError error = deserializeJson(doc,diccionario);
  if (error) {
    Serial.println("Error al analizar el JSON");
    return;
  }
  for (JsonPair kvp : doc.as<JsonObject>()) {
    String clave = kvp.key().c_str();
    bool estado = kvp.value().as<bool>();
    if (!(estado==digitalRead(pines[clave]))){
      digitalWrite(pines[clave],estado);   
    }
  }
} else {
  Serial.printf("Error al obtener el JSON de los dispositivos: %s\n", fbdo.errorReason().c_str());
}
  }
}

void loop() {
  read_data();
  delay(100);
}

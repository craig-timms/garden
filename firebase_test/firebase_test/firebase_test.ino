
//Required HTTPClientESP32Ex library to be installed  https://github.com/mobizt/HTTPClientESP32Ex

#include <WiFi.h>
#include "FirebaseESP32.h"
#include "passwords.h"

//Define Firebase Data objects
FirebaseData firebaseData1;
FirebaseData firebaseData2;
FirebaseData firebaseData3;

const int ledPin =  19; //GPIO19 for LED
const int swPin =  18; //GPIO18 for Switch
bool swState = false;
String path = "/moisture";
String nodeID = "sensor_1"; //This is this node ID to receive control
String otherNodeID = "sensor_2"; //This is other node ID to control

const int adcMS1 = 34; 
const int adcMS2 = 35;
int valMS1 = 1;
int valMS2 = 2;

unsigned long postTimer = 0;
unsigned long postPeriod = 2000;

void streamCallback(StreamData data)
{

  if (data.dataType() == "boolean") {
    if (data.boolData())
      Serial.println("Set " + nodeID + " to High");
    else
      Serial.println("Set " + nodeID + " to Low");
    digitalWrite(ledPin, data.boolData());
  }


}


void streamTimeoutCallback(bool timeout)
{
  if (timeout)
  {
    Serial.println();
    Serial.println("Stream timeout, resume streaming...");
    Serial.println();
  }
}


void setup()
{

  Serial.begin(115200);

  pinMode(ledPin, OUTPUT);
  pinMode(swPin, INPUT);

  Serial.println();
  Serial.println();

  postTimer = millis();

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);



  if (!Firebase.beginStream(firebaseData1, path + "/" + nodeID))
  {
    Serial.println("Could not begin stream");
    Serial.println("REASON: " + firebaseData1.errorReason());
    Serial.println();
  }

  Firebase.setStreamCallback(firebaseData1, streamCallback, streamTimeoutCallback);

}

void loop()
{
  if ( millis() > postTimer + postPeriod ) { 
    valMS1 = analogRead(adcMS1);
    valMS2 = analogRead(adcMS2);
    Serial.print("Sensor 1: ");
    Serial.print(valMS1);
    Serial.print("    Sensor 2: ");
    Serial.print(valMS2);
    Serial.println();

    if (Firebase.pushInt(firebaseData1, path + "/" + nodeID, valMS1)) {
      Serial.println("Set " + nodeID + " to " + valMS1);
      delay(10);
    }
    
    if (Firebase.pushInt(firebaseData2, path + "/" + otherNodeID, valMS2)) {
      Serial.println("Set " + otherNodeID + " to " + valMS2);
      delay(10);
    }
    
    if (Firebase.pushTimestamp(firebaseData3, path + "/Timestamp")) {
//      Serial.print("TIMESTAMP (Seconds): ");
//      Serial.println(firebaseData1.intData());
        printf("TIMESTAMP (milliSeconds): %.0lf\n", firebaseData1.doubleData());
        delay(10);
    }
    
    postTimer = millis();
  }
  
//  if (digitalRead(swPin) != swState) {
//
//    bool _swState = swState;
//    swState = digitalRead(swPin);
//
//    if (Firebase.setBool(firebaseData2, path + "/" + otherNodeID, swState)) {
//      if (swState)
//        Serial.println("Set " + otherNodeID + " to High");
//      else
//        Serial.println("Set " + otherNodeID + " to Low");
//    } else {
//      swState = _swState;
//      Serial.println("Could not set " + otherNodeID);
//    }
//
//  }



}

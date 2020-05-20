#include <EspMQTTClient.h>
#include "PubSubClient.h"

void onConnectionEstablished();

EspMQTTClient client(
    "devolo-426",   //wifi ssid
    "URWGGRZLKMQFUEDN",   //wifi password
    "maqiatto.com",   //MQTT broker ip
    1883,   //MQTT broker port
    "saga.sellin@abbindustrigymnasium.se",    //MQTT username
    "MQTTPAS",    //MQTT 
    "microdator0",    //client name
    onConnectionEstablished,    //connection established callback
    true,   //enable web updater
    true    //enable debug messages

  );



#define motorPinRightDir  0//D2
#define motorPinRightSpeed 5//D1
#define motorPinLeftDir 2
#define motorPinLeftSpeed 4

void setup() {
  // put your setup code here, to run once:
  pinMode(motorPinRightDir, OUTPUT);
  pinMode(motorPinRightSpeed, OUTPUT);
  pinMode(motorPinLeftDir, OUTPUT);
  pinMode(motorPinLeftSpeed, OUTPUT);

  Serial.begin(115200);
}

void nosignal() { //a function that makes the motor stop moving and therefore the car will stop
  int dir = 0;
  int speed = 0;
  digitalWrite(motorPinRightDir, dir);
  analogWrite(motorPinRightSpeed, speed);
}

void forward() { //creates a function where the wheels will spin forward
  Serial.println("forward");
  int dir = 0;
  int speed = 1024;
  digitalWrite(motorPinRightDir, dir);
  analogWrite(motorPinRightSpeed, speed);
}

void backwards() { //creates a function where the wheels will spin backwards
  int dir = 0;
  int speed = 1024;
  digitalWrite(motorPinRightDir, 1);
  analogWrite(motorPinRightSpeed, speed);
}

void onConnectionEstablished() {
  client.subscribe("saga.sellin@abbindustrigymnasium.se/direction", [](const String &payload) {
    Serial.println(payload);
    if (payload == "0") { //if sent data is "0", the arduino program will:
      backwards(); //"tell" the motor to make the wheel spin backwards
      client.publish("saga.sellin@abbindustrigymnasium.se/standard","Motor spinning backwards"); //and this message will be published to the main topic
    }
    else if (payload == "1") { //instead, if sent data is "1", the arduino program will:
      nosignal(); //not use motor
      client.publish("saga.sellin@abbindustrigymnasium.se/standard","Motor not in use"); //and this message will be published to the main topic
    }
    else if (payload == "2") { //instead, if sent data is "2", the arduino program will:
      forward(); //"tell" the motor to make the wheel spin forward
      client.publish("saga.sellin@abbindustrigymnasium.se/standard","Motor spinning forward"); //and this message will be published to the main topic
    }
  });
}

void loop() {
  int speed = 1024;
  int dir = 0;
  client.loop(); //looping functions above
}


void Drivetest(int Dirpin, int Speedpin) {
  Serial.println("Drivetest");
  DriveDirSpeed(Dirpin, Speedpin, 0, 1020);
  delay(2200);
  DriveDirSpeed(Dirpin, Speedpin, 1, 1020);

}


void Drivetest2(int Dirpin, int Speedpin) {
  Serial.println("Drivetest 2");
  int Speed = 0;
  while (Speed < 1020)
  {
    Speed += 100;
    DriveDirSpeed(Dirpin, Speedpin, 0, Speed);
    delay(2200);
  }

}

void Drivetest3(int Dirpin, int Speedpin) {
  Serial.println("Drivetest 3");
  int Direction = 0;
  while (Direction <= 1)
  {
    int Speed = 0;
    while (Speed < 1020)
    {
      Speed += 100;
      DriveDirSpeed(Dirpin, Speedpin, Direction, Speed);
      delay(2200);
    }
    Direction++;
  }

}


void DriveDirSpeed(int Dirpin, int Speedpin, int Direction, int Speed) {
  Serial.println("DriveDirSpeed");
  if (Direction == 1)
    Serial.println("Framåt");
  else
    Serial.println("Bakåt");

  Serial.println("Hastighet: " + String(Speed));

  digitalWrite(Dirpin, Direction);
  analogWrite(Speedpin, Speed);
}

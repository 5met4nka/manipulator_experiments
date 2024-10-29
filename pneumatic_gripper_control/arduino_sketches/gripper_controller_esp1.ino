#include <WiFi.h>
#include <WebServer.h>

#define Gripperpin 12
#define Workpin 13

/* Установите здесь свои SSID и пароль */
const char* ssid = "FANUC gripper controller";  
const char* password = "01234567";  
/* Настройки IP адреса */
IPAddress local_ip(192,168,2,1);
IPAddress gateway(192,168,2,1);
IPAddress subnet(255,255,255,0);
WebServer server(80);


bool Gripperstatus = LOW;

void setup() {
  Serial.begin(115200);
  pinMode(Gripperpin, OUTPUT);
  pinMode(Workpin, OUTPUT);

  delay(1000);
  digitalWrite(Workpin, HIGH);

  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  delay(100);
  server.on("/", handle_OnConnect);
  server.on("/Gripperon", handle_Gripperon);
  server.on("/Gripperoff", handle_Gripperoff);

  server.onNotFound(handle_NotFound);
  server.begin();
  Serial.println("HTTP server started");
}
void loop() {
  server.handleClient();
  
  digitalWrite(Gripperpin, Gripperstatus);
  
}
void handle_OnConnect() {
  Gripperstatus = LOW;

  server.send(200, "text/html", SendHTML(false); 
}
void handle_Gripperon() {
  Gripperstatus = HIGH;

  server.send(200, "text/html", SendHTML(true)); 
}
void handle_Gripperoff() {
  Gripperstatus = LOW;

  server.send(200, "text/html", SendHTML(false)); 
}
void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}
String SendHTML(uint8_t Gripstat){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<meta http-equiv=\"Content-type\" content=\"text/html; charset=utf-8\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>Управление gripper</title>\n";
  ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}\n";
  ptr +=".button {display: block;width: 80px;background-color: #3498db;border: none;color: white;padding: 13px 30px;text-decoration: none;font-size: 25px;margin: 0px auto 35px;cursor: pointer;border-radius: 4px;}\n";
  ptr +=".button-on {background-color: #34495e;}\n";
  ptr +=".button-on:active {background-color: #2c3e50;}\n";
  ptr +=".button-off {background-color: #3498db;}\n";
  ptr +=".button-off:active {background-color: #2980b9;}\n";
  ptr +="p {font-size: 14px;color: #888;margin-bottom: 10px;}\n";
  ptr +="</style>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<h1>ESP32 Веб сервер</h1>\n";
  ptr +="<h3>Режим точка доступа WiFi (AP)</h3>\n";
  if(Gripstat)
  {ptr +="<a class=\"button button-off\" href=\"/Gripperoff\">CLOSE</a>\n";}
  else
  {ptr +="<a class=\"button button-on\" href=\"/Gripperon\">OPEN</a>\n";}
  
  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

const char* ssid = "Tinkerers' Lab";
const char* password = "tinker@tl";
int ledPin = 5;

ESP8266WebServer server(80);

void handleLogin(){
  String msg;
  if (server.hasHeader("Cookie")){
    String cookie = server.header("Cookie");
  }
  if (server.hasArg("DISCONNECT")){
    server.sendHeader("Location","/login");
    server.sendHeader("Cache-Control","no-cache");
    server.sendHeader("Set-Cookie","ESPSESSIONID=0");
    server.send(301);
    return;
  }
  if (server.hasArg("CHARACTER")){
    Serial.println(server.arg("CHARACTER"));
    float unsc = server.arg("CHARACTER").toFloat();
    Serial.println(unsc);
    float sound = map(unsc, -100, 100, 0, 255);
    Serial.println(sound);
    analogWrite(ledPin, sound);

    server.sendHeader("Location","/");
    server.sendHeader("Cache-Control","no-cache");
    server.sendHeader("Set-Cookie","ESPSESSIONID=1");
    server.send(301);
    return;
  }
  String content = "<html><body><form action='/login' method='POST'>";
  content += "Enter character:<input type='text' name='CHARACTER' placeholder='enter any character'><br>";
  content += "<input type='submit' name='SUBMIT' value='Submit'></form>";
  server.send(200, "text/html", content);
}

void handleRoot(){
  String header;
  String content = "<html><body><form action='/login' method='POST'>";
  content += "Enter character:<input type='text' name='CHARACTER' placeholder='enter any character'><br>";
  content += "<input type='submit' name='SUBMIT' value='Submit'></form>";
  server.send(200, "text/html", content);
}

void handleNotFound(){
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
}

void setup(void){
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());


  server.on("/", handleRoot);
  server.on("/login", handleLogin);

  server.onNotFound(handleNotFound);
  //here the list of headers to be recorded
  const char * headerkeys[] = {"User-Agent","Cookie"} ;
  size_t headerkeyssize = sizeof(headerkeys)/sizeof(char*);
  //ask server to track these headers
  server.collectHeaders(headerkeys, headerkeyssize );
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void){
  server.handleClient();
}

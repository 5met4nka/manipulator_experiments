#include <ros.h>
#include <std_msgs/Bool.h>

#define Gripperpin 4
#define Workpin 5

ros::NodeHandle nh;

void messagaCB (const std_msgs::Bool& Gripp){
  digitalWrite(Gripperpin, Gripp.data);
}

ros::Subscriber<std_msgs::Bool> sub("Gripper_control", &messagaCB );

void setup() {

  Serial.begin(115200);
  pinMode(Gripperpin, OUTPUT);
  pinMode(Workpin, OUTPUT);

  delay(1000);
  digitalWrite(Workpin, HIGH);

  nh.initNode();
  nh.subscribe(sub);

}

void loop() {
  
  nh.spinOnce();
  delay(50);

}

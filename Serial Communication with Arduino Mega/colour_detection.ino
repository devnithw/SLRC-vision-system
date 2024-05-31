void colour_detection() {
  motor1.stop();
  motor2.stop();
  delay(1000);
  bool forward = sensorValues[0] == 1 && sensorValues[1] == 1;
  while (forward) {
    sensorValues[SensorCount];
    readSensors(sensorValues);
    forward = sensorValues[0] == 1 && sensorValues[1] == 1;
    if (!forward) {
      break;
    }
    motor1.setSpeed(150);  // Set right motor speed
    motor1.forward();      // Move right motor forward
    motor2.setSpeed(150);  // Set left motor speed
    motor2.forward();      // Move left motor backward for a sharper turn
  }
  motor1.stop();
  motor2.stop();
  delay(200);
  fUltrasonic_read();
  while (fdistance > 24) {
    fUltrasonic_read();
    sensorValues[SensorCount];
    readSensors(sensorValues);
    line_follow(sensorValues);
  }
  motor1.stop();
  motor2.stop();
  delay(1000);
  digitalWrite(send_shape_request, LOW);
  digitalWrite(send_colour_request, HIGH);  

  // Wait for a response
  delay(7000);  // Delay to allow time for response

  // Check for response
  if (digitalRead(recieved_led_1) == HIGH) {  
    digitalWrite(led_green, HIGH);
    digitalWrite(led_blue, LOW);
    wall_colour = "GREEN";
    // Ensure other LED is turned off
  } else if (digitalRead(recieved_led_2) == HIGH) {  
    digitalWrite(led_blue, HIGH);
    digitalWrite(led_green, LOW);  
    wall_colour = "BLUE";
  }
  delay(1000);
}

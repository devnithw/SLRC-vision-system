void shape_detector() {
  digitalWrite(send_shape_request, HIGH);
  digitalWrite(send_colour_request, LOW);  
  digitalWrite(send_shape_request, HIGH);
  digitalWrite(send_colour_request, LOW);  

  
  delay(10000);  // Delay to allow time for response


  // Check for response
  if (digitalRead(recieved_led_1) == HIGH) {  
    digitalWrite(led_blue, HIGH);
    digitalWrite(led_green, LOW);  
  } else {                    
    digitalWrite(led_green, HIGH);
    digitalWrite(led_blue, LOW);
 
  }
}


#include <Wire.h>
#include <LiquidCrystal_I2C.h>


LiquidCrystal_I2C lcd(0x20, 16, 2);  


void setup()
{ 
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0,0);
}

void loop() 
{
  // lcd.print(analogRead(A1));
  // delay(1000);
  // lcd.clear();
    
  int a = analogRead(A0);
  int b = analogRead(A1);
  if(a < 600 && b < 400){
    lcd.print("rock");
    }

  if(a < 600 && b > 400){
    lcd.print("scissor");
  }
  if(a > 600 && b >400){
    lcd.print("papper");
  }
  
  delay(2000);
  lcd.clear();
  
  


 

}

  


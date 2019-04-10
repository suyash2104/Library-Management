 /*
 * Based on code Dr.Leong   ( WWW.B2CQSHOP.COM )
 * Created by Miguel Balboa (circuitito.com), Jan, 2012.
 * Rewritten by Søren Thing Andersen (access.thing.dk), fall of 2013 (Translation to English, refactored, comments, anti collision, cascade levels.)
 * Released into the public domain.
 *
 * Sample program showing how to read data from a PICC using a MFRC522 reader on the Arduino SPI interface.
 *----------------------------------------------------------------------------- empty_skull 
 * Aggiunti pin per arduino Mega
 * add pin configuration for arduino mega
 * http://mac86project.altervista.org/
 ----------------------------------------------------------------------------- Nicola Coppola
 * Pin layout should be as follows:
 * Signal     Pin              Pin               Pin
 *            Arduino Uno      Arduino Mega      MFRC522 board
 * ------------------------------------------------------------
 * Reset      9                5                 RST
 * SPI SS     10               53                SDA
 * SPI MOSI   11               51                MOSI
 * SPI MISO   12               50                MISO
 * SPI SCK    13               52                SCK
 *
 * The reader can be found on eBay for around 5 dollars. Search for "mf-rc522" on ebay.com. 
 */

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN); 
unsigned long getID();// Create MFRC522 instance.
int pin = 3;
char serialdata;
void setup() {
    Serial.begin(9600); // Initialize serial communications with the PC
    SPI.begin();            // Init SPI bus
    mfrc522.PCD_Init(); // Init MFRC522 card
    //Serial.println("Scan PICC to see UID and type...");
}

void loop() {
    // Look for new cards
    if(mfrc522.PICC_IsNewCardPresent()) {
  unsigned long uid = getID();
  if(uid != -1){
    //MSerial.print("Card detected, UID: "); 
    Serial.println(uid);
    pinMode(pin, OUTPUT);
  }
}
   /*
    // Select one of the cards
    if ( ! mfrc522.PICC_ReadCardSerial()) {
        return;
    }

    // Dump debug info about the card. PICC_HaltA() is automatically called.
    mfrc522.PICC_DumpToSerial(&(mfrc522.uid));

    */
      if (Serial.available() > 0 ) {
      serialdata = Serial.read();

      if (serialdata == '1') {
        digitalWrite(pin,HIGH);
      }
      else if (serialdata == '0'){
        digitalWrite(pin, LOW);
      }
    }
    // Select one of the cards
    

}


unsigned long getID(){
  if ( ! mfrc522.PICC_ReadCardSerial()) { //Since a PICC placed get Serial and continue
    return -1;
  }
  unsigned long hex_num;
  hex_num =  mfrc522.uid.uidByte[0] << 24;
  hex_num += mfrc522.uid.uidByte[1] << 16;
  hex_num += mfrc522.uid.uidByte[2] <<  8;
  hex_num += mfrc522.uid.uidByte[3];
  mfrc522.PICC_HaltA(); // Stop reading
  return hex_num;
}

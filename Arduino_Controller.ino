#include <Servo.h>

char lectura; //Variable para guardar la lectura del Serial
int A = 2, B = 4, C = 7, D = 8, S = 10;
int uno = 0, dos = 0, tres = 0, cuatro = 0, reversa;
int cont1 = 90, cont2 = 90, cont3 = 90, cont4 = 90;
int base = 3, seg = 5, ter = 6, pinza = 9;
Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;

//Este codigo está definido el control de servos 
//para un brazo robot
void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(A, INPUT);
  pinMode(B, INPUT);
  pinMode(C, INPUT);
  pinMode(D, INPUT);
  pinMode(S, INPUT);
  myservo1.attach(base);
  myservo2.attach(seg);
  myservo3.attach(ter);
  myservo4.attach(pinza);
}

void loop()
{
  //Si recibimos algo por serial, lo guardamos
  if (Serial.available() >= 1)
  {
    lectura = Serial.read();

    //Lectura del caracter R, G o B
    if (lectura == 'r')
    {
      myservo1.write(0);
    }
    if (lectura == 'g')
    {
      myservo1.write(180);
    }
    if (lectura == 'b')
    {
      myservo1.write(90);
    }
  }
}

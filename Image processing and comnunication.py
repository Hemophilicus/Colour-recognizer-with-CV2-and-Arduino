import cv2
import numpy as np
import serial

captura = cv2.VideoCapture(0)

ser = serial.Serial('COM6', 9600)
 

while(1):
 
   _, frame = captura.read()
   hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
   # Rojo
   low_red = np.array([0, 155, 84]) #161, 155, 84
   high_red = np.array([10, 255, 255])#6
   #La siguiente línea es el Threshold
   red_mask = cv2.inRange(hsv_frame, low_red, high_red)
   red = cv2.bitwise_and(frame, frame, mask=red_mask)

   # Azul
   low_blue = np.array([94, 80, 2])
   high_blue = np.array([126, 255, 255])
   blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
   blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

   # Verde
   low_green = np.array([30, 52, 72])
   high_green = np.array([85, 255, 255])
   green_mask = cv2.inRange(hsv_frame, low_green, high_green)
   green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Todo menos blanco
   low = np.array([0, 42, 0])
   high = np.array([179, 255, 255])
   mask = cv2.inRange(hsv_frame, low, high)
   result = cv2.bitwise_and(frame, frame, mask=mask)


   #Encontrar el area de los objetos que detecta la camara
   momentsg = cv2.moments(green_mask)
   momentsr = cv2.moments(red_mask)
   momentsb = cv2.moments(blue_mask)

   areag = momentsg['m00']
   arear = momentsr['m00']
   areab = momentsb['m00']

   #Descomentar para ver el area por pantalla
   print (areag)
   print (areab)
   print (arear)
 
   #Si el objeto tiene un area determinada, escribimos una letra
   #que tenga referencia al color
   if(areag >2000000): 
      ser.write(str.encode('g'))
   if(arear >2000000): 
      ser.write(str.encode('r'))
   if(areab >2000000): 
      ser.write(str.encode('b'))
     
 
   #Lineas para mascaras

   #cv2.imshow('mask', mask)
   cv2.imshow('Rojo', red)
   cv2.imshow('Verde', green)
   cv2.imshow('Azul', blue)
   cv2.imshow('Camara', frame)
   tecla = cv2.waitKey(5) & 0xFF
   if tecla == 27:
      break
 
cv2.destroyAllWindows()

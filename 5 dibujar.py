import cv2
import numpy as np

cap = cv2.VideoCapture(0)
canvas = None  # Lienzo para dibujar

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if canvas is None:
        canvas = np.zeros_like(frame)  # Inicializar lienzo
    
    # Detectar color rojo (ej. marcador)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Encontrar el centro del objeto rojo
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        (x, y), _ = cv2.minEnclosingCircle(largest)
        cv2.circle(canvas, (int(x), int(y)), 5, (0, 255, 0), -1)  # Dibuja un círculo
    
    cv2.imshow('Webcam', frame)
    cv2.imshow('Lienzo', canvas)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
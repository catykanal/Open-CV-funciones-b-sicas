import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Crear una ventana redimensionable
cv2.namedWindow('Seguimiento de Azul', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir a HSV y crear máscara para color azul
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Encontrar contornos y dibujar rectángulo
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Filtra contornos pequeños
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Convertir máscara a color para concatenar
    mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # Combinar frame y máscara horizontalmente
    combined = np.hstack((frame, mask_colored))
    
    # Mostrar en una sola ventana
    cv2.imshow('Seguimiento de Azul', combined)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
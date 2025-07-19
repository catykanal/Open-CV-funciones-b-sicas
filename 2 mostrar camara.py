import cv2

cap = cv2.VideoCapture(0)  # Abre la cámara

while cap.isOpened():
    ret, frame = cap.read()  # Lee un fotograma
    
    if not ret:  # Si no se pudo leer el fotograma, sal del bucle
        print("Error: No se pudo capturar el fotograma.")
        break
    
    cv2.imshow('Webcam', frame)  # Muestra el fotograma
    
    # Espera 1 ms y verifica si se presionó 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos fuera del bucle
cap.release()
cv2.destroyAllWindows()
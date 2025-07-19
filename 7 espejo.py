import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Aplicar efecto espejo (flip horizontal)
    mirrored = cv2.flip(frame, 1)
    
    # Aplicar desenfoque gaussiano
    blurred = cv2.GaussianBlur(frame, (15, 15), 0)
    
    # Mostrar efectos
    cv2.imshow('Original', frame)
    cv2.imshow('Espejo', mirrored)
    cv2.imshow('Desenfoque', blurred)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
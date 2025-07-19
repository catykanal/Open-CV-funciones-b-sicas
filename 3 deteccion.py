import cv2

cap = cv2.VideoCapture(0)  # Inicia la webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir a grises y aplicar Canny
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)  # Umbrales mínimo y máximo
    
    # Mostrar resultados
    cv2.imshow('Original', frame)
    cv2.imshow('Bordes (Canny)', edges)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
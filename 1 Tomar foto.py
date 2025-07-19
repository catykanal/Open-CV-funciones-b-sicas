import cv2

cap = cv2.VideoCapture(0)  # Usa 0 para /dev/video0

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara")
else:
    print("Cámara conectada correctamente")
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("foto_prueba.jpg", frame)
        print("Foto guardada como 'foto_prueba.jpg'")
        cap.release()

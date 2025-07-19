import cv2
import datetime
import os
import numpy as np

# Configuración inicial
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=False)

# Parámetros de video (ajusta según tu cámara)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Usar 'XVID' para AVI (universal)

# Variables de control
recording = False
out = None
motion_detected = False
last_motion_time = datetime.datetime.now()
motion_timeout = 3  # Segundos para seguir grabando después del último movimiento

# Carpeta para guardar videos
os.makedirs("videos_movimiento", exist_ok=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Detección de movimiento
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))  # Eliminar ruido
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    motion_detected = any(cv2.contourArea(cnt) > 1000 for cnt in contours)  # Área mínima

    # 2. Lógica de grabación
    current_time = datetime.datetime.now()
    
    if motion_detected:
        last_motion_time = current_time  # Reiniciar temporizador
        
        if not recording:
            # Iniciar nueva grabación
            filename = f"movimiento_{current_time.strftime('%Y%m%d_%H%M%S')}.avi"
            filepath = os.path.join("videos_movimiento", filename)
            out = cv2.VideoWriter(filepath, fourcc, fps, (frame_width, frame_height))
            recording = True
            print(f"🔥 Movimiento detectado! Grabando: {filename}")
    
    # Seguir grabando por [motion_timeout] segundos después del último movimiento
    elif recording and (current_time - last_motion_time).seconds > motion_timeout:
        out.release()
        recording = False
        print("⏹️ Grabación detenida (sin movimiento reciente).")

    # 3. Escribir frame si está grabando
    if recording:
        out.write(frame)
        cv2.putText(frame, "GRABANDO", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # 4. Visualización
    cv2.imshow('Camara', frame)
    cv2.imshow('Movimiento', fgmask)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if recording:
            out.release()
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
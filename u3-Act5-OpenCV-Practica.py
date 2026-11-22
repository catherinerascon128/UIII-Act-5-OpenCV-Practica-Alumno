
import cv2
import numpy as np
# catherine rascon NC.0072

# Leer la imagen del archivo
image = cv2.imread('kapibara.png')

# Mostrar la imagen en una ventana
cv2.imshow('Imagen original catherine rascon 0072', image)

# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cargar la imagen
image = cv2.imread('kapibara.png')

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Guardar la imagen en escala de grises
cv2.imwrite('imagen_gris_0072.jpg', gray_image)

# Cargar la imagen
image = cv2.imread('kapibara.png')

# Redimensionar la imagen a 300x200
resized_image = cv2.resize(image, (300, 200))

# Guardar la imagen redimensionada
cv2.imwrite('redimencionar_img_0072.jpg', resized_image)

# Cargar la imagen
image = cv2.imread('kapibara.png')

# Obtener la altura y el ancho de la imagen
(h, w) = image.shape[:2]

# Definir el centro de la imagen
center = (w // 2, h // 2)

# Matriz de rotación
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)

# Realizar la rotación
rotated_image = cv2.warpAffine(image, matrix, (w, h))

# Guardar la imagen rotada
cv2.imwrite('imagen_rotada_0072.jpg', rotated_image)

# Cargar la imagen
image = cv2.imread('kapibara.png')

# Aplicar desenfoque gaussiano
blured_image = cv2.GaussianBlur(image, (15, 15), 0)

# Guardar la imagen desenfocada
cv2.imwrite('desenfoque_imagen_0072.jpg', blured_image)

# Cargar la imagen
image = cv2.imread('kapibara.png')

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100, 200)

# Guardar la imagen de bordes
cv2.imwrite('deteccion_bordes_0072.jpg', edges)

# Cargar la imagen
image = cv2.imread('kapibara.png')

# Dibujar un rectángulo
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)

# Agregar texto a la imagen
cv2.putText(image, 'catherine rascon 0072', (60, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Guardar la imagen de salida
cv2.imwrite('Agregar_txt_rectangulo_imagen_0072.jpg', image)

# Cargar la imagen
image = cv2.imread('kapibara.png', 0)

# Aplicar umbralización
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Guardar la imagen umbralizada
cv2.imwrite('Umbral_0072_image.jpg', thresh_image)

# Cargar la imagen
image = cv2.imread('kapibara.png')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Encontrar bordes
edges = cv2.Canny(gray_image, 100, 200)

# Encontrar contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Guardar la imagen de salida con contornos
cv2.imwrite('contornos_imagen_0072.jpg', image)
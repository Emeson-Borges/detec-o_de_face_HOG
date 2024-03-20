import cv2
import dlib

image =  cv2.imread('img.jpeg')
# cv2.imshow('Pessoas', image)

# Definir o tamanho desejado da imagem
novo_tamanho = (900, 800) 

# Redimensionar a imagem
image_redimensionada = cv2.resize(image, novo_tamanho)

detector_face_hog = dlib.get_frontal_face_detector()
deteccoes = detector_face_hog(image_redimensionada, 1) # escala

#print(deteccoes)

for face in deteccoes:
    # print(face)
    # print(face.left)
    # print(face.right)
    # print(face.top)
    # print(face.bottom)
    l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(image_redimensionada, (l, t), (r, b), (0, 255), 2)
cv2.imshow('Image com Face Detectada', image_redimensionada)

cv2.waitKey(0)

cv2.destroyAllWindows()
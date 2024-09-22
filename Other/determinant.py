import cv2 
import numpy as np
import easyocr

num = int(input("Какой файл открыть? "))
try:
    image = cv2.imread(fr"C:\Users\vladm\.vscode\Projects\Determinant\Test{num}.png")
    if image is None:
        raise FileNotFoundError("Изображения нет")
except Exception as e:
    print(f"Ошибка: {e}")
    exit()
gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY, 11, 2)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(gray, contours, -1, (0, 255, 0), 2)
cv2.imwrite(fr"C:\Users\vladm\.vscode\Projects\Determinant\Test{num}_contours.png", gray)

try:
    text = easyocr.Reader(['en']).readtext(fr"C:\Users\vladm\.vscode\Projects\Determinant\Test{num}_contours.png")
    print("Распознанный текст:\n", text)
except Exception as e:
    print(f"Ошибка при распознавании текста: {e}")

try:
    lines = text.strip().split('\n')
    matrix = []
    for line in lines:
        row = list(map(float, line.split()))
        matrix.append(row)
        matrix = np.array(matrix)

    determinant = np.linalg.det(matrix)
    print(f"Определитель матрицы: {determinant}")
except Exception as e:
    print(f"Ошибка: {e}")

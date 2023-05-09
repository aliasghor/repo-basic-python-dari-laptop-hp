import numpy as np
import os
os.system("cls")

contohList = [1,2,3,4]
vectorA = np.array([1,2,3,4])
print(contohList)
print(vectorA**2)
print(vectorA%2)

matrixB = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrixB}")
print(f"matrix b kuadrat = \n{matrixB**2}")

zerosC = np.zeros((2,2))
print(f"zeros c = \n{zerosC}")

onesD = np.ones((2,2))
print(f"ones d = \n{onesD}")

jumlah = matrixB + matrixB**2 + onesD
print(f"hasilnya = \n{jumlah}")
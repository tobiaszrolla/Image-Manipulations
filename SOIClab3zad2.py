import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy import asarray
def bayer(macierz):
    for i in range(3):
        #Wybór maski
        cz_dane = macierz[:, :, i]
        if i == 0:
            maska = np.array([[0, 1], [0, 0]])
        elif i == 1:
            maska = np.array([[1, 0], [0, 1]])
        elif i == 2:
            maska = np.array([[0, 0], [1, 0]])
        #Duża maska
        duz_macierz = np.zeros((cz_dane.shape[0],cz_dane.shape[1]))
        wiersz_1 = np.zeros((1,duz_macierz.shape[1]))
        wiersz_2 = np.zeros((1,duz_macierz.shape[1]))
        #Okresilenie naprzemiennych wierszy
        for i2 in range(duz_macierz.shape[1]):
            if i2 % 2 == 0:
                wiersz_1[0,i2] = maska[0,0]
            else:
                wiersz_1[0,i2] = maska[0,1]
        for i2 in range(duz_macierz.shape[1]):
            if i2 % 2 == 0:
                wiersz_2[0,i2] = maska[1,0]
            else:
                wiersz_2[0,i2] = maska[1,1]
        #Duza maska
        for i2 in range(duz_macierz.shape[0]):
            if i2 % 2 == 0:
                duz_macierz[i2,:] = wiersz_1
            else:
                duz_macierz[i2,:] = wiersz_2
        #Dopasowanie do maski
        for i2 in np.ndindex(duz_macierz.shape):
            if duz_macierz[i2] == 0:
                cz_dane[i2] = 0
    return macierz
def apr_lin(macierz):
    for i in range(3):
        cz_dane = macierz[:, :, i]
        wiersze, kolumny = cz_dane.shape
        for y in range(wiersze):
            for x in range(1,kolumny-1):
                if cz_dane[y,x] == 0:
                    cz_dane[y,x] = (cz_dane[y,x+1] - cz_dane[y,x-1])/2
        for x in range(kolumny):
            for y in range(1,wiersze-1):
                if cz_dane[y,x] == 0:
                    cz_dane[y,x] = (cz_dane[y+1,x] - cz_dane[y-1,x])/2

    return macierz
brg_obraz = cv2.imread("Birds.bmp",cv2.IMREAD_COLOR)
rgb_obraz = cv2.cvtColor(brg_obraz, cv2.COLOR_BGR2RGB)
obraz_array = np.array(rgb_obraz)
plt.imshow(obraz_array)
plt.show()
#print(obraz_array.shape)
obraz_array = bayer(obraz_array)
plt.imshow(obraz_array)
plt.show()
rgb_obraz = apr_lin(obraz_array)
plt.imshow(obraz_array)
plt.show()


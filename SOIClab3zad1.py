import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy import asarray
def fuji(macierz):
    for i in range(3):
        #Wybór maski
        cz_dane = macierz[:, :, i]
        wiersze, kolumny = cz_dane.shape
        brak_wiersze = 6 - wiersze % 6
        brak_kolumny = 6 - kolumny % 6
        if i == 0:
            maska = np.array([[0, 0, 1, 0, 1, 0],
                              [1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0],
                              [0, 1, 0, 0, 0, 1],
                              [0, 0, 0, 1, 0, 0],
                              [1, 0, 0, 0, 0, 0]])
        elif i == 1:
            maska = np.array([[1, 0, 0, 1, 0, 0],
                              [0, 1, 1, 0, 1, 1],
                              [0, 1, 1, 0, 1, 1],
                              [1, 0, 0, 1, 0, 0],
                              [0, 1, 1, 0, 1, 1],
                              [0, 1, 1, 0, 1, 1],])
        elif i == 2:
            maska = np.array([[0, 1, 0, 0, 0, 1],
                              [0, 0, 0, 1, 0, 0],
                              [1, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 1, 0],
                              [1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0]])
        #Duża maska
        duz_maska = np.zeros((wiersze + brak_wiersze,kolumny + brak_kolumny))
        #Duza maska
        ly = int((wiersze + brak_wiersze)/6)
        lx = int((kolumny + brak_kolumny) / 6)
        for y in range(1,ly+1):
            for x in range(1, lx+1):
                duz_maska[((y-1)*6):y*6,((x-1)*6):x*6] = maska
        #Dopasowanie do maski
        for i2 in np.ndindex(cz_dane.shape):
            if duz_maska[i2] == 0:
                cz_dane[i2] = 0
    return macierz
def inter(macierz):
    for i in range(3):
        cz_dane = macierz[:, :, i]
        wiersze, kolumny = cz_dane.shape
        mac_pom = np.zeros((wiersze+2,kolumny+2))
        #print(mac_pom.shape)
        mac_pom[1:-1,1:-1] = cz_dane[:,:]
        for y in range(1,wiersze+1):
            for x in range(1,kolumny+1):
                if mac_pom[y,x] == 0:
                    mian = 0
                    licznik = 0
                    for y2 in range(y-1,y+1):
                        for x2 in range(x - 1, x + 1):
                            if mac_pom[y2,x2] != 0:
                                licznik = licznik + mac_pom[y2,x2]
                                mian +=1
                    if mian != 0:
                        mac_pom[y,x] = licznik/mian
        cz_dane[:,:] = mac_pom[1:-1,1:-1]
    return macierz
brg_obraz = cv2.imread("Birds.bmp",cv2.IMREAD_COLOR)
rgb_obraz = cv2.cvtColor(brg_obraz, cv2.COLOR_BGR2RGB)
obraz_array = np.array(rgb_obraz)
plt.imshow(obraz_array)
plt.show()
obraz_array = fuji(obraz_array)
plt.imshow(obraz_array)
plt.show()
obraz_array = inter(obraz_array)
plt.imshow(obraz_array)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

ldanych = 99
x = np.linspace(1, 10, ldanych)
y = np.sin(x)
wynik_x = []
wynik_y = []
for i in range(0,len(x),3):
    #Wczytanie macierzy X,Y
    X=np.array([[x[i]**2,x[i],1],
                [x[i+1]**2,x[i+1],1],
                [x[i+2]**2,x[i+2],1]])
    Y = np.array([y[i],
        y[i+1],
        y[i+2]])
    det = X[0,0]*(X[1,1]*X[2,2]-X[1,2]*X[2,1]) - X[0,1]*(X[1,0]*X[2,2]-X[1,2]*X[2,0]) + X[0,2]*(X[1,0]*X[2,1]-X[1,1]*X[2,0])
    diag =np.array([[1.00,-1.00,1.00],
                    [-1.00,1.00,-1.00],
                    [1.00,-1.00,1.00]])
    #Obliczanie macierzy diagonalnej i2 miejsce w macierzy diagonalnej
    for i2 in np.ndindex(X.shape):
        mtx_pom = np.zeros(4)
        nr=0
        for i3 in np.ndindex(X.shape):
            if i3[0] != i2[0] and i3[1] != i2[1]:
                mtx_pom[nr] = X[i3]
                nr+=1
        det_pom = mtx_pom[0]*mtx_pom[3]-mtx_pom[1]*mtx_pom[2]
        diag[i2]=diag[i2]*det_pom
    #transpozycja i2 elementy do transpozycji
    trans = np.zeros((3,3))
    for i2 in np.ndindex(diag.shape):
        trans[i2[1],i2[0]]=diag[i2]
    trans = trans/det
    #mnożenie macierzy Y i X**-1
    A = np.zeros((3,1))
    A[0] = trans[0, 0] * Y[0] + trans[0, 1] * Y[1] + trans[0, 2] * Y[2]
    A[1] = trans[1, 0] * Y[0] + trans[1, 1] * Y[1] + trans[1, 2] * Y[2]
    A[2] = trans[2, 0] * Y[0] + trans[2, 1] * Y[1] + trans[2, 2] * Y[2]
    x_now = np.linspace(x[i], x[i+2], 3)
    y_now = A[0] * x_now**2 + A[1] * x_now + A[2]
    wynik_x = np.hstack((wynik_x, x_now))
    wynik_y = np.hstack((wynik_y, y_now))
#Wynik
plt.plot(wynik_x,wynik_y,'o')
plt.show()
















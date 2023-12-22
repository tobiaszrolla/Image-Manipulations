import numpy as np
import matplotlib.pyplot as plt
ilex = 10
x = np.linspace(0,5,ilex)
y = np.sin(x)
x_wynik = []
y_wynik = []
for i in range(ilex-1):
    ilenowych = 5
    x2 = np.linspace(x[i],x[i+1],ilenowych)
    sr_x = (x[i]+x[i+1])/2
    y2 = [0]*ilenowych
    for i2 in range(ilenowych):
        if x[i2] < sr_x:
            y2[i2] = y[i]
        else:
            y2[i2] = y[i+1]
    if i != 0:
        x2 = x2[1:]
        y2 = y2[1:]
    x_wynik = np.hstack((x_wynik,x2))
    y_wynik = np.hstack((y_wynik, y2))

    print(x_wynik,y_wynik)
plt.plot(x_wynik,y_wynik,'o')
plt.show()



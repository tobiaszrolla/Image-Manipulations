import numpy as np
import matplotlib.pyplot as plt
ldanych = 10
x = np.linspace(0,5,ldanych)
y = np.sin(x)
lpomiendzy = 5
lnowych = (ldanych*lpomiendzy) -lpomiendzy
x_wynik = [0]*lnowych
y_wynik = [0]*lnowych
cont = 0
for i in range(ldanych-1):
    x2 = np.linspace(x[i],x[i+1],lpomiendzy)
    a = (y[i]-y[i+1])/(x[i]-x[i+1])
    b = y[i]-a*x[i]
    y2 = x2*a+b
    y_wynik[i* 5:(i + 1) * 5] = y2
    x_wynik[i * 5:(i + 1) * 5] = x2

    #print(cont)

#print(x_wynik,y_wynik)
plt.plot(x_wynik,y_wynik,'o')
plt.show()
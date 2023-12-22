import numpy as np
import matplotlib.pyplot as plt
#ldanych = 33
#x = np.linspace(0,5,ldanych)
x = np.array([1,2,3])
#y = np.sin(x)
y = x*2
lpomiendzy = 5
lnowych = (3*lpomiendzy) - lpomiendzy
plt.show()
x_wynik = []
y_wynik = []
for i in range(0,len(x),3):
    x2 = np.linspace(x[i],x[i+2],lpomiendzy)
    mian = (x[i+1] - x[i])*(x[i+2] - x[i])*(x[i+2] - x[i+1])
    a = ((y[i+1] - y[i])*(x[i+2]**2 - x[i]**2) - (y[i+2] - y[i])*(x[i+1]**2 - x[i]**2))/mian
    b = ((y[i+1] - y[i])*(x[i+2] - x[i]) - (y[i+2] - y[i])*(x[i+1] - x[i]))/mian
    c = (y[i]*(x[i+1]**2 - x[i+2]**2)+y[i+1]*(x[i+2]**2-x[i]**2)+y[i+2]*(x[i]**2 - x[i+1]**2))/mian
    y2 = a*x2**2 + b*x2 + c
    x_wynik = np.hstack((x_wynik, x2))
    y_wynik = np.hstack((y_wynik, y2))
plt.plot(x_wynik,y_wynik,'o')
plt.show()
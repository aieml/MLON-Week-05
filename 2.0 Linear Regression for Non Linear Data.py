import numpy as np

x=np.arange(0,100,2)

x=x.reshape(-1,1) #interchanging rows and columns(this creates a column vector)
y=3*np.power(x,2)-4*x+5
#y=3x^2-4x+5

from sklearn.linear_model import LinearRegression

clsfr=LinearRegression()
clsfr.fit(x,y)

m=clsfr.coef_[0]
c=clsfr.intercept_

x_best=np.arange(0,100,5)
y_best=m*x_best+c

from matplotlib import pyplot as plt

plt.plot(x,y,marker='o')
plt.xlabel('X')
plt.ylabel('Y')

plt.plot(x_best,y_best,'r')

plt.show()

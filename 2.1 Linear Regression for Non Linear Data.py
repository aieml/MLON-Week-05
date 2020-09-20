import numpy as np
from matplotlib import pyplot as plt

x=np.arange(0,100,1)

x=x.reshape(-1,1) #interchanging rows and columns(this creates a column vector)
y=3*np.power(x,2)-4*x+5
#y=3x^2-4x+5
plt.plot(x,y,'b',marker='x')

for i in range (len(y)):
    y[i]=y[i]+np.random.randint(-5,5,1)

#y=3x^2-4x+5+noise
plt.scatter(x,y,c='r')
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly=PolynomialFeatures(degree=3,include_bias=False)
x_new=poly.fit_transform(x)

from sklearn.linear_model import LinearRegression

clsfr=LinearRegression()
clsfr.fit(x_new,y)

print(clsfr.coef_)
print(clsfr.intercept_)


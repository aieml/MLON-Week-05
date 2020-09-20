import pickle
import numpy as np

data=pickle.load(open('data.pickle','rb'))
target=pickle.load(open('target.pickle','rb'))

target[0,4]=170
#correction

data=data.reshape((13,1))
target=target.reshape((13,1))

from sklearn.linear_model import LinearRegression

clsfr=LinearRegression()
clsfr.fit(data,target)

c=clsfr.intercept_
m=clsfr.coef_[0]
#gradient and intercept of the best fit line

x=np.arange(40,100,5)
#for i in range(0,10,1)
y=m*x+c
#calculating the corresponding y vals using x vals

result=clsfr.predict([[87]])

print('Height:',result)

from matplotlib import pyplot as plt

plt.scatter(data,target,c='b') #scatter diagram
plt.plot(x,y,'r')              #line diagram

plt.scatter(87,result,c='r')   #test data

plt.xlabel('Weights(kg)')
plt.ylabel('Heights(cm)')
plt.show()



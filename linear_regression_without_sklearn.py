from statistics import mean
import numpy as np
from matplotlib import pyplot as plt

def fit(x,y):

    x=np.array(x,dtype=np.float64)
    y=np.array(y,dtype=np.float64)
    
    ms= ((mean(x)*mean(y))-(mean(x*y)))/((mean(x)*mean(x))-mean(x*x))
    bs= mean(y)-(ms*mean(x))
    return ms,bs

x=[70,79,64,80,97,59,80,75,80,80,85,60]
y=[177,160,165,174,175,167,175,177,175,165,180,150]

#rt=fit(x,y)     #rt is a tuple, rt[0]=m, rt[1]=b
#m=rt[0]
#b=rt[1]

(m,b)=fit(x,y)
xp=84       #test x value
yp=m*xp+b   #predicted y value
print(yp)


bestFitx=np.arange(60,101,10)
bestFity= m*bestFitx +b

plt.plot(bestFitx,bestFity,'r')

plt.scatter(xp,yp)

print(y)
y=np.array(y,dtype=np.float64)
ymean=mean(y)

yp=[ymean for i in range(len(x))]

plt.plot(x,yp)

plt.scatter(x,y)
plt.xlabel('Weights(kg)')
plt.ylabel('Heights(cm)')

plt.show()

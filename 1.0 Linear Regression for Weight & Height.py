no_ptcpnts=eval(input('Enter the no of Participants:'))

import numpy as np

data=np.zeros((1,no_ptcpnts),np.float32)
target=np.zeros((1,no_ptcpnts),np.float32)

for i in range(no_ptcpnts):

    weight=eval(input('Patricpant '+str(i+1)+', Enter your Weight(kg):'))
    data[0,i]=weight

    height=eval(input('Patricpant '+str(i+1)+', Enter your Height(cm):'))
    target[0,i]=height

import pickle

pickle.dump(data,open('data.pickle','wb'))
pickle.dump(target,open('target.pickle','wb'))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
def PLA(x, y, w_vector, order, data_number, dimension, uptime):
    index = np.random.randint(data_number,size=1) # the index of x we are checking
    index = index[0]
    last_corrected = (index - 1 + data_number) % data_number  # the index of the last corrected data 
    print(index, last_corrected)
    while(True):
        if(sign_of_inner_product(x[order[index],],w_vector)== y[order[index],0]):
            if(index == last_corrected): 
                return uptime #no mistake
            else:
                index += 1
                index %= data_number
                continue
        else:
            learn(x[order[index],], y[order[index],0 ], w_vector)        
            uptime += 1
            last_corrected = index
            index += 1 
            index %= data_number
def learn(x, y, w):
        w += y * x
        return 
def sign_of_inner_product(data, w):
    inner = np.inner(data,w)
    if(inner > 0):
        return 1
    else:
        return -1
with open("./hw1_7_train.dat", 'r') as input_file:
    fd_data = input_file.readlines()
    data_list = [list(map(float,num.split())) for num in fd_data]
raw_data = np.array(data_list)
#initialize x 
x_tmp = raw_data[:,:4]
(data_number, dimension) = x_tmp.shape
x0 = np.ones((data_number,1))    
x = np.hstack((x0,x_tmp))
dimension += 1
#initialize y
y = raw_data[:,4:]
update_list = []
for trial in range(0,2000):
#initialize w
    w_vector = np.zeros((1,dimension))
#set order
    order = np.arange(data_number)
#do PLA
    uptime = 0
    uptime = PLA(x, y, w_vector, order, data_number, dimension, uptime)
    update_list.append(uptime)
update_array = np.array(update_list)
print(update_array.mean())
plt.hist(update_array, density=True)
plt.show()

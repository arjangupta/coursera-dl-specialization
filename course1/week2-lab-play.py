# Just a playground to understand Week 2 concepts

import numpy as np

x_arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(f'x_arr is {x_arr}')
# Print shape of array
print(f'x_arr shape is {x_arr.shape}')
flatten_x = x_arr.reshape(1, x_arr.shape[0]*x_arr.shape[1])
print(f'flatten_x is {flatten_x}')
print(f'flatten_x shape is {flatten_x.shape}')
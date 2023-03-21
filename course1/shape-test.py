import numpy as np

a = np.random.randn(3,3)
print(f'Shape of a is {a.shape}')

b = np.random.randn(2,1)
print(f'Shape of b is {b.shape}')

# The following does not work because broadcasting doesn't work that way
# c = a+b
# print(f'Shape of c is {c.shape}')
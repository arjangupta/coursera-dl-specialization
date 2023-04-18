import numpy as np

random_array = np.random.rand(3,2)
y = np.sum(random_array, axis=0, keepdims=True)
print(y.shape)
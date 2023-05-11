import numpy as np

# Create array with higher dimensions
x = np.array([[[0], [1], [2]]])
# Show array
print("x: ", x)
# Show shape of array
print("x.shape: ", x.shape)

# Squeeze array
x_squeezed = np.squeeze(x)
# Show squeezed array
print("x_squeezed: ", x_squeezed)
# Show shape of squeezed array
print("x_squeezed.shape: ", x_squeezed.shape)

# Create another random higher dimensional array (integer values)
x = np.random.randint(1, 10, size=(2, 3, 4))
# Show array
print("x: ", x)
# Show shape of array
print("x.shape: ", x.shape)

# Squeeze array
x_squeezed = np.squeeze(x)
# Show squeezed array
print("x_squeezed: ", x_squeezed)
# Show shape of squeezed array
print("x_squeezed.shape: ", x_squeezed.shape)

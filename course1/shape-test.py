import numpy as np

# a = np.random.randn(3,3)
# print(f'Shape of a is {a.shape}')

# b = np.random.randn(2,1)
# print(f'Shape of b is {b.shape}')
# The following does not work because broadcasting doesn't work that way
# c = a+b
# print(f'Shape of c is {c.shape}')


a = np.random.randn(1,3)
print(f'Shape of a is {a.shape}')
b = np.random.randn(3,3)
print(f'Shape of b is {b.shape}')
c = a*b
print(f'Shape of c is {c.shape}')

q7 = np.array([[2,1],[1,3]])
print(f'Result a q7*q7 is {q7*q7}')

# Good example of broadcasting
q8_a = np.random.randint(low=0,high=10,size=(4,3))
print(f'q8_a is {q8_a}')
q8_b = np.random.randint(low=0,high=10,size=(4,1))
print(f'q8_b is {q8_b}')
q8_c = q8_a + q8_b
print(f'q8_c is {q8_c}')

# Another good example of broadcasting
q9_a = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
print(f'q9_a is {q9_a}, its shape is {q9_a.shape}')
# q9_b = np.random.randint(low=0,high=10,size=(3,1))
q9_b = np.array([[7],[6],[5]])
print(f'q9_b is {q9_b}, its shape is {q9_b.shape}')
q9_c = q9_a*q9_b
print(f'q9_c is {q9_c}')
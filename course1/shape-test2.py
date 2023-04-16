import numpy as np

q4_a = np.random.randn(2,3)
q4_b = np.random.randn(2,1)
q4_c = q4_a + q4_b
print(f'q4_c shape is {q4_c.shape}')
print(f'q4_c shape[0] is {q4_c.shape[0]}')

q5_a = np.random.randn(4,3)
q5_b = np.random.randn(3,2)
# ValueError: operands could not be broadcast together with shapes (4,3) (3,2)
# q5_c = q5_a*q5_b 
# print(f'q5_c shape is {q5_c.shape}')

q8_a = np.random.randint(low=0,high=10,size=(3,4))
print(f'q8_a is {q8_a}')
q8_b = np.random.randint(low=0,high=10,size=(4,1))
print(f'q8_b is {q8_b}')
q8_c = np.zeros((3,4), dtype=int)
for i in range(3):
    for j in range(4):
        q8_c[i][j] = q8_a[i][j] + q8_b[j]
print(f'q8_c is {q8_c}')
q8_c_vectorized = q8_a + q8_b.T
print(f'q8_c_vectorized is {q8_c_vectorized}')

# Week 2 practice
example_mat = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(f'example_mat is {example_mat}')
ex_shape = example_mat.shape
print(f'shape of example_mat is {ex_shape}')
print(f'ex_shape first dimension is {ex_shape[0]}')
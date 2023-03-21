import numpy as np

q4_a = np.random.randn(2,3)
q4_b = np.random.randn(2,1)
q4_c = q4_a + q4_b
print(f'q4_c shape is {q4_c.shape}')

q5_a = np.random.randn(4,3)
q5_b = np.random.randn(3,2)
# ValueError: operands could not be broadcast together with shapes (4,3) (3,2)
# q5_c = q5_a*q5_b 
# print(f'q5_c shape is {q5_c.shape}')
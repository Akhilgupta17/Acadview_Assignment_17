import numpy as np
A = np.random.rand(10,1)

print("Randome Integers Are:\n",A)

def func(x):
    return (1 / (1 + np.exp(-x)))

result = np.apply_along_axis(func, 0, A)

print('*'*50)

print("New Array to Be Printed:\n",result)

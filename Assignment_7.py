import numpy as np

#Question1

arr= np.random.random((10,1))
print("Random Numbers are:\n",arr)
print("Mean Of These Numbers:",np.mean(arr))

#Question2

arr= np.random.random((20,1))
print("Random Numbers are:\n",arr)
print("Standrad Deviation Of These Numbers:",np.std(arr))
print("Variance Of These Numbers:",np.var(arr))


#Question3

a=np.random.rand(10,20)
b=np.random.rand(20,25)
A=(np.dot(a,b))
print("Multiplication of Both Array IS:\n",A)
B=np.sum(A)
print("Sum Of The New Array Is:",B)

#Question4

A = np.random.rand(10,1)
print("Randome Integers Are:\n",A)
def func(x):
    return (1 / (1 + np.exp(-x)))
result = np.apply_along_axis(func, 0, A)
print('*'*50)
print("New Array to Be Printed:\n",result)


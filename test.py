from datetime import datetime

from numba import njit, jit
from numpy import dot, array as np_array

array = np_array([
    [-1.83048772, 0., 0., 0.],
    [0., 1.83048772, 0., 0.],
    [0., 0., -1.00020002, 0.],
    [0., 0., 0., 100]
])

array2 = np_array([0.679009, 6.149848, 8.080674, 0])


# @njit(cache=True)
def calc():
    for i in range(6500):
        arr = dot(array2, array) / 100
        arr4 = arr[0] * 1920 + 1920 / 2, -arr[1] * 1080 - 1080 / 2


now = datetime.now()
calc()
print(datetime.now() - now)

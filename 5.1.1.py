import numpy as np

x_value = 0.24
a_value = 5.8

z = np.arctan(x_value**2) - np.sqrt(x_value + 1.43**3) + (np.cos(np.pi / (2 * a_value))**3) / np.abs(x_value - a_value**(1/5))

print(z)

import numpy as np
import matplotlib.pyplot as plt

def fourier(x):
    result = 0
    for k in range(6):
        term = (
            (4 / (5*np.pi + 10*np.pi*k)**2) * ((-1)**k * 0.1 - 1/(5*np.pi + 10*np.pi*k))
            + (2 / (15*np.pi + 10*np.pi*k)**2) * ((-1)**(k+1) * 0.1 - 1/(15*np.pi + 10*np.pi*k))
            + (2 / (10*np.pi*k - 5*np.pi)**2) * ((-1)**(k+1) * 0.1 - 1/(10*np.pi*k - 5*np.pi))
        )
        result += 810 * term * np.sin((5*np.pi + 10*np.pi*k)/9 * x)
    return result

def f(x):
    return x ** 2 * np.cos((np.pi * x) / 1.8) ** 2

x = np.linspace(0, 0.9, 1000)
y = fourier(x)
f_x = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Ряд Фурье')
plt.plot(x, f_x, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
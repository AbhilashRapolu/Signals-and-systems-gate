import numpy as np
import matplotlib.pyplot as plt

def x_n(n):
    return 1 + 3*np.sin((15*np.pi/8)*n + (3*np.pi/4)) - 5*np.sin((np.pi/3)*n - np.pi/4)

def z_transform_x(z):
    X_z = 1/(1 - 3*np.cos(15*np.pi/8)*z**(-1) + z**(-2)) + 5/(1 - 2*np.cos(np.pi/3)*z**(-1) + z**(-2))
    return X_z

n = np.arange(0, 100, 1)
x = x_n(n)

z = np.exp(1j * np.linspace(0, 2*np.pi, 1000))
X_z = z_transform_x(z)

plt.figure()
plt.subplot(2, 1, 1)
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Discrete Signal x[n]')

plt.subplot(2, 1, 2)
plt.plot(np.real(z), np.abs(X_z))
plt.xlabel('Re(z)')
plt.ylabel('|X(z)|')
plt.title('Z-Transform of x[n]')
plt.grid(True)

plt.show()



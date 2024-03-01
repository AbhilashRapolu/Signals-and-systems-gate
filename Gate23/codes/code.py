import numpy as np
import matplotlib.pyplot as plt

# Given signal parameters
N = 48
n_values = np.arange(N)
x_n = 1 + 3 * np.sin((15 * np.pi / 8) * n_values + (3 * np.pi / 4)) - 5 * np.sin((np.pi / 3) * n_values - (np.pi / 4))

# DFT coefficients (from previous calculation)
X_k = np.array([ 4.80000000e+01+0.00000000e+00j,  4.52970994e-14-4.59632332e-14j,
  3.13460209e-13-4.43999841e-13j,  5.09116882e+01-5.09116882e+01j,
 -5.15165904e-13+3.47826578e-13j,  5.50881137e-14+5.66202297e-14j,
 -2.70326602e-13-8.09874534e-14j,  8.99969429e-14+1.54056239e-13j,
  8.48528137e+01+8.48528137e+01j, -5.97796541e-14+2.37894551e-13j,
 -4.98556571e-14+2.83025508e-14j, -7.37313171e-14+1.63165177e-13j,
  5.15143483e-14-9.54791801e-14j, -5.68434189e-14+1.77635684e-13j,
 -1.00063121e-13+1.63675991e-15j, -6.92779167e-14+4.61852778e-14j,
 -1.42108547e-13+7.07650269e-14j, -3.65164662e-15-6.21602467e-14j,
 -2.09959196e-14+1.31594591e-14j,  2.34569355e-15+3.30789232e-14j,
 -1.59647908e-14+1.10917575e-13j, -4.79826863e-14+1.35458655e-14j,
 -1.28014295e-13-4.60754707e-14j, -3.84363619e-15+3.86784779e-14j,
 -1.06581410e-13-1.42108547e-14j, -2.22044605e-15-3.97459843e-14j,
 -1.28014295e-13+4.60754707e-14j, -4.26325641e-14-1.42108547e-14j,
 -1.59647908e-14-1.10917575e-13j,  7.10542736e-15-3.19744231e-14j,
 -2.09959196e-14-1.31594591e-14j, -3.86072287e-15+6.39721871e-14j,
 -1.42108547e-13-7.07650269e-14j, -7.09553406e-14-4.90841004e-14j,
 -1.00063121e-13-1.63675991e-15j, -5.91891124e-14-1.82292898e-13j,
  5.15143483e-14+9.54791801e-14j, -7.10542736e-14-1.60760294e-13j,
 -4.98556571e-14-2.83025508e-14j, -6.21724894e-14-2.38031816e-13j,
  8.48528137e+01-8.48528137e+01j,  8.59809175e-14-1.52851467e-13j,
 -2.70326602e-13+8.09874534e-14j,  5.24150351e-14-5.83601240e-14j,
 -5.15165904e-13-3.47826578e-13j,  5.09116882e+01+5.09116882e+01j,
  3.13460209e-13+4.43999841e-13j,  4.38287518e-14+4.70501154e-14j]
)

# Compute magnitude and phase of X[k]
magnitude_X_k = np.abs(X_k)
phase_X_k = np.angle(X_k)

# Plot x[n]
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(n_values, x_n)
plt.title("Signal x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")

# Plot magnitude of X[k]
plt.subplot(3, 1, 2)
plt.stem(np.arange(N), magnitude_X_k)
plt.title("Magnitude of X[k]")
plt.xlabel("k")
plt.ylabel("|X[k]|")

# Plot phase of X[k]
plt.subplot(3, 1, 3)
plt.stem(np.arange(N), phase_X_k)
plt.title("Phase of X[k]")
plt.xlabel("k")
plt.ylabel("Phase (radians)")

plt.tight_layout()
plt.show()

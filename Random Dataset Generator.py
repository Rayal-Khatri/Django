import numpy as np
import matplotlib.pyplot as plt

# Given poles and zeros
poles = [0.45 + 1.06j, 0.45 - 1.06j]
zeros = [0.58 + 2.06j, 0.58 - 2.06j]

plt.figure(figsize=(8, 6))
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Poles and Zeros in the Z-plane')
plt.legend()
plt.grid()
plt.show()

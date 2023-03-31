# exercise 6.8
mu_data = {
    'air': {'C': 120,
        'T_0': 291.15,
        'mu_0': 18.27},
    'nitrogen': {'C': 111,
        'T_0': 300.55,
        'mu_0': 17.81},
    'oxygen': {'C': 127,
        'T_0': 292.25,
        'mu_0': 20.18},
    'carbon dioxide': {'C': 240,
        'T_0': 293.15,
        'mu_0': 14.8},
    'carbon monoxide': {'C': 118,
        'T_0': 288.15,
        'mu_0': 17.2},
    'hydrogen': {'C': 72,
        'T_0': 293.85,
        'mu_0': 8.76},
    'ammonia': {'C': 370,
        'T_0': 293.15,
        'mu_0': 9.82},
    'sulphur dioxide': {'C': 416,
        'T_0': 293.65,
        'mu_0': 12.54}
          }

def mu(T, gas, mu_data):
    C = mu_data[gas]['C']
    T_0 = mu_data[gas]['T_0']
    mu_0 = mu_data[gas]['mu_0']
    return mu_0 * (T_0 + C) / (T + C) * (T/T_0)**1.5


import matplotlib.pyplot as plt
import numpy as np
T_range = np.linspace(223, 373, 100)
gases = ['air', 'carbon dioxide', 'hydrogen']

for gas in gases:
    mu_vals = [mu(T, gas, data) for T in T_range]
    plt.plot(T_range, mu_vals, label=gas)

# plot
plt.title('Viscosity of Gases')
plt.xlabel('Temperature (K)')
plt.ylabel('Viscosity (Pa s)')
plt.legend()

plt.show()

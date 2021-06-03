"""
File which stores natural constants in cgs units.
Created on 2. June 2021 by Andrea Gebek.
"""

import numpy as np

pi = np.pi
e = 4.803e-10
m_e = 9.109e-28
c = 2.998e10
G = 6.674*10**(-8)
k_B = 1.381*10**(-16)
amu = 1.661*10**(-24)
R_J = 6.99e9        #Jupiter radius
M_J = 1.898e30      #Jupiter mass
M_E = 5.974e27      #Earth mass
R_sun = 6.96e10     # Solar radius
R_Io = 1.822e8      # Io radius
m_K = 39.0983*amu
m_Na = 22.99*amu
euler_mascheroni = 0.57721 

"""
Parameters for the absorption lines
Format: [Oscillator strength, Wavelength in vacuum (cm), Natural linewidth*2 pi (Hz),
mass of the absorber (g), name of the absorber]
Na_D2, Na_D1: Draine 2011, Steck 2000
K_D2, K_D1: Draine 2011, Tiecke 2011
"""

absorptionlines_dict = {'Na_D2': [0.641, 5889.95e-8, 3.833e8, m_Na, 'sodium'],
'Na_D1': [0.3199, 5895.92e-8, 3.855e8, m_Na, 'sodium'],
'K_D2': [0.682, 7667.01e-8, 2.3825e8, m_K, 'potassium'],
'K_D1': [0.34, 7701.08e-8, 2.3513e8, m_K, 'potassium']}


"""
Planetary parameters
Format: [Stellar radius (cm), Reference radius (cm), Planetary mass(g)]
WASP-49b: Wyttenbach et al. 2017
HD189733b: Wyttenbach et al. 2015
"""

planets_dict = {'WASP-49b': [1.038 * R_sun, 1.198 * R_J, 0.399 * M_J],
'HD189733b': [0.756 * R_sun, 1.138 * R_J, 1.138 * M_J]}


"""
Dictionary with possible scenarios
"""

scenario_list = ['barometric', 'hydrostatic', 'exomoon']

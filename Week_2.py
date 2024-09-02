import astropy.units as u
import astropy.constants as const
import numpy as np

# calculating orbital velocity of Earth around the Sun
G = const.G       # G as the gravitation constant
M = 1 * u.solMass # physical qunatity with a value and a unit.
R = 1 * u.au      # radius of the Earth's orbit around the Sun in astronomical unit


V = np.sqrt(G * M / R)  # 
print(V.to(u.km/u.s))

# calculating orbital velocity of a satellite around the Earth

G = const.G
M_Earth = 1 * u.earthMAss
R_Satellite = 1 * u.earthRad

V_Satellite = np.sqrt(G * M_Earth / R_Satellite)
print(V_Satellite.to(u.km/u.s))

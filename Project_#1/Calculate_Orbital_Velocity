import astropy.units as u
import astropy.constants as const
import numpy as np

'''
Calculate the orbital velocity
@intput: mass, radius
@output: orbital velocity
'''
def orbital_velocity(mass, radius):
  G = const.G   # G as the gravitation constant
  v = np.sqrt(G * mass / radius)
  return v
  

'''calculating the orbital velocity of Earth around the Sun'''  
M = 1 * u.solMass # physical qunatity with a value and a unit.
R = 1 * u.au      # radius of the Earth's orbit around the Sun in astronomical unit
V = orbita_velocity(M, R) 
print(V.to(u.km/u.s))

'''calculating the orbital velocity of a satellite around the Earth'''
M_Earth = 1 * u.earthMass
R_Satellite = 1 * u.earthRad
V_Satellite = orbital_velocity(M_Earth, R_Satellite)
print(V_Satellite.to(u.km/u.s))

'''calculating the Schwarzschild radius of a solar-mass blackhole'''
M = 1 * u.solMass
R_Schwarzschild = 2 * G * M / (const.c**2)
print(R_Schwarzschild.to(u.km))

'''calculating the rotation curve of a galaxy with only one central super-massive blackhole'''
mass_Black_Hole = 4.297e6 * u.solMass   # mass of the black hole
R_Array = np.arange(1, 30) * u.au       # array of numbers from 1 to 30
orbitalVelocities_Black_Hole = orbital_velocity(mass_Black_Hole, R_Array)
print(orbitalVelocities_Black_Hole.to(u.km/u.s))


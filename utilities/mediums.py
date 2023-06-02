from utilities.constants import (Density, Longitudinal_velocity, Shear_velocity)
class Medium():
	def __init__(self, density: Density, longitudinal_velocity: Longitudinal_velocity, shear_velocity: Shear_velocity):
		self.density = density
		self.longitudinal_velocity = longitudinal_velocity
		self.shear_velocity = shear_velocity
	def get_longitudinal_impedance(self) -> float:
		return self.density.value * self.longitudinal_velocity.value
	def get_shear_impedance(self) -> float : 
		return self.density.value*self.shear_velocity.value

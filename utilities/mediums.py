from utilities.constants import (Density, LongitudinalVelocity, ShearVelocity)
class Medium():
	def __init__(self, density: float, longitudinal_velocity: float, shear_velocity: float):
		self.density = density
		self.longitudinal_velocity = longitudinal_velocity
		self.shear_velocity = shear_velocity
	def get_longitudinal_impedance(self) -> float:
		return self.density * self.longitudinal_velocity
	def get_shear_impedance(self) -> float : 
		return self.density*self.shear_velocity

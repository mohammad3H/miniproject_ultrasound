from utilities.constants import (Density, LongitudinalVelocity, ShearVelocity)
class Medium():
	def __init__(self, density: float, longitudinal_velocity: float, shear_velocity: float, name: str):
		self.density = density
		self.longitudinal_velocity = longitudinal_velocity
		self.shear_velocity = shear_velocity
		self.name = name
	def get_longitudinal_impedance(self) -> float:
		return self.density * self.longitudinal_velocity
	def get_shear_impedance(self) -> float : 
		return self.density*self.shear_velocity
	def get_name(self) -> str:
		return self.name
	def get_density(self) -> float:
		return self.density
	def get_shear_velocity(self):
		return self.shear_velocity
	def get_longitudinal_velocity(self):
		return self.longitudinal_velocity

# this function will return a list of mediums that have non null properties
def get_mediums_list():
	densities = {}
	shear_velocities = {}
	longitudinal_velocities = {}
	list_of_mediums = []
	#put all materuals in dictionaries associating the medium name to the the constants
	for density in Density:
		densities[density.name] = density.value
	for shear_velocity in ShearVelocity:
		shear_velocities[shear_velocity.name] = shear_velocity.value
	for longitudinal_velocity in LongitudinalVelocity:
		longitudinal_velocities[longitudinal_velocity.name] = longitudinal_velocity.value
  
	# i now have a list of all te mediums
	for key in densities.keys():
		density_key = densities.get(key)
		shear_key = shear_velocities.get(key)
		long_key = longitudinal_velocities.get(key)
		if density_key and shear_key and long_key:
			list_of_mediums.append(Medium(densities[key], shear_velocities[key], longitudinal_velocities[key], key))
	return list_of_mediums

def get_sorted_medium_list():
	medium_list = get_mediums_list()
	sorted_objects = sorted(medium_list, key=lambda obj: obj.get_density())
	return sorted_objects

def get_air():
	return Medium(Density.Air.value, LongitudinalVelocity.Air.value, ShearVelocity.Air.value, 'AIR')
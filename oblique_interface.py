import math
from utilities.mediums import (Medium, get_sorted_medium_list, get_air)
from utilities.constants import PropagationMode

def _get_angle(snell_factor: float, velocity: float) -> float:
	# in this function snell factor is used to get all 4 angles on the interface using the incidemt angle, and the
	# mode velocities.
	return math.asin(snell_factor * velocity)

class ObliqueInterface():
	# all angles in radians
	def __init__(self, medium1: Medium, medium2: Medium, propagation_mode: PropagationMode, incidence_angle: float):
		self.medium1 = medium1
		self.medium2 = medium2
		self.incidence_propagation_mode = propagation_mode
		self.incidence_angle = incidence_angle
		# snell factor is the vlue of sin(angle) devided by the speed of the wave in the medium
		snell_factor = math.sin(incidence_angle)/medium1.get_shear_velocity()
		self.transversal_refracted_angle = _get_angle(snell_factor, medium1.get_shear_velocity())
		self.longitudinal_refracted_angle = _get_angle(snell_factor, medium1.get_longitudinal_velocity())
		self.transversal_transmited_angle = _get_angle(snell_factor, medium2.get_shear_velocity())
		self.longitudinal_transmited_angle = _get_angle(snell_factor, medium2.get_longitudinal_velocity())

		# now we define the matrix M : Mx = a
		# a is the incident light vector that changes from transversal to longitudinal modes
		# x is the outputed energy of the 4 waves normalized eq 5.21
		# in M we have some constants: k1L, k2L, k1T, k2T lambda 1 et 2, mu 1 et 2

		# lambda + 2 mu = rheau *cl^2
		# mu = rheau * ct^2
		# k = w/cl
		# w = 2 pi f
		def get_general_matrix():
			return(
				[
					[
						-1*math.cos(self.longitudinal_refracted_angle),
						math.sin(self.transversal_refracted_angle),
						-1*math.cos(self.longitudinal_transmited_angle),
						math.sin(self.transversal_transmited_angle)
					],
					[
						-1*math.sin(self.longitudinal_refracted_angle),
						-1*math.cos(self.transversal_refracted_angle),
						math.sin(self.longitudinal_transmited_angle),
						math.cos(self.transversal_transmited_angle)
					],
					[

					]
				]
			)




	
	def get_interface_characteristics(self) -> dict:
		characteristics = {}
		characteristics['medium1_name'] = self.medium1.get_name()
		characteristics['medium2_name'] = self.medium2.get_name()
		characteristics['medium1_density'] = self.medium1.get_density()
		characteristics['medium2_density'] = self.medium2.get_density()
		characteristics['medium1_impedance'] = self.medium1.get_longitudinal_impedance()
		characteristics['medium2_impedance'] = self.medium2.get_longitudinal_impedance()
		characteristics['reflexion_ratio'] = self.get_normal_reflexion_ratio()
		characteristics['transmission_ratio'] = self.get_normal_transmission_ratio()

		return characteristics
# this function creates the interfaces between air and the mediums and retunrn the rormal reflexion
# and transmissions ratios in order to be plotted
def get_air_solid_sorted_interfaces():
	air = get_air()
	interfaces = []
	mediums = get_sorted_medium_list()
	for medium in mediums:
		interfaces.append(MediumsInterface(air, medium, PropagationMode.Longitudinal))
	return interfaces

def get_solid_air_sorted_interfaces():
	air = get_air()
	interfaces = []
	mediums = get_sorted_medium_list()
	for medium in mediums:
		interfaces.append(MediumsInterface(medium, air, PropagationMode.Longitudinal))
	return interfaces

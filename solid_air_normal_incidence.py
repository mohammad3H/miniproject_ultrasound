from utilities.mediums import (Medium, get_sorted_medium_list, get_air)
from utilities.constants import PropagationMode

class MediumsInterface():
	def __init__(self, medium1: Medium, medium2: Medium, propagation_mode: PropagationMode):
		self.medium1 = medium1
		self.medium2 = medium2
		self.propagation_mode = propagation_mode

	def get_normal_reflexion_ratio(self):
		if self.propagation_mode == PropagationMode.Longitudinal:
			r = self.medium2.get_longitudinal_impedance()/self.medium1.get_longitudinal_impedance()
		if self.propagation_mode == PropagationMode.Shear:
			r = self.medium2.get_shear_impedance()/self.medium1.get_shear_impedance()
		return ((r - 1) / (r + 1)) ** 2
	
	def get_normal_transmission_ratio(self):
		if self.propagation_mode == PropagationMode.Longitudinal:
			r = self.medium2.get_longitudinal_impedance()/self.medium1.get_longitudinal_impedance()
		if self.propagation_mode == PropagationMode.Shear:
			r = self.medium2.get_shear_impedance()/self.medium1.get_shear_impedance()
		return ((4 * r) / (r + 1) ** 2)
	
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


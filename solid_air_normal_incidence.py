from utilities.mediums import Medium
from utilities.constants import PropagationMode

class Interface():
	def __init__(self, medium1: Medium, medium2: Medium, propagation_mode: PropagationMode):
		self.medium1 = medium1
		self.medium2 = medium2
		self.propagation_mode = propagation_mode
		
	def get_normal_reflexion_ratio(self):
		if self.propagation_mode == PropagationMode.Longitudinal:
			r = self.medium2.get_longitudinal_impedance()/self.medium1.get_longitudinal_impedance()
		if self.propagation_mode == PropagationMode.Longitudinal:
			r = self.medium2.get_shear_impedance()/self.medium1.get_shear_impedance()
		return ((r - 1) / (r + 1))^2
	
	def get_normal_transmission_ratio(self):
		if self.propagation_mode == PropagationMode.Longitudinal:
			r = self.medium2.get_longitudinal_impedance()/self.medium1.get_longitudinal_impedance()
		if self.propagation_mode == PropagationMode.Longitudinal:
			r = self.medium2.get_shear_impedance()/self.medium1.get_shear_impedance()
		return ((2 * r) / (r + 1))^2


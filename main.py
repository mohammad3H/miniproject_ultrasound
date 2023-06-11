from solid_air_normal_incidence import (MediumsInterface, get_air_solid_sorted_interfaces)
from utilities.plotting import plot
# aluminum = Medium(Density.Aluminum, LongitudinalVelocity.Aluminum, ShearVelocity.Aluminum)
# air = Medium(Density.Air, LongitudinalVelocity.Air, ShearVelocity.Air)

# air_solid = SolidAirInterface(air, aluminum, PropagationMode.Longitudinal)
# print(air_solid.get_normal_reflexion_ratio())

# print(air_solid.get_normal_transmission_ratio())

# get all interfaces
air_solid_interfaces = get_air_solid_sorted_interfaces()
# save all the reflexion and transmission coefficients in a list of tuples
air_solid_characteristics = []
for interface in air_solid_interfaces:
    air_solid_characteristics.append(interface.get_interface_characteristics())

reflexion_coefficients = [interface['reflexion_ratio'] for interface in air_solid_characteristics]
transmission_coefficients = [interface['transmission_ratio'] for interface in air_solid_characteristics]
medium_impedances = [interface['medium2_impedance'] for interface in air_solid_characteristics]
densities = [interface['medium2_density'] for interface in air_solid_characteristics]

plot(reflexion_coefficients, densities, 'r_coef_density')
plot(transmission_coefficients, densities, 'r_t_coef_density', False)
plot(transmission_coefficients, densities, 't_coef_density')

plot(reflexion_coefficients, medium_impedances, 'r_coef_impedance')
plot(transmission_coefficients, medium_impedances, 'r_t_coef_impedance', False)
plot(transmission_coefficients, medium_impedances, 't_coef_impedance')

# plot(reflexion_coefficients, medium_impedances, 'r_coef_impedance', clear=False)
# plot(transmission_coefficients, medium_impedances, 'r_t_coef_impedance')

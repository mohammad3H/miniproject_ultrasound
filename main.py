from solid_air_normal_incidence import SolidAirInterface
from utilities.mediums import Medium
from utilities.constants import (Density, LongitudinalVelocity, ShearVelocity, PropagationMode)

# aluminum = Medium(Density.Aluminum, LongitudinalVelocity.Aluminum, ShearVelocity.Aluminum)
# air = Medium(Density.Air, LongitudinalVelocity.Air, ShearVelocity.Air)

# air_solid = SolidAirInterface(air, aluminum, PropagationMode.Longitudinal)
# print(air_solid.get_normal_reflexion_ratio())

# print(air_solid.get_normal_transmission_ratio())

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

for key in densities.keys():
    density_key = densities.get(key)
    print('this is density key '+str(density_key))
    shear_key = shear_velocities.get(key)
    print('this is shear key '+str(shear_key))
    long_key = longitudinal_velocities.get(key)
    print('this is long key '+str(long_key))
    if density_key and shear_key and long_key:
        list_of_mediums.append(Medium(densities[key], shear_velocities[key], longitudinal_velocities[key]))

for medium in list_of_mediums:
    print(medium.get_longitudinal_impedance())
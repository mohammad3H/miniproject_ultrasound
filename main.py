from solid_air_normal_incidence import SolidAirInterface
from utilities.mediums import Medium
from utilities.constants import (Density, LongitudinalVelocity, ShearVelocity, PropagationMode)

aluminum = Medium(Density.Aluminum, LongitudinalVelocity.Aluminum, ShearVelocity.Aluminum)
air = Medium(Density.Air, LongitudinalVelocity.Air, ShearVelocity.Air)

air_solid = SolidAirInterface(air, aluminum, PropagationMode.Longitudinal)
print(air_solid.get_normal_reflexion_ratio())

print(air_solid.get_normal_transmission_ratio())
from enum import Enum

class Density(Enum):
    AIR = 0.001
    Aluminum = 2.7

class Longitudinal_velocity(Enum):
    Air = 330
    Aluminum = 6250

class Shear_velocity(Enum):
    Air = None
    Aluminum = 3100
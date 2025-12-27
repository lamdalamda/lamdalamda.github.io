from  matplotlib import pyplot  as plt
import numpy as np



electron_mass=9.10938356*(10**(-31))
k=9*(10**9)
electron_charge=-1.602*(10**-19)
class electron(object):
    def __init__(self,position=(0,0.1),charge=electron_charge,speed=(500,500)):
        self.position = position
        self.charge = charge
        self.speed=(500,500)
        self.mass=electron_mass
class atom(object):
    def __init__(self,position=(0,0),charge=-2*electron_charge):
        self.position = position
        self.charge = charge


class space(object):
    # traditional
    def __init__(self,objects=[atom(),electron()],timestep=10^(-10)):
        self.objects = objects
        self.timestep = timestep
    
    def calculate_force(self,object1=atom(),object2=electron()):
        force=
    
    def calculate_acceleration(self,object1=atom(),object2=electron()):
        
    def traditional_step(self):
        
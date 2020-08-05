import numpy as np
class RigidBody():

    def __init__(self):
        self.mass = 1 # kg
        self.center_of_gravity = np.zeros(3)
        self.moment_of_inertia #relative to cog
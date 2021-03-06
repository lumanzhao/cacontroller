import rigid_body as rb
import numpy as np

class Vessel():

    def __init__(self):
        self.rigid_body = rb.RigidBody()
        self.added_mass_matrix = np.zeros((6,6))
        self.damping_matrix = np.zeros((6,6))
import rigid_body as rb
import actor
import numpy as np

class Vessel(actor.Actor):

    def __init__(self):
        super().__init__()
        self.rigid_body = rb.RigidBody()
        self.added_mass_matrix = np.zeros((6,6))
        self.first_order_damping_matrix = np.zeros((6,6))
        self.second_order_damping_matrix = np.zeros((6,6))

    def get_damping_force_and_torque(self):
        velocity_translational_model_frame, velocity_rotational_model_frame = self.rigid_body.get_velocity_model_frame()
        damping_force_and_torque = self.first_order_damping_matrix * np.concatenate(velocity_translational_model_frame, velocity_rotational_model_frame) # questionable
        return 
    def update(self, dt : float):

    
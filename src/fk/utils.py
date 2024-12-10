import numpy as np

class Robot:
    """
    A class to represent a robot with base position, rotation, and Denavit-Hartenberg parameters.
    """
    def __init__(self, base_position=[0, 0, 0], base_orientation=[0, 0, 0, 1]):
        """
        Initialize the Robot.

        Args:
            base_position (list): The base position of the robot [x, y, z].
            base_rotation (list): The base rotation of the robot specified as a quaternion.
            dh_params (list): A list of DH parameters, where each entry is [a, d, alpha, theta].
        """
        self.base_position = np.array(base_position)
        self.base_rotation = self.quaternion_to_rotation_matrix(base_orientation)
        self.dh_params = [
            {"a": 0, "d": 0.4, "alpha": np.pi/2, "theta": np.pi/2},
            {"a": 0.4, "d": 0, "alpha": -np.pi/2, "theta": 0},
            {"a": 0, "d": 0, "alpha": -np.pi/2, "theta": -np.pi/2},
            {"a": 0, "d": 0, "alpha": np.pi/2, "theta": 0}
        ]
    
    def quaternion_to_rotation_matrix(self, q):
        """
        Convert a quaternion [x, y, z, w] to a 3x3 rotation matrix.

        Args:
            q (list or np.array): Quaternion [x, y, z, w].

        Returns:
            np.array: A 3x3 rotation matrix.
        """
        x, y, z, w = q
        return np.array([
            [1 - 2*(y**2 + z**2), 2*(x*y - z*w), 2*(x*z + y*w)],
            [2*(x*y + z*w), 1 - 2*(x**2 + z**2), 2*(y*z - x*w)],
            [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x**2 + y**2)]
        ])

    @staticmethod
    def homogeneous_transform(a, d, alpha, theta):
        """
        Compute the Denavit-Hartenberg transformation matrix.

        Args:
            a (float): Link length.
            d (float): Link offset.
            alpha (float): Link twist.
            theta (float): Joint angle.

        Returns:
            np.array: The 4x4 homogeneous transformation matrix.
        """
        ct = np.cos(theta)
        st = np.sin(theta)
        ca = np.cos(alpha)
        sa = np.sin(alpha)
        return np.array([
            [ct, -st*ca, st*sa, a*ct],
            [st, ct*ca, -ct*sa, a*st],
            [0, sa, ca, d],
            [0, 0, 0, 1]
        ])

    def calc_fk(self, q):
        """
        Calculate the forward kinematics of the robot.

        Returns:
            np.array: The overall transformation matrix from world frame to the end effector.
        """
        # Start with the identity matrix
        T_base = np.eye(4)

        # Apply base translation and rotation
        T_base[:3, 3] = self.base_position
        T_base[:3, :3] = self.base_rotation

        # Initialize the transformation matrix
        transform = T_base

        # Loop through each DH parameter set to compute the chain of transformations given the joint angles
        for i, params in enumerate(self.dh_params):
            if i <= 2: # Revolute joints
                T_i = self.homogeneous_transform(params["a"], params["d"], params["alpha"], params["theta"] + q[i])
            else: # Prismatic joint
                T_i = self.homogeneous_transform(params["a"], params["d"] + q[i], params["alpha"], params["theta"])
            transform = transform @ T_i
        return np.round(transform, 3)

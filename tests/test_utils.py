import pytest
import numpy as np
from fk.utils import Robot

def test_quaternion_to_rotation_matrix():
    """
    Test the quaternion_to_rotation_matrix method.
    """
    # Input quaternion [x, y, z, w]
    q = [0, 0, np.sqrt(0.5), np.sqrt(0.5)]  # 90-degree rotation about the Z-axis
    robot = Robot()
    rotation_matrix = robot.quaternion_to_rotation_matrix(q)

    # Expected rotation matrix (90-degree rotation about Z-axis)
    expected = np.array([
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ])
    assert np.allclose(rotation_matrix, expected, atol=1e-3)
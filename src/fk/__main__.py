from .utils import Robot

def main():
    """Main entry point for the program."""
    robot = Robot()
    print(robot.forward_kinematics([0, 0, 0, 0]))

if __name__ == "__main__":
    main()
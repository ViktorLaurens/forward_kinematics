from .utils import Robot

def main():
    """Main entry point for the program."""
    robot = Robot()
    print(robot.calc_fk([0, 0, 0, 0.2]))

if __name__ == "__main__":
    main()
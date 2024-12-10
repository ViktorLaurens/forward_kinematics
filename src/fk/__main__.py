import numpy as np
from .utils import Robot

def main():
    """
    Terminal program to calculate the forward kinematics of the robot.
    """

    # Create the Robot instance
    robot = Robot()

    print("\nWelcome to the Robot Forward Kinematics Calculator!")

    while True:
        print("\nMenu:")
        print("1. Input joint values (theta1 to theta4) and calculate FK")
        print("2. Exit")
        
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            try:
                # Prompt user for joint values
                theta1 = float(input("Enter theta1 (in radians): "))
                theta2 = float(input("Enter theta2 (in radians): "))
                theta3 = float(input("Enter theta3 (in radians): "))
                theta4 = float(input("Enter theta4 (prismatic joint displacement): "))

                # Calculate forward kinematics
                q = [theta1, theta2, theta3, theta4]
                fk_transform = robot.calc_fk(q)

                # Display the result
                print("\nForward Kinematics Transformation Matrix:\n")
                print(fk_transform)

            except ValueError:
                print("\nInvalid input. Please enter numerical values for the joint angles.\n")
        elif choice == "2":
            print("\nExiting the program. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please select 1 or 2.\n")

if __name__ == "__main__":
    main()
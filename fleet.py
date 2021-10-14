from robots import Robot
from weapons import Weapon 
class Fleet:
    def __init__(self):
        self.robot = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot("Drake")
        robot2 = Robot("Cole")
        robot3 = Robot("Keem")
        self.robot.append(robot1)
        self.robot.append(robot2)
        self.robot.append(robot3)
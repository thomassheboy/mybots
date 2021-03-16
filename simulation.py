from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time


class SIMULATION:
    def __init__(self):
        #Connect to Physics cloent
        self.physicsClient = p.connect(p.GUI)

        #Set up path for generating a floor
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        #Add Gravity to simulation
        p.setGravity(0, 0, -9.8)


    def RUN(self):
        #For loop for simulation
        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1/60)

    def __del__(self):
        p.disconnect()
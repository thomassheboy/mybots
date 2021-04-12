from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time


class SIMULATION:
    def __init__(self,arg,solutionID):
        #Connect to Physics cloent

        if arg == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif arg == "GUI":
            self.physicsClient = p.connect(p.GUI)
        #Set up path for generating a floor
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.directOrGUI = arg
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

        #Add Gravity to simulation
        p.setGravity(0, 0, -9.8)


    def RUN(self):
        #For loop for simulation
        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if(self.directOrGUI == "GUI"):
                time.sleep(1/100000)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
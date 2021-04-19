from motor import MOTOR
from sensor import SENSOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c


class ROBOT:
    def __init__(self,solutionID):
        self.sensors = {}
        self.solutionID = solutionID
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) +".nndf")
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        # os.system("del brain" + str(solutionID) + ".nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    def Sense(self,t):
        #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
        for i in self.sensors:
            self.sensors[i].Get_Value(t)


    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)


    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                desiredAngle *= c.motorJointRange
                self.motors[jointName].Set_Value(self.robot, desiredAngle)


    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)

        basePosition = basePositionAndOrientation[0]

        xPosition = basePosition[0]


        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xPosition))
        # os.rename("tmp" + str(self.solutionID) + ".txt" , "fitness" + str(self.solutionID) + ".txt")

        f.close()
        os.system("rename tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
        # exit()
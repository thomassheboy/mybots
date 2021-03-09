import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = numpy.zeros(1000)
        self.values = numpy.linspace(-numpy.pi, numpy.pi, 1000)
        self.frequency = c.fbl
        if self.jointName == "Torso_Front_Leg":
            self.frequency /= 2
        self.amplitude = c.abl
        self.offset = c.pbl
        for i in range(1000):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency * self.values[i] + self.offset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition= self.motorValues[t],
            maxForce=500)

    def Save_Values(self):
        numpy.save("data/motorValues.npy", self.motorValues)


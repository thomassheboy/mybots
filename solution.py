import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.Generate_Body()
        self.Create_World()
        self.Generate_Brain()

    def Set_ID(self):
        self.myID += 1

    def Evaluate(self,decision):
        string = "py simulate.py " + decision + " " + str(self.myID)
        os.system("START /B " + string)
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        self.fitness = float(fitnessFile.read())
        print(self.fitness)
        fitnessFile.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Start_Simulation(self, decision):
        string = "py simulate.py " + decision + " " + str(self.myID)
        os.system("START /B " + string)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        #print(self.fitness)
        os.system("del fitness" + str(self.myID) + ".txt")
        fitnessFile.close()
        # os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
        self.Generate_Brain()

    def Create_World(self):
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = height/2
        # while not os.path.exists("world.sdf"):
        #     time.sleep(0.01)
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y + 2, z, 0], size=[length,width,height])
        pyrosim.End()
        # while not os.path.exists("world.sdf"):
        #     time.sleep(0.01)

    def Generate_Body(self):
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 1
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
        pyrosim.Start_URDF("body.urdf")
        #Torso
        pyrosim.Send_Cube(name="Torso",pos=[x, y, z, 0], size=[length,width,height])
        #Torso - Front
        pyrosim.Send_Joint(name = "Torso_Front_Leg", parent = "Torso" ,
                           child = "Front_Leg", type = "revolute" , position = "0 .5 1",jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="Front_Leg",pos=[0, .5, 0, 0], size=[0.2,1,0.2])
        #Torso - Back
        pyrosim.Send_Joint(name = "Torso_Back_Leg", parent = "Torso" ,
                           child = "Back_Leg", type = "revolute" , position = "0 -.5 1", jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="Back_Leg",pos=[0, -.5, 0, 0], size=[0.2,1,0.2])
        #Torso - Left
        pyrosim.Send_Joint(name = "Torso_Left_Leg", parent = "Torso" ,
                           child = "Left_Leg", type = "revolute" , position = "-.5 0 1",jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="Left_Leg",pos=[-.5, 0, 0, 0], size=[1,0.2,0.2])
        #Torso - Right
        pyrosim.Send_Joint(name = "Torso_Right_Leg", parent = "Torso" ,
                           child = "Right_Leg", type = "revolute" , position = ".5 0 1",jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="Right_Leg",pos=[.5, 0, 0, 0], size=[1,0.2,0.2])

        #LeftLeg - Lower Leg
        pyrosim.Send_Joint(name = "Left_Leg_Lower_Left_Leg", parent = "Left_Leg" ,
                           child = "Lower_Left_Leg", type = "revolute" , position = "-1 -.5 -.5",jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="Lower_Left_Leg",pos=[0, .5, 0, 0], size=[0.2,0.2,1])

        #RightLeg - Lower Leg
        pyrosim.Send_Joint(name = "Right_Leg_Lower_Right_Leg", parent = "Right_Leg" ,
                           child = "Lower_Right_Leg", type = "revolute" , position = "1 0 -.5",jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="Lower_Right_Leg",pos=[0, 0, 0, 0], size=[0.2,0.2,1])

        #FrontLeg - Lower Leg
        pyrosim.Send_Joint(name = "Front_Leg_Lower_Front_Leg", parent = "Front_Leg" ,
                           child = "Lower_Front_Leg", type = "revolute" , position = "0 1 0",jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="Lower_Front_Leg",pos=[0, 0, -.5, 0], size=[0.2,0.2,1])
        #BackLeg - Lower Leg
        pyrosim.Send_Joint(name = "Back_Leg_Lower_Back_Leg", parent = "Back_Leg" ,
                           child = "Lower_Back_Leg", type = "revolute" , position = "0 -1 0",jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="Lower_Back_Leg",pos=[0, 0, -.5, 0], size=[0.2,0.2,1])

        pyrosim.End()
        # while not os.path.exists("body.urdf"):
        #     time.sleep(0.01)

    def Generate_Brain(self):
        # while not os.path.exists("brain" + str(self.myID) + ".nndf"):
        #     time.sleep(0.01)
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Front_Leg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Back_Leg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Left_Leg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Right_Leg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "Lower_Front_Leg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "Lower_Back_Leg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "Lower_Left_Leg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "Lower_Right_Leg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_Back_Leg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_Front_Leg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_Left_Leg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_Right_Leg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Back_Leg_Lower_Back_Leg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Front_Leg_Lower_Front_Leg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Left_Leg_Lower_Left_Leg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Right_Leg_Lower_Right_Leg")
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = .10 )
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = .10 )

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight=self.weights[currentRow][currentColumn] )

        pyrosim.End()
        # while not os.path.exists("brainID.nndf"):
        #     time.sleep(0.01)

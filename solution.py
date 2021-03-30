import numpy
import pyrosim.pyrosim as pyrosim
import os
import random


class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.Generate_Brain()

    def Evaluate(self,decision):
        string = "py simulate.py " + decision
        os.system(string)
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
        self.Generate_Brain()

    def Create_World(self):
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = height/2
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y + 2, z, 0], size=[length,width,height])
        pyrosim.End()

    def Generate_Body(self):
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = height/2
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso",pos=[x, y, 1.5, 0], size=[length,width,height])
        pyrosim.Send_Joint(name = "Torso_Front_Leg", parent = "Torso" ,
                           child = "Front_Leg", type = "revolute" , position = ".5 0 1")
        pyrosim.Send_Cube(name="Front_Leg",pos=[.5, 0, -.5, 0], size=[length,width,height])
        pyrosim.Send_Joint(name = "Torso_Back_Leg", parent = "Torso" ,
                           child = "Back_Leg", type = "revolute" , position = "-.5 0 1")
        pyrosim.Send_Cube(name="Back_Leg",pos=[-.5, 0, -.5, 0], size=[length,width,height])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Front_Leg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Back_Leg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Back_Leg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Front_Leg")
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = .10 )
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = .10 )

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight=self.weights[currentRow][currentColumn] )

        pyrosim.End()

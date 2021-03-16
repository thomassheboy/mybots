import pyrosim.pyrosim as pyrosim

#pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = height/2

#pyrosim.Send_Cube(name="Box",pos=[x, y, z, 0], size=[length,width,height])
#pyrosim.Send_Cube(name="Box2",pos=[x + length, y, z * 3, 0], size=[length,width,height])

#Commented Out for simplicity
# for k in range(10):
#     for i in range(10):
#         for j in range(10):
#             pyrosim.Send_Cube(name="Box",pos=[x + i, y + j, z, 0], size=[length,width,height])
#     length *= .9
#     width *= .9
#     height *= .9
#     z = z + height

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box",pos=[x, y + 2, z, 0], size=[length,width,height])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso",pos=[x, y, 1.5, 0], size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_Front_Leg", parent = "Torso" ,
                       child = "Front_Leg", type = "revolute" , position = ".5 0 1")
    pyrosim.Send_Cube(name="Front_Leg",pos=[.5, 0, -.5, 0], size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_Back_Leg", parent = "Torso" ,
                       child = "Back_Leg", type = "revolute" , position = "-.5 0 1")
    pyrosim.Send_Cube(name="Back_Leg",pos=[-.5, 0, -.5, 0], size=[length,width,height])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Front_Leg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Back_Leg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Back_Leg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Front_Leg")
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()
#pyrosim.End()
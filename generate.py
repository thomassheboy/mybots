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

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso",pos=[x, y, 1.5, 0], size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_Front_Leg", parent = "Torso" ,
                       child = "Front_Leg", type = "revolute" , position = ".5 0 1")
    pyrosim.Send_Cube(name="Front_Leg",pos=[.5, 0, -.5, 0], size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_Back_Leg", parent = "Torso" ,
                       child = "Back_Leg", type = "revolute" , position = "-.5 0 1")
    pyrosim.Send_Cube(name="Back_Leg",pos=[-.5, 0, -.5, 0], size=[length,width,height])
    pyrosim.End()

Create_World()
Create_Robot()
#pyrosim.End()
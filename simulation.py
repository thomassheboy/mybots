import pybullet as p
import time
import pybullet_data

#Connect to Physics cloent
physicsClient = p.connect(p.GUI)

#Set up path for generating a floor
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Add Gravity to simulation
p.setGravity(0,0,-9.8)

#load a floor
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

#load box.sdf
p.loadSDF("world.sdf")

#For loop for simulation
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)

#Disconnect
p.disconnect()

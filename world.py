import pybullet as p
import pybullet_data

class WORLD:
    def __init__(self):

        self.planeID = p.loadURDF("plane.urdf")
        #load box.sdf
        p.loadSDF("world.sdf")
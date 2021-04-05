from solution import SOLUTION
import constants
import copy
import constants as c
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del tmp*.txt")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        # for i in range(c.populationSize):
        #     self.parents[i].Start_Simulation("DIRECT")
        # for i in range(c.populationSize):
        #     self.parents[i].Wait_For_Simulation_To_End()
        self.Evaluate(self.parents)

    # self.parent.Evaluate("GUI")
        numberOfGenerations = constants.numGen
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID()


    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()

    def Select(self):
        for i in range(len(self.children)):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        for i in range(len(self.children)):
            print("\nP: ", self.parents[i].fitness, " C: ", self.children[i].fitness,"\n")

    def Show_Best(self):
        mini = 0.0
        for i in range (1, len(self.parents) - 1):
            if self.parents[i].fitness < self.parents[mini].fitness:
                mini = i
        self.parents[mini].Start_Simulation("GUI")
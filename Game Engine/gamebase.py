import numpy as np

from PIL import Image

from matplotlib import pyplot as plt

import random

import math

import numpy as np

import sys

import player1, player2



class Map():

    def __init__(self):

        

        self.displaymap = np.load("Game Engine\gamemaps\\betamap2.npy")

        self.displaymap = np.load("Game Engine\gamemaps\\betamap2.npy")
        self.terrainmap = self.displaymap

        self.mapsizex = (self.displaymap).shape[1]

        self.mapsizey = (self.displaymap).shape[0]

        self.unitmap = np.zeros([self.mapsizey, self.mapsizex])



    

    def coordinateList(self):

        a = np.floor(np.arange(0,self.mapsizex*self.mapsizey,1) / (self.mapsizey))

        b = np.tile(np.arange(0,self.mapsizey,1),self.mapsizex)

        self.coordinateList = np.vstack((a,b)).T

        print(b)





    def showMap(self):



        self.displaymap = self.terrainmap * self.unitmap

        # Terrain types

        # 0 = fog

        # 1 = water

        # 2 = sand

        # 3 = grass1

        # 4 = grass2

        # 5 = stone1

        # 6 = stone2

        # 7 = stone3

        # 8 = stone4

        fogcolor = np.array([0,0,0])

        desertcolor = np.array([255, 255, 0])

        grasscolor = np.array([0, 255, 0])

        deepgrasscolor = np.array([0, 200, 0])

        stonecolor1 = np.array([128, 128, 128])

        stonecolor2 = np.array([160, 160, 160])

        stonecolor3 = np.array([180, 180, 180])

        stonecolor4 = np.array([200, 200, 200])

        watercolor = np.array([0, 0, 255])

        red_team_color = np.array([255, 0, 0])

        blue_team_color = np.array([128, 0, 200])



        imagearray = np.zeros([self.mapsizey, self.mapsizex, 3])

        currentx = 0

        currenty = 0

        while currenty < (self.displaymap).shape[0]:

            if self.displaymap[currenty, currentx] <= 0:

                imagearray[currenty, currentx, :] = fogcolor

            elif self.displaymap[currenty, currentx] <= 1:

                imagearray[currenty, currentx, :] = watercolor

            elif self.displaymap[currenty, currentx] <= 2:

                imagearray[currenty, currentx, :] = desertcolor

            elif self.displaymap[currenty, currentx] <= 3:

                imagearray[currenty, currentx, :] = grasscolor

            elif self.displaymap[currenty, currentx] <= 4:

                imagearray[currenty, currentx, :] = deepgrasscolor

            elif self.displaymap[currenty, currentx] <= 5:

                imagearray[currenty, currentx, :] = stonecolor1

            elif self.displaymap[currenty, currentx] <= 6:

                imagearray[currenty, currentx, :] = stonecolor2

            elif self.displaymap[currenty, currentx] <= 7:

                imagearray[currenty, currentx, :] = stonecolor3

            elif self.displaymap[currenty, currentx] <= 8:

                imagearray[currenty, currentx, :] = stonecolor4
            elif self.displaymap[currenty, currentx] >= 10:
                imagearray[currenty, currentx, :] = red_team_color 
            currentx += 1

            if currentx == (self.displaymap).shape[1]:

                currentx = 0

                currenty += 1



        plt.imshow(imagearray.astype('uint8'))

        plt.show()



    def resetUnitMap(self):

        self.unitmap = np.zeros([self.mapsizey, self.mapsizex]) + 1



    def updateUnitMapWithPosition(self,unit):
        self.unitmap[unit.y,unit.x] = 0
    






    



class Game():

    def __init__(self):

        pass





class Team():

    def __init__(self, mapIn):

        self.visibleMap = np.zeros([mapIn.mapsizey, mapIn.mapsizex])

        self.fogOfWarMap = np.zeros([mapIn.mapsizey, mapIn.mapsizex])

        self.teamUnits = []

        self.visibleUnits = []    

        self.unit_color =   []    

    def lose():
        #TODO
        return False

    def get_castle(self):
        castle = self.teamUnits.__getitem__(type.__class__(Castle))

        if castle is None:
            print("no Castle found.")
        else:
            return castle


    def updateMap(self, mapIn):

        self.visibleMap = self.fogOfWarMap * mapIn.displaymap



    def createUnit(self,x,y,unitType):
        if(unitType == "worker"):
            self.teamUnits.append(Worker(x,y))
        if(unitType == "scout"):
            self.teamUnits.append(Scout(x,y))
        pass



    def showMap(self,mapIn):

        # Terrain types

        # 0 = fog

        # 1 = water

        # 2 = sand

        # 3 = grass1

        # 4 = grass2

        # 5 = stone1

        # 6 = stone2

        # 7 = stone3

        # 8 = stone4

        fogcolor = np.array([0,0,0])

        desertcolor = np.array([255, 255, 0])

        grasscolor = np.array([0, 255, 0])

        deepgrasscolor = np.array([0, 200, 0])

        stonecolor1 = np.array([128, 128, 128])

        stonecolor2 = np.array([160, 160, 160])

        stonecolor3 = np.array([180, 180, 180])

        stonecolor4 = np.array([200, 200, 200])

        watercolor = np.array([0, 0, 255])

        red_team_color = np.array([255, 0, 0]) 

        blue_team_color = np.array([128, 0, 200])



        imagearray = np.zeros([mapIn.mapsizey, mapIn.mapsizex, 3])

        currentx = 0

        currenty = 0

        while currenty < (self.visibleMap).shape[0]:

            if self.visibleMap[currenty, currentx] <= 0:

                imagearray[currenty, currentx, :] = fogcolor

            elif self.visibleMap[currenty, currentx] <= 1:

                imagearray[currenty, currentx, :] = watercolor

            elif self.visibleMap[currenty, currentx] <= 2:

                imagearray[currenty, currentx, :] = desertcolor

            elif self.visibleMap[currenty, currentx] <= 3:

                imagearray[currenty, currentx, :] = grasscolor

            elif self.visibleMap[currenty, currentx] <= 4:

                imagearray[currenty, currentx, :] = deepgrasscolor

            elif self.visibleMap[currenty, currentx] <= 5:

                imagearray[currenty, currentx, :] = stonecolor1

            elif self.visibleMap[currenty, currentx] <= 6:

                imagearray[currenty, currentx, :] = stonecolor2

            elif self.visibleMap[currenty, currentx] <= 7:

                imagearray[currenty, currentx, :] = stonecolor3

            elif self.visibleMap[currenty, currentx] <= 8:

                imagearray[currenty, currentx, :] = stonecolor4

            currentx += 1

            if currentx == (self.visibleMap).shape[1]:

                currentx = 0

                currenty += 1



        plt.imshow(imagearray.astype('uint8'))
        plt.draw()











        





# Class Hierarchy - Units:

# ------------------------

#                        GameObject

#                            |

#                       Units

#                  /           \

#        Utility Units       Combat Units

#          /    |               |      \    \       \

#       Worker Scout            Melee Tank Archer GlassCannon

#

# GameObject:    Base class for game objects with default health and canAttack attribute.

#

# Units:         Inherits from GameObject, represents units with default damage, speed, and cooldown.

#

# UtilityUnits:  Inherits from Units, represents utility units with the ability to attack.

#

# Worker:        Inherits from UtilityUnits, a specific type of utility unit with custom health, damage, speed, and cooldown.

#

# Scout:         Inherits from UtilityUnits, another type of utility unit with custom health, damage, speed, and no attack ability.

#

# CombatUnits:   Inherits from GameObject, represents combat units with default health.

#

# Melee:         Inherits from CombatUnits, a specific type of combat unit with custom health, damage, speed, and cooldown.

#

# Tank:          Inherits from CombatUnits, another type of combat unit with custom health, damage, speed, and cooldown.

#

# Archer:        Inherits from CombatUnits, a ranged combat unit with custom health, damage, speed, cooldown, and bulletSpeed.

#

# GlassCannon:   Inherits from CombatUnits, a specialized combat unit with low health, high damage, speed, cooldown, and bulletSpeed.





class GameObject():

    defaultHealth = 10

    x = 0

    y = 0

    canAttack = False

    dead = False
    
    possible_actions = set()



    def __init__(self, x, y):

        
        self.health = self.defaultHealth

        self.x = x

        self.y = y

        self.action_queue = []



    def _lose_health(self, damage):

        self.health -= damage

        if (self.health <= 0):

            dead = True



    def add_to_queue(self, action):
        
        if action not in self.possible_actions:
            print("Not in possible actions")
        else:
            self.action_queue.append(action)



    def _execute_next_action(self):

        """Execute the next action in the queue, if any."""

        if self.action_queue:
            
            action = self.action_queue.pop(0)

            # Here, add code to perform the action

        else:

            print("no actions to execute.")





class Units(GameObject):



    def __init__(self, x, y, team):

        super().__init__(x,y)

        possible_actions = {"move_up","move_down","move_left","move_right"}

        self.team = team

        self.canAttack = True

        self.damage = 1

        self.speed = 1

        self.cooldown = 1

        self.range = 2

        self.vision_range = 4


    def move_up(self,mapIn):

        # if(mapIn[self.y-1,self.x]==1):

            self.y-=1



    def move_down(self,mapIn):

        # if(mapIn[self.y+1,self.x]==1):

            self.y+=1



    def move_right(self,mapIn):

        # if(mapIn[self.y,self.x+1]==1):

            self.x+=1



    def move_left(self,mapIn):

        # if(mapIn[self.y,self.x-1]==1):

            self.x-=1



    def move_to(self):

        pass



    def get_vision_coordinates(self):



        visioncoordinates = np.vstack((np.tile(np.arange(-self.vision_range,self.vision_range+1,1),self.vision_range*2+1),np.floor(np.arange(0,(self.vision_range*2+1)**2,1) / (self.vision_range*2+1)) - self.vision_range)).T


        print(visioncoordinates)



    def _attack(self, ennemy):

        # jsp quoi faire

        if (ennemy.pos < self.range):

            pass





class UtilityUnits(Units):

    def __init__(self, x, y):

        super().__init__(x,y)





class Worker(UtilityUnits):

    def __init__(self, x, y):

        super().__init__(x,y)

        self.x = x

        self.y = y

        self.health = 10

        self.damage = 1

        self.speed = 3

        self.cooldown = 2

    def _execute_next_action(self):

        """Execute the next action in the queue, if any."""

        if self.action_queue:
            
            action = self.action_queue.pop(0)

            if action == "move_up":
                self.move_up()
            elif action == "move_down":
                self.move_down()
            elif action == "move_left":
                self.move_left()
            elif action == "move_right":
                self.move_right
        else:

            print("no actions to execute.")





class Scout(UtilityUnits):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x

        self.y = y

        self.canAttack = False

        self.health = 10

        self.damage = 0

        self.speed = 10





class CombatUnits(GameObject):

    pass





class Melee(CombatUnits):

    def __init__(self, x, y, team):

        super().__init__(team)

        self.x = x

        self.y = y

        self.health = 20

        self.damage = 5

        self.speed = 5

        self.cooldown = 2





class Tank(CombatUnits):

    def __init__(self, x, y, team):

        super().__init__(team)

        self.x = x

        self.y = y

        self.health = 40

        self.damage = 5

        self.speed = 3

        self.cooldown = 3





class Archer(CombatUnits):

    def __init__(self, x, y, team):

        super().__init__(team)

        self.x = x

        self.y = y

        self.health = 15

        self.damage = 5

        self.speed = 5

        self.cooldown = 2

        self.bulletSpeed = 6





class GlassCannon(CombatUnits):

    def __init__(self, x, y, team):

        super().__init__(team)

        self.x = x

        self.y = y

        self.health = 5

        self.damage = 15

        self.speed = 10

        self.cooldown = 1

        self.bulletSpeed = 10





class Building(GameObject):

    size = 3

    x = 0

    y = 0



    def __init__(self):

        super().__init__()

        self.size = self.size

        self.x = self.x

        self.y = self.y





class Castle(Building):

    def __init__(self):
        self.possibleactions = {"create_worker","create_scout"}
        self.size = 6

        super().__init__()



    def CreateWorker(x, y, team):

        return Worker(x, y, team)



    def _CreateScout(x, y, team):

        return Scout(x, y, team)





def main():

    np.set_printoptions(threshold=sys.maxsize)





class Game:

    def __init__(self):

        self.game_map = Map()

        self.map_units = np.full((90, 160), None)

        self.map_terrain = np.zeros((90, 160), dtype=int)

        self.red_units = []

        self.blue_units = []

        self.team_red = Team(self.game_map)

        self.team_blue = Team(self.game_map)



    def update_game_state(self):
        self.game_map.updateUnitMapWithPosition
        self.game_map.resetUnitMap

         

    def check_win_condition(self):
        return self.team_red.lose() or self.team_blue.lose()

    def main_loop(self):
        
        game_over = self.check_win_condition()
        
        self.team_red.createUnit(27, 27, "castle")
        self.team_blue.createUnit(27, 77, "castle")

        while not game_over:
            player1.play(self.team_red)
            player2.play(self.team_blue)

            # Update game state
            self.update_game_state()

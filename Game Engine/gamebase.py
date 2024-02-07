import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import random 
import math
import numpy as np
import sys




class Map():
    def __init__(self):
        self.terrainmap = np.load("Game Engine/gamemaps/betamap2.npy")
        self.mapsizex = (self.terrainmap).shape[1]
        self.mapsizey = (self.terrainmap).shape[0]

        print(self.terrainmap)
    
    def showMap(self):

        # Terrain types
        # 1 = water
        # 2 = sand
        # 3 = grass1 
        # 4 = grass2
        # 5 = stone1
        # 6 = stone2
        # 7 = stone3
        # 8 = stone4
        
        desertcolor = np.array([255,255,0])
        grasscolor = np.array([0,255,0])
        deepgrasscolor = np.array([0,200,0])
        stonecolor1 = np.array([128,128,128])
        stonecolor2 = np.array([160,160,160])
        stonecolor3 = np.array([180,180,180])
        stonecolor4 = np.array([200,200,200])
        watercolor = np.array([0,0,255])

        imagearray = np.zeros([self.mapsizey, self.mapsizex,3])
        currentx = 0
        currenty = 0
        while currenty < (self.terrainmap).shape[0]:
            
            if self.terrainmap[currenty,currentx] <= 1:
                imagearray[currenty,currentx,:] = watercolor
            elif self.terrainmap[currenty,currentx] <= 2:
                imagearray[currenty,currentx,:] = desertcolor
            elif self.terrainmap[currenty,currentx] <= 3:
                imagearray[currenty,currentx,:] = grasscolor
            elif self.terrainmap[currenty,currentx] <= 4:
                imagearray[currenty,currentx,:] = deepgrasscolor
            elif self.terrainmap[currenty,currentx] <= 5:
                imagearray[currenty,currentx,:] = stonecolor1
            elif self.terrainmap[currenty,currentx] <= 6:
                imagearray[currenty,currentx,:] = stonecolor2
            elif self.terrainmap[currenty,currentx] <= 7:
                imagearray[currenty,currentx,:] = stonecolor3
            elif self.terrainmap[currenty,currentx] <= 8:
                imagearray[currenty,currentx,:] = stonecolor4
            currentx+=1
            if currentx==(self.terrainmap).shape[1]:
                currentx=0
                currenty+=1

        plt.imshow(imagearray.astype('uint8'))
        plt.show()

class Game():
    def __init__(self):
        
        pass

class Team():
    def __init__(self):
        pass

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

class GameObject:
    defaultHealth = 10
    x = 0
    y = 0
    canAttack = False
    dead=False
    

    def __init__(self, team):
        self.health = self.defaultHealth
        self.team = team
        
    
    def lose_health(self,damage):
        self.health-=damage
        if(self.health<=0):
            dead=True
    
    def add_to_queue(self,action):
        self.action_queue.append(action)
    
    def execute_next_action(self):
        """Execute the next action in the queue, if any."""
        if self.action_queue:
            action = self.action_queue.pop(0)
            
            # Here, add code to perform the action
        else:
            print("no actions to execute.")
            




class Units(GameObject):
    defaultDamage = 1
    defaultSpeed = 1
    defaultCooldown = 1
    
    def __init__(self, team):
        super().__init__(team)
        self.canAttack = True
        self.damage = self.defaultDamage
        self.speed = self.defaultSpeed
        self.cooldown = self.defaultCooldown
        self.action_queue = []
        
        
    
                         
class UtilityUnits(Units):
    pass

class Worker(UtilityUnits):
    def __init__(self, x, y, team):
        super().__init__(team)
        self.x = x
        self.y = y
        self.health = 10
        self.damage = 1
        self.speed = 3
        self.cooldown = 2

class Scout(UtilityUnits):
    def __init__(self, x, y, team):
        super().__init__(team)
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
    def __init__(self, red):
        if red:
            self.x = 0
            self.y = 0
        else:
            self.x = 50
            self.y = 50
        self.size = 6
        super().__init__()

    def CreateWorker(x, y, team):
        return Worker(x, y, team)

    def CreateScout(x, y, team):
        return Scout(x, y, team)






def main():
    np.set_printoptions(threshold=sys.maxsize)


   



class Game:
    def __init__(self):
        self.map_units = np.full((90, 160), None)
        self.map_terrain = np.zeros((90, 160), dtype=int)
        self.red_units = []
        self.blue_units = []

    def read_ai_input(self, ai_file):
        pass

    def update_game_state(self):
        pass
        

    def main_loop(self, red_ai_file, blue_ai_file):
        #temp
        game_over=False
        #temp
        while not game_over:
            # Read and execute commands for red team
            red_commands = self.read_ai_input(red_ai_file)
            

            # Read and execute commands for blue team
            blue_commands = self.read_ai_input(blue_ai_file)
            

            # Update game state
            self.update_game_state()

if __name__ == "__main__":
    main()
    game = Game()
    game.main_loop("red_ai.txt", "blue_ai.txt")

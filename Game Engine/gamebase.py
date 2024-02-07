import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import random 
import math
import sys



class Map():
    def __init__(self):
        self.terrainmap = np.load("./gamemaps/betamap2.npy")
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
    
class GameObject():
    defaultHealth = 10
    x=0
    y=0
    canAttack=False
    def __init__(self):
        self.health=self.defaultHealth
        

class Units(GameObject):
    defaultDamage=1
    defaultSpeed=1
    defaultCooldown=1
    def __init__(self):
        super().__init__()
        self.canAttack=True
        self.damage=self.defaultDamage
        self.speed=self.defaultSpeed
        self.cooldown=self.defaultCooldown

class UtilityUnits(Units):
    def __init__(self):
        super().__init__()
        

class Worker(UtilityUnits):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.health = 10
        self.damage = 1
        self.speed = 3
        self.cooldown= 2

class Scout(UtilityUnits):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.canAttack=False
        self.health = 10
        self.damage = 0
        self.speed = 10


        
class CombatUnits(GameObject):
    def __init__(self):
        super().__init__()


class Melee(CombatUnits):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.health = 20
        self.damage = 5
        self.speed = 5
        self.cooldown= 2


class Tank(CombatUnits):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.health = 40
        self.damage = 5
        self.speed = 3
        self.cooldown= 3


class Archer(CombatUnits):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.health = 15
        self.damage = 5
        self.speed = 5   
        self.cooldown= 2
        self.bulletSpeed=6

class GlassCannon(CombatUnits):       
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.health=5
        self.damage=15
        self.speed=10
        self.cooldown= 1
        self.bulletSpeed=10

# Class Hierarchy - Buildings:
# ----------------------------
#                        GameObject
#                            |
#                       Building
#                   /  |  |   |   \
#                Castle TrainingCamp Mine LumberMill Farm University
# 
# Building:      Inherits from GameObject, represents buildings with a default size.
# 
# Castle:        Inherits from Building, a specific type of building with a custom size.
# 
# TrainingCamp:  Inherits from Building, a building that can create units.
# 
# Mine:          Inherits from Building, a building that can generate resources.
# 
# LumberMill:    Inherits from Building, a building that can generate resources.
# 
# Farm:          Inherits from Building, a building that can generate resources.
# 
# University:    Inherits from Building, a building that can generate resources.
        
        
class Building(GameObject):
    size=3
    x=0
    y=0
    def __init__(self):
        self.size=self.size
        self.x=self.x
        self.y=self.y
        super().__init__()

#je ne sais pas encore la position des teams       
class Castle(Building):
    def __init__(self, red):
        if red:
            self.x=0
            self.y=0

        else:
         
            self.x=50
            self.y=50 
        
        self.size=6
        super().__init__()

    #UtilyUnits
    def CreateWorker(x,y):
        return Worker(x,y)
    def CreateScout(x,y):
        return Scout(x,y)
        
    #Buildings
    def CreateTrainingCamp(self,x,y):
        return TrainingCamp(x,y)
    def CreateMine(self,x,y):
        return Mine(x,y)
    def CreateLumberMill(self,x,y):
        return LumberMill(x,y)
    def CreateFarm(self,x,y):
        return Farm(x,y)
    def CreateUniversity(self,x,y):
        return University(x,y)
    
class TrainingCamp(Building):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y

    def CreateMelee(self):
        return Melee(self.x,self.y)
    def CreateTank(self):
        return Tank(self.x,self.y)
    def CreateArcher(self):
        return Archer(self.x,self.y)
    def CreateGlassCannon(self):
        return GlassCannon(self.x,self.y)
   
    


class Mine(Building):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y

class LumberMill(Building):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y

class Farm(Building):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y

class University(Building):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        
        
        
        
## game arrays

map_units=np.zeros((90,160))
map_terrain=np.zeros((90,160))
map_building=np.zeros((90,160))


def main():
    np.set_printoptions(threshold=sys.maxsize)
    
    
    while(True):
        print(map_units)
        
        
        ##print(map_terrain)
        ##print(map_building)
        
        
        
    
    
    
    
    
    

if __name__ == "__main__":
    main()
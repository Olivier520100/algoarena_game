import gamebase
import player1
import player2
import time 

print("starting")
gamemap = gamebase.Map()

# gamemap.coordinateList()
team1 = gamebase.Team(gamemap)
print("gamebase created")

# initial generation
gamemap.resetUnitMap()
gamemap.showMap()
print("map generated")

# creating units (testing only)
team1.createUnit(22,47, "worker")
team1.createUnit(24, 47, "scout")
print("units generated")
gamemap.showMap()
# gameloop
while (True):
    print("looping")
    gamemap.showMap()
    gamemap.resetUnitMap()
    for unit in team1.teamUnits:
        unit.move_up(gamemap)
        gamemap.updateUnitMapWithPosition(unit)
    team1.showMap(gamemap)

    

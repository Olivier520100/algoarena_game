import gamebase
import player1
import player2
gamemap = gamebase.Map()
# gamemap.coordinateList()
team1 = gamebase.Team(gamemap)
team1.createUnit(27,47,"worker")
gamemap.resetUnitMap()
gamemap.updateUnitMapWithPosition(team1.teamUnits[0])
gamemap.showMap()


while (True):
    team1.teamUnits[0].move_up(gamemap)
    print("1")
    gamemap.updateUnitMapWithPosition(team1.teamUnits[0])
    team1.showMap(gamemap)

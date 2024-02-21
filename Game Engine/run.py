import gamebase

gamemap = gamebase.Map()
# gamemap.coordinateList()
team1 = gamebase.Team(gamemap)
team1.createUnit(12,12,"worker")
gamemap.resetUnitMap()
gamemap.updateUnitMapWithPosition(team1.teamUnits[0])
gamemap.showMap()
while (True):
    team1.teamUnits[0].move_up(gamemap)
    gamemap.resetUnitMap()
    gamemap.updateUnitMapWithPosition(team1.teamUnits[0])
    gamemap.showMap()

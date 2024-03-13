import gamebase
def play(team_var = gamebase.Team):
    team_var.updateMap()
    team_var.get_castle().CreateWorker(27, 44, team_var)

    team_var.get_teamUnits()[1].add_to_queue("move_up")
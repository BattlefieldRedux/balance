# change teams to one that required
# BLUEFOR = 2, OPFOR = 1
HUMANTEAM = 2 

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    host.registerGameStatusHandler(onGameStatusChanged)

# ------------------------------------------------------------------------
# DeInit
# ------------------------------------------------------------------------
def deinit():
    host.unregisterGameStatusHandler(onGameStatusChanged)

# ------------------------------------------------------------------------
# onGameStatusChanged
# ------------------------------------------------------------------------
def onGameStatusChanged(status):
    if status == bf2.GameStatus.Playing: # game is now in playing state
        host.registerHandler('PlayerChangeTeams', onPlayerChangeTeams, 1) #registering onPlayerChangeTeams event handler


def onPlayerChangeTeams(player, humanHasSpawned): # player changed team
    
    if player is None or player.isValid() is False or player.isAIPlayer(): # some checks...
        return

    if player.getTeam() != HUMANTEAM: # checking if player changed team to wrong one
        player.setTeam(HUMANTEAM) # setting team to proper one
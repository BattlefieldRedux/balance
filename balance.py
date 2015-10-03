# importing standart bf2 packages
import bf2
import host
# importing config
import config as C

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

    # some checks before checking for switch
    if player is None:
        return

    if player.isValid() is False:
        return

    if player.isAIPlayer():
        return

    if player.getName() in C.EXCLUDES:
        return

    # checking player team
    if player.getTeam() != C.HUMANTEAM:
        player.setTeam(C.HUMANTEAM) # setting team to proper one
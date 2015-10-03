### Balance script

 Little tool i have made for PRBF2 admins.<br>
 Will keep all human players on same side.

Usage:

1. Clone repo to `mods/pr/python/game/`
2. Add `import balance` to bottom `mods/pr/python/game/__init__.py`
3. Should be working now.

Settings available in `config.py`:<br>
	* "HUMANTEAM": - determines where players will be kept `onPlayerChangeTeams` event, team 1 is opfor, team 2 is bluefrog.<br>
	* "EXCLUDES": - a list with player names that will be excluded from check for team change.
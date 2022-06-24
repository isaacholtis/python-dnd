import initiative as cen
import os.path
main = cen.Main()

if(os.path.exists("players.json")):
    initiative, playerInfo = main.InterData(main.ReadData())
    print(f"Initiative for today will be in this order: {initiative}\nHere's how the players rolled: ")
    for player in initiative:
        playerName = player
        playerName = playerName[0].upper() + playerName[1:1000]
        print(f"{playerName} rolls a {main.playerDiceType[player]}")
        if playerInfo[player][2] != 0:
            for roll in playerInfo[player][1]:
                print(f"{playerName} rolled a {roll}")
        else:
            print(f"{player} rolled a {roll}")
        if playerInfo[player][3] != 0:
            print(f"{playerName} also adds {playerInfo[player][3]} to their final result, which gives {playerName} a total of {playerInfo[player][0]}")
        else:
            print(f"{playerName}'s final score is {playerInfo[player][0]}") 
else: 
    print("First run of program, please create players.json and input your players and their initiative dice in dictionary format before running again")
    # Put a players name and dice in like this {"playername": "playerdice"} seperated by a coma in between different players
    main.FirstRun({})
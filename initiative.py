import json
import random
from dataclasses import dataclass

@dataclass

class Player:
    rolls: list
    multi: int
    additive: int
    totals: int

class Main:
    def __init__(self):
        self.playerDiceType = []

    def FirstRun(self, playerDict):
        data = open("players.json", "w")
        json.dump(playerDict, data)
        data.close()

    def ReadData(self):
        data = open("players.json", "r")
        playerDict = json.load(data)
        self.playerDiceType = playerDict
        return playerDict

    def InterData(self, playerDict):
        players = list(playerDict.keys())
        playerDict2 = {}
        playerStats = {}
        counter = 0
        for player in players:
            rolls = []
            total = 0
            dicer = playerDict[player]
            nums = list(Main.dicer(dicer))
            for times in range(nums[0]):
                roll = random.randint(1, nums[1])
                total += roll
                rolls.append(roll)
            total += nums[2]
            playerDict2.update({player: total})
            playerStruct = Player(rolls, nums[0], nums[2], total)
            playerDict3 = list(playerDict2.keys())
            playerName = playerDict3[counter]
            playerStats.update({playerName: [playerStruct.totals, playerStruct.rolls, playerStruct.multi, playerStruct.additive]})
            counter += 1
        sorted2 = sorted(playerDict2, key=playerDict2.get)
        sortedDict = {}
        for key in sorted2:
            sortedDict[key] = playerDict2[key]
        initiative = list(sortedDict.keys())
        initiative.reverse()
        return initiative, playerStats

    def dicer(dice):
        multi = dice[0]
        rolls = dice[2]
        for i in range(len(dice) - 1):
            if dice[i] == '+':
                location = i + 1
        additive = dice[location]
        multi = int(multi)
        rolls = int(rolls)
        additive = int(additive)
        return multi, rolls, additive

def createRewardTable(transitionTable, normalCost, trapDict, bonusDict):
    rewardTable={s:{action:{sPrime:normalCost for sPrime in transitionTable[s][action].keys()} for action in transitionTable[s].keys()} for s in transitionTable.keys()}
    for s in rewardTable.keys():
        for a in rewardTable[s].keys():
            for sPrime in trapDict.keys():
                if s not in trapDict.keys():
                    rewardTable[s][a][sPrime]=trapDict[sPrime]
                else:
                    rewardTable[s][a][sPrime]=0
            for sPrime in bonusDict.keys():
                if s not in bonusDict.keys():
                    rewardTable[s][a][sPrime]=bonusDict[sPrime]
                else:
                    rewardTable[s][a][sPrime]=0
    return rewardTable
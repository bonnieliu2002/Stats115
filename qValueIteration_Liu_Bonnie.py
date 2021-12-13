import numpy as np
import drawHeatMap as hm
import rewardTable as rt
import transitionTable as tt

def expect(xDistribution, function):
    expectation=sum([function(x)*px for x, px in xDistribution.items()])
    return expectation

def getSPrimeRDistributionFull(s, action, transitionTable, rewardTable):
    reward=lambda sPrime: rewardTable[s][action][sPrime]
    p=lambda sPrime: transitionTable[s][action][sPrime]
    sPrimeRDistribution={(sPrime, reward(sPrime)): p(sPrime) for sPrime in transitionTable[s][action].keys()}
    return sPrimeRDistribution
    
def updateQFull(s, a, Q, getSPrimeRDistribution, gamma):

##################################################
#		Your code here
##################################################  
    maxQs = {s : max(Q[s].values()) for s in Q}
    Qas = sum([getSPrimeRDistribution(s, a)[(sPrime, r)] * (r + gamma * maxQs[sPrime]) for (sPrime, r) in getSPrimeRDistribution(s, a)])
    return Qas

def qValueIteration(Q, updateQ, stateSpace, actionSpace, convergenceTolerance):

##################################################
#		Your code here
##################################################  
    # Q = {s : {a : Q(s, a)}}
    iterate = True
    # QOld = Q
    QNew = {s : {a : 0 for a in actionSpace} for s in stateSpace}
    while iterate:
        difference = []
        for s in stateSpace:
            for a in actionSpace:
                QNew[s][a] = updateQ(s, a, Q)
                difference.append(abs(QNew[s][a] - Q[s][a]))
            Q = QNew.copy()
            if max(difference) < convergenceTolerance:
                iterate = False
    return QNew

def getPolicyFull(Q, roundingTolerance):

##################################################
#		Your code here
##################################################  
    maxQ = max(Q.values())
    actions = [a for a in Q if maxQ - Q[a] < roundingTolerance]
    policy = {a : 1 / len(actions) for a in actions}
    return policy


def viewDictionaryStructure(d, levels, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(levels[indent]) + ": "+ str(key))
        if isinstance(value, dict):
            viewDictionaryStructure(value, levels, indent+1)
        else:
            print('\t' * (indent+1) + str(levels[indent+1])+ ": " + str(value))

def main():
    minX, maxX, minY, maxY=(0, 3, 0, 2)

    
    
    actionSpace=[(0,1), (0,-1), (1,0), (-1,0)]
    stateSpace=[(i,j) for i in range(maxX+1) for j in range(maxY+1) if (i, j) != (1, 1)]
    Q={s:{a: 0 for a in actionSpace} for s in stateSpace}
    
    normalCost=-0.04
    trapDict={(3,1):-1}
    bonusDict={(3,0):1}
    blockList=[(1,1)]
    
    p=0.8
    transitionProbability={'forward':p, 'left':(1-p)/2, 'right':(1-p)/2, 'back':0}
    transitionProbability={move: p for move, p in transitionProbability.items() if transitionProbability[move]!=0}
    
    transitionTable=tt.createTransitionTable(minX, minY, maxX, maxY, trapDict, bonusDict, blockList, actionSpace, transitionProbability)
    rewardTable=rt.createRewardTable(transitionTable, normalCost, trapDict, bonusDict)

    
    """
    levelsReward  = ["state", "action", "next state", "reward"]
    levelsTransition  = ["state", "action", "next state", "probability"]
    
    viewDictionaryStructure(transitionTable, levelsTransition)
    viewDictionaryStructure(rewardTable, levelsReward)
    """
        
    getSPrimeRDistribution=lambda s, action: getSPrimeRDistributionFull(s, action, transitionTable, rewardTable)
    gamma = 0.8       
    updateQ=lambda s, a, Q: updateQFull(s, a, Q, getSPrimeRDistribution, gamma)
    
    convergenceTolerance = 1e-7
    QNew=qValueIteration(Q, updateQ, stateSpace, actionSpace, convergenceTolerance)
    
    roundingTolerance= 1e-7
    getPolicy=lambda Q: getPolicyFull(Q, roundingTolerance)
    policy={s:getPolicy(QNew[s]) for s in stateSpace}
    
    V={s: max(QNew[s].values()) for s in stateSpace}
    
    VDrawing=V.copy()
    VDrawing[(1, 1)]=0
    VDrawing={k: v for k, v in sorted(VDrawing.items(), key=lambda item: item[0])}
    policyDrawing=policy.copy()
    policyDrawing[(1, 1)]={(1, 0): 1.0}
    policyDrawing={k: v for k, v in sorted(policyDrawing.items(), key=lambda item: item[0])}

    hm.drawFinalMap(VDrawing, policyDrawing, trapDict, bonusDict, blockList, normalCost)
    
    
    
if __name__=='__main__': 
    main()

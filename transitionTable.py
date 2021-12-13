
def transitionFull(s, move, minX, minY, maxX, maxY, blockList, trapDict, bonusDict):
    if s in trapDict.keys() or s in bonusDict.keys():
        return s
    x, y=s
    dx, dy=move
    def boundary(x, minX, maxX):
        return max(minX, min(x, maxX))
    sPrimeConsideringBoundary=(boundary(x+dx, minX, maxX), boundary(y+dy, minY, maxY))
    def blocking(sPrime, blockList):
        if sPrime in blockList:
            return s
        else:
            return sPrime
    sPrime=blocking(sPrimeConsideringBoundary, blockList)
    return sPrime

def createTransitionTable(minX, minY, maxX, maxY, trapDict, bonusDict, blockList, possibleAction, transitionProbability):
        
    possibleState=[(i,j) for i in range(minX, maxX+1) for j in range(minY, maxY+1)]
    

    for block in blockList:
        possibleState.remove(block)
        
    moves={'forward':{(1,0):(1,0),(0,-1):(0,-1),(-1,0):(-1,0),(0,1):(0,1)},\
        'left':{(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1),(0,1):(1,0)},\
       'right':{(1,0):(0,1),(0,-1):(1,0),(-1,0):(0,-1),(0,1):(-1,0)},\
       'back':{(1,0):(-1,0),(0,-1):(0,1),(-1,0):(1,0),(0,1):(0,-1)}}
    
    def transition(s, move):
        return transitionFull(s, move, minX, minY, maxX, maxY, blockList, trapDict, bonusDict)
    
    def transitionFunction(s, action, sPrime, transitionProbability, moves):
        moveDictionary={moves[move][action]:transitionProbability[move] for move in transitionProbability.keys()}
        sPrimeProbability=sum([p for move, p in moveDictionary.items() if transition(s, move)==sPrime])
        return sPrimeProbability
    
    emptyTransitionTable={s:{action:{transition(s, moves[move][action]):transitionProbability[move] for move in transitionProbability.keys()} for action in possibleAction} for s in possibleState}
    
    transitionTable={s:{action:{sPrime:transitionFunction(s, action, sPrime, transitionProbability, moves) for sPrime in possibleState} for action in possibleAction} for s in possibleState}
    return transitionTable
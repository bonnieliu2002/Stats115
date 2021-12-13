


def expect(xDistribution, function):
    fxProduct=[px*function(x) for x, px in xDistribution.items()]
    expectation=sum(fxProduct)
    return expectation


def forward(xT_1Distribution, eT, transitionTable, sensorTable):
    
##################################################
#		Your code here
################################################## 
    xTDistribution = {x_t : sensorTable[x_t][eT] * sum(transitionTable[x_t_1][x_t] * xT_1Distribution[x_t_1] for x_t_1 in transitionTable) for x_t in sensorTable}
    alpha = 1 / sum(xTDistribution.values())
    xTDistribution = {x_t : xTDistribution[x_t] * alpha for x_t in xTDistribution}
    return xTDistribution

def main():
    
    pX0={0:0.3, 1:0.7}
    e=1
    transitionTable={0:{0:0.6, 1:0.4}, 1:{0:0.3, 1:0.7}}
    sensorTable={0:{0:0.6, 1:0.3, 2:0.1}, 1:{0:0, 1:0.5, 2:0.5}}
    
    xTDistribution=forward(pX0, e, transitionTable, sensorTable)
    print(xTDistribution)

if __name__=="__main__":
    main()
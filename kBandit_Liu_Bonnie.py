import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import random

def getSamplar():
    mu=np.random.normal(0,10)
    sd=abs(np.random.normal(5,2))
    getSample=lambda: np.random.normal(mu,sd)
    return getSample

def e_greedy(Q, e):

##################################################
#		Your code here
##################################################  
    
    x = np.random.rand()
    if x < e:
        return random.randint(0, 9)
    actions_with_max_reward = [random.randint(0, 9)]
    max_reward = Q[actions_with_max_reward[0]]
    for action in Q:
        if Q[action] == max_reward:
            actions_with_max_reward.append(action)
        elif Q[action] > max_reward:
            max_reward = Q[action]
            actions_with_max_reward.clear()
            actions_with_max_reward.append(action)
    return random.choice(actions_with_max_reward)

def calculateConfidenceBound(Q, N, c, action):
    return Q[action] + c * np.sqrt(np.log(sum(N.values()) + 1) / (N[action]))

def upperConfidenceBound(Q, N, c):
   
##################################################
#		Your code here
##################################################  
    if min(N.values()) == 0:
        actions = [action for action in Q if N[action] == 0]
        return np.random.choice(actions)
    actions_with_ucb = [random.randint(0, 9)]
    ucb = calculateConfidenceBound(Q, N, c, actions_with_ucb[0])
    for action in Q:
        cb = calculateConfidenceBound(Q, N, c, action)
        if cb == ucb:
            actions_with_ucb.append(action)
        elif cb > ucb:
            ucb = cb
            actions_with_ucb.clear()
            actions_with_ucb.append(action)
    return random.choice(actions_with_ucb)

def updateQN(action, reward, Q, N):

##################################################
#		Your code here
##################################################  
    QNew = deepcopy(Q)
    NNew = deepcopy(N)
    # my implementation of QNew[action] calculations: QNew[action] = (Q[action] * N[action] + reward) / (N[action] + 1)
    NNew[action] = N[action] + 1
    QNew[action] = QNew[action] + (reward - QNew[action]) / NNew[action]
    return QNew, NNew

def decideMultipleSteps(Q, N, policy, bandit, maxSteps):

##################################################
#		Your code here
##################################################  
    actionReward = []
    for i in range(maxSteps):
        action = policy(Q, N)
        reward = bandit(action)
        actionReward.append((action, reward))
        Q, N = updateQN(action, reward, Q, N)
    return {'Q':Q, 'N':N, 'actionReward':actionReward}

def plotMeanReward(actionReward,label):
    maxSteps=len(actionReward)
    reward=[reward for (action,reward) in actionReward]
    meanReward=[sum(reward[:(i+1)])/(i+1) for i in range(maxSteps)]
    plt.plot(range(maxSteps), meanReward, linewidth=0.9, label=label)
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')

def main():
    np.random.seed(2020)
    K=10
    maxSteps=1000
    Q={k:0 for k in range(K)}
    N={k:0 for k in range(K)}
    testBed={k:getSamplar() for k in range(K)}
    bandit=lambda action: testBed[action]()
    
    policies={}
    policies["e-greedy-0.5"]=lambda Q, N: e_greedy(Q, 0.5)
    policies["e-greedy-0.1"]=lambda Q, N: e_greedy(Q, 0.1)
    policies["UCB-2"]=lambda Q, N: upperConfidenceBound(Q, N, 2)
    policies["UCB-20"]=lambda Q, N: upperConfidenceBound(Q, N, 20)
    
    allResults = {name: decideMultipleSteps(Q, N, policy, bandit, maxSteps) for (name, policy) in policies.items()}
    
    for name, result in allResults.items():
         plotMeanReward(allResults[name]['actionReward'], label=name)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
    


if __name__=='__main__':
    main()

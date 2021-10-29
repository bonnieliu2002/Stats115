

def expect(xDistribution, function):
    fxProduct=[px*function(x) for x, px in xDistribution.items()]
    expectation=sum(fxProduct)
    return expectation

def getUnnormalizedPosterior(prior, likelihood):
    
##################################################
#		Your code here
##################################################
    unnormalizedPosterior = {state : prior[state] * likelihood[state] for state in prior}
    return unnormalizedPosterior

def normalize(unnormalizedDistribution):

##################################################
#		Your code here
################################################## 
    sumOfProbabilities = sum(unnormalizedDistribution.values())
    normalizedDistribution = {key : value / sumOfProbabilities for (key, value) in unnormalizedDistribution.items()}
    return normalizedDistribution

def getSumOfProbability(unnormalizedDistribution):
    
##################################################
#		Your code here
################################################## 
    sumOfProbability = sum(unnormalizedDistribution.values())
    return sumOfProbability

def getPosterior(prior, likelihood):

##################################################
#		Your code here
################################################## 
    posterior = normalize(getUnnormalizedPosterior(prior, likelihood))
    return posterior

def getMarginalOfData(prior, likelihood):
    
##################################################
#		Your code here
################################################## 
    marginal = getSumOfProbability(getUnnormalizedPosterior(prior, likelihood))
    return marginal

def getEU(action, sDistribution, rewardTable):
    
##################################################
#		Your code here
################################################## 
    EU = expect(sDistribution, lambda s : rewardTable[s][action])
    return EU

def getMaxEUFull(evidence, prior, likelihoodTable, rewardTable, actionSpace):
    
##################################################
#		Your code here
################################################## 
    if evidence is None:
        EUs = [getEU(action, prior, rewardTable) for action in actionSpace]
    else:
        EUs = [getEU(action, getPosterior(prior, likelihoodTable[evidence]), rewardTable) for action in actionSpace]
    return max(EUs)

def getValueOfInformationOfATest(evidenceSpace, getMarginalOfEvidence, getMaxEU):
    
##################################################
#		Your code here
################################################## 
    sumOverEvidence = sum([getMarginalOfEvidence(evidence) * getMaxEU(evidence) for evidence in evidenceSpace])
    valueOfInfo = sumOverEvidence - getMaxEU(None)
    return valueOfInfo



def main():
    
    prior={'Well 1 contains oil': 0.2, 'Well 2 contains oil': 0.4, 'Well 3 contains oil': 0.2, 'Well 4 contains oil': 0.2}
    
    actionSpace=['Buy Well 1', 'Buy Well 2', 'Buy Well 3', 'Buy Well 4']
    rewardTable={'Well 1 contains oil': {'Buy Well 1': 100, 'Buy Well 2': 0, 'Buy Well 3': 0, 'Buy Well 4': 0},
                 'Well 2 contains oil': {'Buy Well 1': 0, 'Buy Well 2': 100, 'Buy Well 3': 0, 'Buy Well 4': 0},
                 'Well 3 contains oil': {'Buy Well 1': 0, 'Buy Well 2': 0, 'Buy Well 3': 100, 'Buy Well 4': 0},
                 'Well 4 contains oil': {'Buy Well 1': 0, 'Buy Well 2': 0, 'Buy Well 3': 0, 'Buy Well 4': 100}}   
    
    testSpace=['Test Well 1', 'Test Well 2', 'Test Well 3', 'Test Well 4']
    evidenceSpace=['Microbe', 'No microbe']
    likelihoodTable={'Test Well 1':{'Microbe': {'Well 1 contains oil': 0.8, 'Well 2 contains oil': 0.1, 'Well 3 contains oil': 0.1, 'Well 4 contains oil': 0.1},
                                    'No microbe': {'Well 1 contains oil': 0.2, 'Well 2 contains oil': 0.9, 'Well 3 contains oil': 0.9, 'Well 4 contains oil': 0.9}},
                     'Test Well 2':{'Microbe': {'Well 1 contains oil': 0.1, 'Well 2 contains oil': 0.8, 'Well 3 contains oil': 0.1, 'Well 4 contains oil': 0.1},
                                    'No microbe': {'Well 1 contains oil': 0.9, 'Well 2 contains oil': 0.2, 'Well 3 contains oil': 0.9, 'Well 4 contains oil': 0.9}},
                     'Test Well 3':{'Microbe': {'Well 1 contains oil': 0.1, 'Well 2 contains oil': 0.1, 'Well 3 contains oil': 0.8, 'Well 4 contains oil': 0.1},
                                    'No microbe': {'Well 1 contains oil': 0.9, 'Well 2 contains oil': 0.9, 'Well 3 contains oil': 0.2, 'Well 4 contains oil': 0.9}},
                     'Test Well 4':{'Microbe': {'Well 1 contains oil': 0.1, 'Well 2 contains oil': 0.1, 'Well 3 contains oil': 0.1, 'Well 4 contains oil': 0.8},
                                    'No microbe': {'Well 1 contains oil': 0.9, 'Well 2 contains oil': 0.9, 'Well 3 contains oil': 0.9, 'Well 4 contains oil': 0.2}}}
    

    getMarginalOfEvidenceGivenTest=lambda test, evidence: getMarginalOfData(prior, likelihoodTable[test][evidence]) 
    
    getMaxEU=lambda test, evidence:getMaxEUFull(evidence, prior, likelihoodTable[test], rewardTable, actionSpace)
    
    getValueOfInformation=lambda test: getValueOfInformationOfATest(evidenceSpace,
                                                                    lambda evidence: getMarginalOfEvidenceGivenTest(test, evidence), 
                                                                    lambda evidence: getMaxEU(test, evidence))
    
    testExample1='Test Well 1'
    print(getValueOfInformation(testExample1))
    
    testExample2='Test Well 2'
    print(getValueOfInformation(testExample2))



    
if __name__=="__main__":
    main()      

def expect(xDistribution, function):
    
##################################################
#		Your code here
##################################################  
    expectation = 0
    for x in xDistribution:
        expectation += xDistribution[x] * function(x)
    return expectation



 
def getVariance(xDistribution):
    
##################################################
#		Your code here
#       Call your own “expect” function
################################################## 
    variance = 0
    expected = expect(xDistribution, lambda x: x)
    for x in xDistribution:
        variance += xDistribution[x] * ((x - expected) ** 2)
    return variance

def main():
    xDistributionExample1={1: 1/5, 2: 2/5, 3: 2/5}
    functionExample1=lambda x: x ** 2
    print(expect(xDistributionExample1, functionExample1))
    print(getVariance(xDistributionExample1))
    
    xDistributionExample2={1: 1/6, -1/2: 1/3, 1/3: 1/4, -1/4: 1/12, 1/5: 1/6}
    functionExample2=lambda x: 1/x
    print(expect(xDistributionExample2, functionExample2))
    print(getVariance(xDistributionExample2))


if __name__ == '__main__':
    main()

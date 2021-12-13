import sys
sys.path.append('../src/')

import unittest
from ddt import ddt, data, unpack
import qValueIteration_Liu_Bonnie as targetCode


@ddt
class TestQValueIteration(unittest.TestCase):
    
    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)

##################################################
#		Complete the code below
##################################################

    transitionTable = {(0, 0) : {(1, 0) : {(0, 0) : 0, (1, 0) : 1}}, (1, 0) : {(-1, 0) : {(0, 0) : 1, (1, 0) : 0}}}
    rewardTable = {(0, 0) : {(1, 0) : {(0, 0) : -2, (1, 0) : 5}}, (1, 0) : {(-1, 0) : {(0, 0) : -2, (1, 0) : 5}}}

    @data(((0, 0), (1, 0), transitionTable, rewardTable, {((0, 0), -2) : 0, ((1, 0), 5) : 1}))
    @unpack
    def test_get_sPrime_r_distribution_full_move_down(self, s, action, transitionTable, rewardTable, expectedResult):
        calculatedResult = targetCode.getSPrimeRDistributionFull(s, action, transitionTable, rewardTable)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

    @data(((1, 0), (-1, 0), transitionTable, rewardTable, {((0, 0), -2) : 1, ((1, 0), 5) : 0}))
    @unpack
    def test_get_sPrime_r_distribution_full_move_up(self, s, action, transitionTable, rewardTable, expectedResult):
        calculatedResult = targetCode.getSPrimeRDistributionFull(s, action, transitionTable, rewardTable)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

    @data(((0, 0), (1, 0), {(0, 0) : {(1, 0) : 3, (0, 1) : 0, (-1, 0) : 0, (0, -1) : 0}, (1, 0) : {(-1, 0) : 2, (1, 0) : 0, (0, 1) : 0, (0, -1) : 0}}, lambda s, a : targetCode.getSPrimeRDistributionFull(s, a, {(0, 0) : {(1, 0) : {(0, 0) : 0, (1, 0) : 1}}, (1, 0) : {(-1, 0) : {(0, 0) : 1, (1, 0) : 0}}}, {(0, 0) : {(1, 0) : {(0, 0) : -2, (1, 0) : 5}}, (1, 0) : {(-1, 0) : {(0, 0) : -2, (1, 0) : 5}}}), 0.8, 6.6))
    @unpack
    def test_update_q_full_move_down(self, s, a, Q, getSPrimeRDistribution, gamma, expectedResult):
        calculatedResult = targetCode.updateQFull(s, a, Q, getSPrimeRDistribution, gamma)
        self.assertAlmostEqual(calculatedResult, expectedResult)

    @data(((1, 0), (-1, 0), {(0, 0) : {(1, 0) : 3, (0, 1) : 0, (-1, 0) : 0, (0, -1) : 0}, (1, 0) : {(-1, 0) : 2, (1, 0) : 0, (0, 1) : 0, (0, -1) : 0}}, lambda s, a : targetCode.getSPrimeRDistributionFull(s, a, {(0, 0) : {(1, 0) : {(0, 0) : 0, (1, 0) : 1}}, (1, 0) : {(-1, 0) : {(0, 0) : 1, (1, 0) : 0}}}, {(0, 0) : {(1, 0) : {(0, 0) : -2, (1, 0) : 5}}, (1, 0) : {(-1, 0) : {(0, 0) : -2, (1, 0) : 5}}}), 0.8, 0.4))
    @unpack
    def test_update_q_full_move_up(self, s, a, Q, getSPrimeRDistribution, gamma, expectedResult):
        calculatedResult = targetCode.updateQFull(s, a, Q, getSPrimeRDistribution, gamma)
        self.assertAlmostEqual(calculatedResult, expectedResult)
    
    @data(({(0, 1) : 5, (1, 0) : 4, (0, -1) : 3, (-1, 0) : 2}, 0.5, {(0, 1) : 1}))
    @unpack
    def test_get_policy_full_no_tie(self, Q, roundingTolerance, expectedResult):
        calculatedResult = targetCode.getPolicyFull(Q, roundingTolerance)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

    @data(({(0, 1) : 5, (1, 0) : 4.9, (0, -1) : 4.8, (-1, 0) : 4.7}, 0.5, {(0, 1) : 0.25, (1, 0) : 0.25, (0, -1) : 0.25, (-1, 0) : 0.25}))
    @unpack
    def test_get_policy_full_tie(self, Q, roundingTolerance, expectedResult):
        calculatedResult = targetCode.getPolicyFull(Q, roundingTolerance)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

##################################################
#		Complete the code above
##################################################  
	
    def tearDown(self):
       pass
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
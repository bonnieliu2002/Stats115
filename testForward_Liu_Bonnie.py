import sys
sys.path.append('../src/')

import unittest
from ddt import ddt, data, unpack
import forward_Liu_Bonnie as targetCode #change to file name


@ddt
class TestForward(unittest.TestCase):
    
    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)

##################################################
#		Complete the code below
##################################################  
                
    # @data(({0:0.3, 1:0.7}, 1, {0:{0:0.6, 1:0.4}, 1:{0:0.3, 1:0.7}}, {0:{0:0.6, 1:0.3, 2:0.1}, 1:{0:0, 1:0.5, 2:0.5}}, {0: 0.2773, 1: 0.7227}))#(xT_1Distribution, eT, transitionTable, sensorTable, expectedResult)
    # @unpack
    # def test_forward_original(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
    #     calculatedResult = targetCode.forward(xT_1Distribution, eT, transitionTable, sensorTable)
    #     self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

    @data(({0:1}, 1, {0:{0:1}}, {0:{0:0.5, 1:0.5}}, {0:1}))
    @unpack
    def test_forward_one_state(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
        calculatedResult = targetCode.forward(xT_1Distribution, eT, transitionTable, sensorTable)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

    @data(({0:0.25, 1:0.25, 2:0.5}, 0, {0:{0:0.9, 1:0.01, 2:0.09}, 1:{0:0.5, 1:0, 2:0.5}, 2:{0:0.01, 1:0.99, 2:0}}, {0:{0:0.2, 1:0.8}, 1:{0:0.7, 1:0.3}, 2:{0:0.5, 1:0.5}}, {0:0.144, 1:0.7064, 2:0.1496}))
    @unpack
    def test_forward_three_states(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
        calculatedResult = targetCode.forward(xT_1Distribution, eT, transitionTable, sensorTable)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)


##################################################
#		Complete the code above
##################################################  
	
    def tearDown(self):
       pass
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
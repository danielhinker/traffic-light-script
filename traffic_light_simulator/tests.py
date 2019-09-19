import unittest
import time
import math
import traffic_light
import traffic_light_designs


class TrafficLightTests(unittest.TestCase):

    def setUp(self):
        self.traffic = traffic_light.TrafficLight()
        self.traffic_designs = traffic_light_designs.traffic_lights_array


    def testTime(self):
        self.assertEqual(self.traffic.time, 0)


    def testInvalidInput(self):
        returnValue = self.traffic.checkInput('string')
        self.assertFalse(returnValue)


    def testInvalidInput2(self):
        returnValue = self.traffic.checkInput('-1')
        self.assertFalse(returnValue)


    def testInvalidInput3(self):
        returnValue = self.traffic.checkInput('5')
        self.assertTrue(returnValue)


    def testInvalidInput4(self):
        returnValue = self.traffic.checkInput('0')
        self.assertFalse(returnValue)


    def testDesign(self):
        self.assertEqual(self.traffic.traffic_lights_array, self.traffic_designs)


    def testExit(self):
        with self.assertRaises(SystemExit):
            self.traffic.exit_simulator()

   
    def testChangeLightTime(self):
        self.traffic.time = 1
        start = time.time()
        self.traffic.change_light()
        end = time.time()
        diff = end - start
        self.assertEqual(math.floor(diff / 2 + 1), 2)


    def testChangeLightTime2(self):
        self.traffic.time = 2
        start = time.time()
        self.traffic.change_light()
        end = time.time()
        diff = end - start
        self.assertEqual(math.floor(diff / 2 + 1), 3)


    def testChangeLightTime3(self):
            self.traffic.time = 3
            start = time.time()
            self.traffic.change_light()
            end = time.time()
            diff = end - start
            self.assertEqual(math.floor(diff / 2 + 1), 4)


if __name__ == '__main__':
    unittest.main()
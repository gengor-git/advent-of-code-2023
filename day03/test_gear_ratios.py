import unittest
import day03.gear_ratios as day3

class TestGearRatios(unittest.TestCase):
    def testSamplePart1(self):
        self.assertEqual(day3.calculate_parts(day3.sample_file), 4361)

if __name__ == '__main__':
    unittest.main()
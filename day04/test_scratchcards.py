import unittest
import day04.scratchcards as day4

class TestScratchCards(unittest.TestCase):
    def testSamplePart1(self):
        self.assertEqual(day4.calculate_scratchcard_points_pt1(day4.sample_file), 13)

    def testPart1(self):
        self.assertEqual(day4.calculate_scratchcard_points_pt1(day4.input_file), 22897)

    def testSamplePart2(self):
        self.assertEqual(day4.calculate_scratchcard_points_pt2(day4.sample_file), 30)

    def testPart2(self):
        self.assertEqual(day4.calculate_scratchcard_points_pt2(day4.input_file), 5095824)

if __name__ == '__main__':
    unittest.main()
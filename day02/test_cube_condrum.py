import unittest
import day02.cube_condrum as day2


class TestExtracdtDigits(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(day2.calculate_possible_games(day2.sample_file), 8)

    def testPart1(self):
        self.assertEqual(day2.calculate_possible_games(day2.input_file), 2006)

    def testSamplePart2(self):
        self.assertEqual(day2.calculate_minimum_cubes(day2.sample_file), 2286)

    # def testPart2(self):
    #     self.assertEqual(day2.extract_words_with_digits(day1.input_file), 53868)



if __name__ == '__main__':
    unittest.main()

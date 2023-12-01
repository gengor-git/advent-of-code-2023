
import unittest
import day01.extract_digits as day1


class TestExtracdtDigits(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(day1.extract_digits(day1.sample_file), 142)

    def testPart1(self):
        self.assertEqual(day1.extract_digits(day1.input_file), 54953)

    def testSamplePart2(self):
        self.assertEqual(day1.extract_words_with_digits(day1.sample_file2), 281)



if __name__ == '__main__':
    unittest.main()

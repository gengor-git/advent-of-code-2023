
import unittest
import day01.extract_digits as day1


class TestExtracdtDigits(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(day1.extract_digits(day1.sample_file), 142)

    # def testRealInputPart1(self):
    #     self.assertEqual(day1.extract_digits(day1.input_file), 560)


if __name__ == '__main__':
    unittest.main()

import unittest
import kid


class KIDTestCase(unittest.TestCase):
    def test_should_generate_kid(self):
        result = kid.kid_mod11('100', length=15)
        expected = '000000000001007'
        self.assertEqual(expected, result)

    def test_should_return_kid_with_ctrl_num_as_1(self):
        expected = '0016861'
        result = kid.kid_mod11('1686', length=7)
        self.assertEqual(expected, result)

    def test_should_return_kid_with_ctrl_num_as_minus(self):
        expected = '000023-'
        result = kid.kid_mod11('23', length=7)
        self.assertEqual(expected, result)

    def test_should_return_kid_with_ctrl_num_as_zero(self):
        expected = '0097780'
        result = kid.kid_mod11('9778', length=7)
        self.assertEqual(expected, result)

    def test_should_return_kid_with_ctrl_num_as_weighted_num(self):
        expected = '1231235'
        result = kid.kid_mod11('123123', length=7)
        self.assertEqual(expected, result)

    def test_kid_no_should_be_atleast_7_digits(self):
        result = kid.kid_mod11('23', length=7)
        self.assertEqual(7, len(result))


if __name__ == '__main__':
    unittest.main()

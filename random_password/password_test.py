import unittest

from random_password.pass_generator import generate_password, Strength, DEFAULT_REQUIREMENTS


class MyTestCase(unittest.TestCase):

    def do_test_validity(self, expected, required=DEFAULT_REQUIREMENTS):
        for template in required:
            self.assertTrue(any(map(lambda x: x in template, expected)))

    def test_weak(self):
        strength = Strength.WEAK
        expected = generate_password(strength)
        self.assertEqual(strength.value, len(expected))
        self.do_test_validity(expected)

    def test_strong(self):
        strength = Strength.STRONG
        expected = generate_password(strength)
        self.assertEqual(strength.value, len(expected))
        self.do_test_validity(expected)

    def test_very_strong(self):
        strength = Strength.VERY_STRONG
        expected = generate_password(strength)
        self.assertEqual(strength.value, len(expected))
        self.do_test_validity(expected)

    def test_custom_req_weak(self):
        strength = Strength.WEAK
        required = ['ABC', '123', '&%^']
        expected = generate_password(strength, required)
        self.assertEqual(strength.value, len(expected))
        self.do_test_validity(expected, required)


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase
from utils.misc import *


class Test_Misc(TestCase):

    def test_alpha_to_number(self):
        self.assertEqual(0, alpha_to_number("A"))
        self.assertEqual(9, alpha_to_number("J"))

    def test_number_to_alpha(self):
        self.assertEqual("A", number_to_alpha(0))
        self.assertEqual("J", number_to_alpha(9))

    def test_letter_to_prime(self):
        self.assertEqual(2, letter_to_prime("A"))
        self.assertEqual(61, letter_to_prime("R"))

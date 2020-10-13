from unittest import TestCase
from utils import Reflector


class Test_Reflector(TestCase):

    def setUp(self):
        self.reflector = Reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")

    def test_reflector_init(self):
        self.assertEqual("YRUHQSLDPXNGOKMIEBFZCWVJAT", self.reflector._letters)

    def test_reflect_forward(self):
        self.assertEqual("H", self.reflector.forward_flow("D"))
        self.assertEqual("Y", self.reflector.forward_flow("A"))
        self.assertEqual("T", self.reflector.forward_flow("Z"))


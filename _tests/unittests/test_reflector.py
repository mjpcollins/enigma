from unittest import TestCase
from utils import Reflector


class Test_Reflector(TestCase):

    def setUp(self):
        self.reflector = Reflector(letters="CDEMUXPNVZBHYFQWKIATGLORSJ")

    def test_entry_wheel_swaps_init(self):
        self.assertEqual("CDEMUXPNVZBHYFQWKIATGLORSJ", self.reflector._letters)
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.reflector._alphabet)

    def test_entry_wheel_swaps_forwardflow(self):
        self.assertEqual("M", self.reflector.forward_flow("D"))
        self.assertEqual("C", self.reflector.forward_flow("A"))
        self.assertEqual("J", self.reflector.forward_flow("Z"))

    def test_entry_wheel_swaps_reverseflow(self):
        self.assertEqual("B", self.reflector.reverse_flow("D"))
        self.assertEqual("S", self.reflector.reverse_flow("A"))
        self.assertEqual("J", self.reflector.reverse_flow("Z"))

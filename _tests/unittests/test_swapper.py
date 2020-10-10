from unittest import TestCase
from utils import Swapper


class Test_Swapper(TestCase):

    def setUp(self):
        self.swapper = Swapper(letters="CDEMUXPNVZBHYFQWKIATGLORSJ")

    def test_init(self):
        self.assertEqual("CDEMUXPNVZBHYFQWKIATGLORSJ", self.swapper._letters)
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.swapper._alphabet)

    def test_forwardflow(self):
        self.assertEqual("M", self.swapper.forward_flow("D"))
        self.assertEqual("C", self.swapper.forward_flow("A"))
        self.assertEqual("J", self.swapper.forward_flow("Z"))

    def test_reverseflow(self):
        self.assertEqual("B", self.swapper.reverse_flow("D"))
        self.assertEqual("S", self.swapper.reverse_flow("A"))
        self.assertEqual("J", self.swapper.reverse_flow("Z"))



from unittest import TestCase
from utils import EntryWheel


class Test_EntryWheel(TestCase):

    def setUp(self):
        self.entry_wheel_plain = EntryWheel()
        self.entry_wheel_swaps = EntryWheel(letters="CDEMUXPNVZBHYFQWKIATGLORSJ")

    def test_entry_wheel_swaps_init(self):
        self.assertEqual("CDEMUXPNVZBHYFQWKIATGLORSJ", self.entry_wheel_swaps._letters)
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.entry_wheel_swaps._alphabet)

    def test_entry_wheel_swaps_forwardflow(self):
        self.assertEqual("M", self.entry_wheel_swaps.forward_flow("D"))
        self.assertEqual("C", self.entry_wheel_swaps.forward_flow("A"))
        self.assertEqual("J", self.entry_wheel_swaps.forward_flow("Z"))

    def test_entry_wheel_swaps_reverseflow(self):
        self.assertEqual("B", self.entry_wheel_swaps.reverse_flow("D"))
        self.assertEqual("S", self.entry_wheel_swaps.reverse_flow("A"))
        self.assertEqual("J", self.entry_wheel_swaps.reverse_flow("Z"))

    def test_entry_wheel_plain_init(self):
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.entry_wheel_plain._letters)
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.entry_wheel_plain._alphabet)

    def test_entry_wheel_plain_forwardflow(self):
        self.assertEqual("D", self.entry_wheel_plain.forward_flow("D"))
        self.assertEqual("A", self.entry_wheel_plain.forward_flow("A"))
        self.assertEqual("Z", self.entry_wheel_plain.forward_flow("Z"))

    def test_entry_wheel_plain_reverseflow(self):
        self.assertEqual("D", self.entry_wheel_plain.reverse_flow("D"))
        self.assertEqual("A", self.entry_wheel_plain.reverse_flow("A"))
        self.assertEqual("Z", self.entry_wheel_plain.reverse_flow("Z"))

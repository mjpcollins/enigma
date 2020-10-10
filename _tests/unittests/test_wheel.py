from unittest import TestCase
from utils import Wheel


class Test_Wheel(TestCase):

    def setUp(self):
        self.plain_wheel = Wheel(letters="CDEMUXPNVZBHYFQWKIATGLORSJ",
                                 start_position="C",
                                 turnover="E",
                                 position=0)
        self.offset_wheel = Wheel(letters="CDEMUXPNVZBHYFQWKIATGLORSJ",
                                  start_position="D",
                                  turnover="E",
                                  position=1)

    def test_plain_wheel_init(self):
        self.assertEqual("CDEMUXPNVZBHYFQWKIATGLORSJ", self.plain_wheel._letters)
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.plain_wheel._alphabet)
        self.assertEqual("C", self.plain_wheel._starting_pos)
        self.assertEqual("E", self.plain_wheel._turnover)
        self.assertEqual(0, self.plain_wheel._position)
        self.assertEqual("DEMUXPNVZBHYFQWKIATGLORSJC", self.offset_wheel._letters)
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.offset_wheel._alphabet)
        self.assertEqual("D", self.offset_wheel._starting_pos)
        self.assertEqual("E", self.offset_wheel._turnover)
        self.assertEqual(1, self.offset_wheel._position)

    def test__gt(self):
        self.assertEqual(True, self.offset_wheel > self.plain_wheel)
        self.assertEqual(False, self.offset_wheel < self.plain_wheel)

    def test_position_in_machine(self):
        self.assertEqual(0, self.plain_wheel.get_position_in_machine())
        self.plain_wheel._position = 1
        self.assertEqual(1, self.plain_wheel.get_position_in_machine())

    def test_get_current_position(self):
        self.plain_wheel._current_pos = "A"
        self.assertEqual("A", self.plain_wheel.get_current_position())

    def test_set_current_position(self):
        self.plain_wheel._current_pos = "A"
        self.plain_wheel.set_current_position("Z")
        self.assertEqual("Z", self.plain_wheel._current_pos)

    def test_plain_wheel_forward_flow(self):
        self.assertEqual("M", self.plain_wheel.forward_flow("D"))
        self.assertEqual("C", self.plain_wheel.forward_flow("A"))
        self.assertEqual("J", self.plain_wheel.forward_flow("Z"))

    def test_plain_wheel_reverse_flow(self):
        self.assertEqual("B", self.plain_wheel.reverse_flow("D"))
        self.assertEqual("S", self.plain_wheel.reverse_flow("A"))
        self.assertEqual("J", self.plain_wheel.reverse_flow("Z"))

    def test_plain_wheel_rotate_once(self):
        self.assertEqual("M", self.plain_wheel.forward_flow("D"))
        self.assertEqual(False, self.plain_wheel.rotate_once())
        self.assertEqual("U", self.plain_wheel.forward_flow("D"))

    def test_offset_wheel_rotate_once(self):
        self.assertEqual("U", self.offset_wheel.forward_flow("D"))
        self.assertEqual(False, self.offset_wheel.rotate_once())
        self.assertEqual("X", self.offset_wheel.forward_flow("D"))
        self.assertEqual(True, self.offset_wheel.rotate_once())
        self.assertEqual("P", self.offset_wheel.forward_flow("D"))

    def test_will_cause_turnover(self):
        self.plain_wheel._turnover = "E"
        self.plain_wheel._current_pos = "A"
        self.assertEqual(False, self.plain_wheel.will_cause_turnover())
        self.plain_wheel._current_pos = "E"
        self.assertEqual(True, self.plain_wheel.will_cause_turnover())


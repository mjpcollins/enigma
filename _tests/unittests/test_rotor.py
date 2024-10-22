from unittest import TestCase
from utils import Rotor


class Test_Rotor(TestCase):

    def setUp(self):
        self.plain_wheel = Rotor(letters="CDEMUXPNVZBHYFQWKIATGLORSJ",
                                 start_position="A",
                                 turnover="E",
                                 position=0)
        self.offset_wheel = Rotor(letters="DEMUXPNVZBHYFQWKIATGLORSJC",
                                  start_position="D",
                                  turnover="E",
                                  position=1)
        self.rotor_I = Rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                             start_position="A",
                             turnover="Q",
                             position=1)
        self.rotor_no_notch = Rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                    start_position="A",
                                    turnover="",
                                    position=1)

    def test_plain_wheel_init(self):
        self.assertEqual("CDEMUXPNVZBHYFQWKIATGLORSJ", self.plain_wheel._letters)
        self.assertEqual("A", self.plain_wheel._starting_pos)
        self.assertEqual("E", self.plain_wheel._turnover)
        self.assertEqual(0, self.plain_wheel._position)
        self.assertEqual("DEMUXPNVZBHYFQWKIATGLORSJC", self.offset_wheel._letters)
        self.assertEqual("D", self.offset_wheel._starting_pos)
        self.assertEqual("E", self.offset_wheel._turnover)
        self.assertEqual(1, self.offset_wheel._position)

    def test__gt(self):
        self.assertEqual(False, self.offset_wheel > self.plain_wheel)
        self.assertEqual(True, self.offset_wheel < self.plain_wheel)

    def test_position_in_machine(self):
        self.assertEqual(0, self.plain_wheel.position_in_machine())
        self.assertEqual(1, self.offset_wheel.position_in_machine())

    def test_get_current_position(self):
        self.assertEqual("A", self.plain_wheel.get_current_position())
        self.assertEqual("D", self.offset_wheel.get_current_position())

    def test_set_current_position(self):
        self.plain_wheel._offset = 0
        self.plain_wheel.set_current_position("Z")
        self.assertEqual(25, self.plain_wheel._offset)

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
        self.plain_wheel.rotate_once()
        self.assertEqual("T", self.plain_wheel.forward_flow("D"))

    def test_will_cause_turnover(self):
        self.plain_wheel._offset = 0
        self.assertEqual(False, self.plain_wheel.will_cause_turnover())
        self.plain_wheel._offset = 4
        self.assertEqual(True, self.plain_wheel.will_cause_turnover())

    def test_previous_letter_caused_turnover(self):
        self.plain_wheel._offset = 4
        self.assertEqual(False, self.plain_wheel.previous_letter_caused_turnover())
        self.plain_wheel._offset = 5
        self.assertEqual(True, self.plain_wheel.previous_letter_caused_turnover())

    def test_handle_ring_setting(self):
        self.assertEqual("M", self.plain_wheel.forward_flow("D"))
        self.plain_wheel.set_ring_setting(3)
        self.assertEqual("F", self.plain_wheel.forward_flow("D"))
        self.plain_wheel._offset = 3
        self.plain_wheel.set_ring_setting(3)
        self.assertEqual("M", self.plain_wheel.forward_flow("D"))

    def test_single_rotor_I(self):
        self.assertEqual("E", self.rotor_I.forward_flow("A"))
        self.assertEqual("U", self.rotor_I.reverse_flow("A"))

    def test_has_notches(self):
        self.assertEqual(True, self.rotor_I.has_notches())
        self.assertEqual(False, self.rotor_no_notch.has_notches())
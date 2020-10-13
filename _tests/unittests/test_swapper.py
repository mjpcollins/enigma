from unittest import TestCase
from utils import Swapper


class Test_Swapper(TestCase):

    def setUp(self):
                                        #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.swapper_1 = Swapper(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        self.swapper_3 = Swapper(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO")

    def test_init(self):
        self.assertEqual("EKMFLGDQVZNTOWYHXUSPAIBRCJ", self.swapper_1._letters)
        self.assertEqual(0, self.swapper_1._offset)
        self.assertEqual("BDFHJLCPRTXVZNYEIWGAKMUSQO", self.swapper_3._letters)
        self.assertEqual(0, self.swapper_3._offset)

    def test_right_to_left(self):
        self.assertEqual("F", self.swapper_1._right_to_left("D"))
        self.assertEqual("J", self.swapper_1._right_to_left("Z"))

    def test_left_to_right(self):
        self.assertEqual("G", self.swapper_1._left_to_right("D"))
        self.assertEqual("J", self.swapper_1._left_to_right("Z"))

    def test_forwardflow(self):
        self.assertEqual("F", self.swapper_1.forward_flow("D"))
        self.assertEqual("J", self.swapper_1.forward_flow("Z"))

    def test_reverseflow(self):
        self.assertEqual("G", self.swapper_1.reverse_flow("D"))
        self.assertEqual("J", self.swapper_1.reverse_flow("Z"))

    def test_add_letter_offset(self):
        self.swapper_1._offset = 1
        self.assertEqual("B", self.swapper_1._add_letter_offset("A"))
        self.assertEqual("A", self.swapper_1._add_letter_offset("Z"))

    def test_minus_letter_offset(self):
        self.swapper_1._offset = 1
        self.assertEqual("Z", self.swapper_1._minus_letter_offset("A"))
        self.assertEqual("Y", self.swapper_1._minus_letter_offset("Z"))

    def test_increase_offset(self):
        self.assertEqual(0, self.swapper_1._offset)
        self.swapper_1.increase_offset()
        self.assertEqual(1, self.swapper_1._offset)
        self.swapper_1.increase_offset()
        self.assertEqual(2, self.swapper_1._offset)

    def test_decrease_offset(self):
        self.swapper_1._offset = 2
        self.assertEqual(2, self.swapper_1._offset)
        self.swapper_1.decrease_offset()
        self.assertEqual(1, self.swapper_1._offset)
        self.swapper_1.decrease_offset()
        self.assertEqual(0, self.swapper_1._offset)

    def test_offset_loops(self):
        self.swapper_1._offset = 25
        self.assertEqual(25, self.swapper_1._offset)
        self.swapper_1.increase_offset()
        self.assertEqual(0, self.swapper_1._offset)
        self.swapper_1.decrease_offset()
        self.assertEqual(25, self.swapper_1._offset)

    def test_add_offset(self):
        self.swapper_1._offset = 2
        self.assertEqual(4, self.swapper_1._add_offset(2))
        self.assertEqual(1, self.swapper_1._add_offset(25))

    def test_minus_offset(self):
        self.swapper_1._offset = 2
        self.assertEqual(2, self.swapper_1._minus_offset(4))
        self.assertEqual(25, self.swapper_1._minus_offset(1))

    def test_forward_flow_after_increase_offset(self):
        self.swapper_1._offset = 1
        self.assertEqual("K", self.swapper_1.forward_flow("D"))
        self.assertEqual("D", self.swapper_1.forward_flow("Z"))

    def test_forward_flow_after_decrease_offset(self):
        self.swapper_1._offset = 25
        self.assertEqual("N", self.swapper_1.forward_flow("D"))
        self.assertEqual("D", self.swapper_1.forward_flow("Z"))

    def test_3_forward_flow_position_L(self):
        self.swapper_3._offset = 11
        self.assertEqual("T", self.swapper_3.forward_flow("E"))

    def test_1_forward_flow_position_M(self):
        self.swapper_1._offset = 12
        self.assertEqual("B", self.swapper_1.forward_flow("Y"))

    def test_1_reverse_flow_position_M(self):
        self.swapper_1._offset = 12
        self.assertEqual("W", self.swapper_1.forward_flow("J"))

    def test_reverse_flow_after_increase_offset(self):
        self.swapper_1._offset = 1
        self.assertEqual("Z", self.swapper_1.reverse_flow("D"))
        self.assertEqual("T", self.swapper_1.reverse_flow("Z"))

    def test_reverse_flow_after_decrease_offset(self):
        self.swapper_1._offset = 25
        self.assertEqual("Z", self.swapper_1.reverse_flow("D"))
        self.assertEqual("P", self.swapper_1.reverse_flow("Z"))

    def test_get_ring_setting(self):
        self.assertEqual(0, self.swapper_1.get_ring_setting())
        self.swapper_1._ring_offset = 3
        self.assertEqual(3, self.swapper_1.get_ring_setting())

    def test_set_ring_setting(self):
        self.assertEqual(0, self.swapper_1._ring_offset)
        self.swapper_1.set_ring_setting(3)
        self.assertEqual(3, self.swapper_1._ring_offset)

    def test_can_handle_forward_flow_ring_offset(self):
        self.swapper_1._offset = 0
        self.swapper_1._ring_offset = 0
        self.assertEqual("F", self.swapper_1.forward_flow("D"))
        self.swapper_1._offset = 1
        self.swapper_1._ring_offset = 1
        self.assertEqual("F", self.swapper_1.forward_flow("D"))
        self.swapper_1._offset = 0
        self.swapper_1._ring_offset = 1
        self.assertEqual("N", self.swapper_1.forward_flow("D"))
        self.swapper_1._offset = 1
        self.swapper_1._ring_offset = 2
        self.assertEqual("N", self.swapper_1.forward_flow("D"))

    def test_can_handle_reverse_flow_ring_offset(self):
        self.swapper_1._offset = 0
        self.swapper_1._ring_offset = 0
        self.assertEqual("G", self.swapper_1._left_to_right("D"))
        self.swapper_1._offset = 1
        self.swapper_1._ring_offset = 1
        self.assertEqual("G", self.swapper_1._left_to_right("D"))
        self.swapper_1._offset = 0
        self.swapper_1._ring_offset = 1
        self.assertEqual("Z", self.swapper_1.reverse_flow("D"))
        self.swapper_1._offset = 1
        self.swapper_1._ring_offset = 2
        self.assertEqual("Z", self.swapper_1.reverse_flow("D"))





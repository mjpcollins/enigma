from unittest import TestCase
from utils import Scrambler, Settings


class Test_Scrambler(TestCase):

    def setUp(self):
        self.settings = Settings()
                                   #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.set_reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                start_position="A",
                                turnover="Q",
                                position=0)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="ESOVPZJAYQUIRHXLNFTGKDCMWB",
                                start_position="A",
                                turnover="J",
                                position=1)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                                start_position="B",
                                turnover="V",
                                position=2)
        self.scrambler = Scrambler(settings=self.settings)

    def test_flow_through(self):
        self.assertEqual("G", self.scrambler.flow_through("Z"))
        self.assertEqual("A", self.scrambler.flow_through("A"))

    def test_entry_wheel_in(self):
        self.assertEqual("A", self.scrambler._entry_wheel_in("A"))
        self.assertEqual("T", self.scrambler._entry_wheel_in("T"))

    def test_entry_wheel_out(self):
        self.assertEqual("A", self.scrambler._entry_wheel_in("A"))
        self.assertEqual("T", self.scrambler._entry_wheel_in("T"))

    def test_reflect(self):
        self.assertEqual("Y", self.scrambler._reflect("A"))
        self.assertEqual("T", self.scrambler._reflect("Z"))

    def test_flow_forward_through_wheels(self):
        self.assertEqual("J", self.scrambler._flow_forward_through_rotors("A"))
        self.assertEqual("X", self.scrambler._flow_forward_through_rotors("Z"))

    def test_flow_back_through_wheels(self):
        self.assertEqual("J", self.scrambler._flow_back_through_rotors("A"))
        self.assertEqual("B", self.scrambler._flow_back_through_rotors("Z"))

    def test_find_fast_wheel(self):
        wheel = self.scrambler._find_fast_rotor()
        self.assertEqual("EKMFLGDQVZNTOWYHXUSPAIBRCJ", wheel._letters)
        self.assertEqual("A", wheel.get_current_position())
        self.assertEqual("A", wheel._starting_pos)
        self.assertEqual("Q", wheel._turnover)

    def test_find_wheels_to_turnover(self):
        self.scrambler._rotors[0].set_current_position("Q")
        wheels = self.scrambler._find_rotors_to_turnover()

        self.assertEqual(2, len(wheels))
        self.assertEqual("EKMFLGDQVZNTOWYHXUSPAIBRCJ", wheels[0]._letters)
        self.assertEqual("Q", wheels[0].get_current_position())
        self.assertEqual("A", wheels[0]._starting_pos)
        self.assertEqual("Q", wheels[0]._turnover)

        self.assertEqual("ESOVPZJAYQUIRHXLNFTGKDCMWB", wheels[1]._letters)
        self.assertEqual("A", wheels[1].get_current_position())
        self.assertEqual("A", wheels[1]._starting_pos)
        self.assertEqual("J", wheels[1]._turnover)

    def test_find_wheels_permitted_to_rotate(self):
        self.scrambler._rotors[0].set_current_position("Q")
        wheels = self.scrambler._find_rotors_permitted_to_rotate()

        self.assertEqual(2, len(wheels))
        self.assertEqual("EKMFLGDQVZNTOWYHXUSPAIBRCJ", wheels[0]._letters)
        self.assertEqual("Q", wheels[0].get_current_position())
        self.assertEqual("A", wheels[0]._starting_pos)
        self.assertEqual("Q", wheels[0]._turnover)

        self.assertEqual("ESOVPZJAYQUIRHXLNFTGKDCMWB", wheels[1]._letters)
        self.assertEqual("A", wheels[1].get_current_position())
        self.assertEqual("A", wheels[1]._starting_pos)
        self.assertEqual("J", wheels[1]._turnover)

    def test_rotate_wheels(self):
        self.assertEqual("A", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("A", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("B", self.scrambler._rotors[2].get_current_position())
        self.scrambler.rotate_rotors()
        self.assertEqual("B", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("A", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("B", self.scrambler._rotors[2].get_current_position())

    def test_double_step(self):
       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual("A", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("A", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("B", self.scrambler._rotors[2].get_current_position())
        for _ in range(16 + 9 * 26):
            self.scrambler.rotate_rotors()
        self.assertEqual("Q", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("J", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("B", self.scrambler._rotors[2].get_current_position())
        self.scrambler.rotate_rotors()
        self.assertEqual("R", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("K", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("C", self.scrambler._rotors[2].get_current_position())
        self.scrambler.rotate_rotors()
        self.assertEqual("S", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("K", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("C", self.scrambler._rotors[2].get_current_position())

    # def test_scramble_letter_A(self):
    #     self.assertEqual("U", self.scrambler.scramble_letter("A"))
    #
    # def test_scramble_letter_G(self):
    #     self.assertEqual("A", self.scrambler.scramble_letter("U"))

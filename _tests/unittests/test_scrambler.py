from unittest import TestCase
from utils import Scrambler, Settings


class Test_Scrambler(TestCase):

    def setUp(self):
        # Set up for I-II-III-B, AAB

        self.settings = Settings()
                                   #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.set_reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                start_position="A",
                                turnover="Q",
                                position=1)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                                start_position="A",
                                turnover="E",
                                position=2)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                                start_position="B",
                                turnover="V",
                                position=3)
        self.scrambler = Scrambler(settings=self.settings)

    def test_flow_through(self):
        self.assertEqual("B", self.scrambler.flow_through("A"))
        self.assertEqual("A", self.scrambler.flow_through("B"))

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
        self.assertEqual("F", self.scrambler._flow_forward_through_rotors("A"))
        self.assertEqual("E", self.scrambler._flow_forward_through_rotors("Z"))

    def test_flow_back_through_wheels(self):
        self.assertEqual("P", self.scrambler._flow_back_through_rotors("A"))
        self.assertEqual("F", self.scrambler._flow_back_through_rotors("Z"))

    def test_find_fast_wheel(self):
        wheel = self.scrambler._find_fast_rotor()
        self.assertEqual("BDFHJLCPRTXVZNYEIWGAKMUSQO", wheel._letters)
        self.assertEqual("B", wheel.get_current_position())
        self.assertEqual("B", wheel._starting_pos)
        self.assertEqual("V", wheel._turnover)

    def test_find_wheels_to_turnover(self):
        self.scrambler._rotors[0].set_current_position("V")
        wheels = self.scrambler._find_rotors_to_turnover()
        self.assert_rotor_1_and_2_selected(wheels)

    def test_find_double_step_rotors(self):
        self.scrambler._rotors[0].set_current_position("U")
        self.scrambler._rotors[1].set_current_position("E")
        self.scrambler._rotors[2].set_current_position("A")
        wheels = self.scrambler._find_rotors_permitted_to_rotate()
        self.assert_all_rotors_selected(wheels)
        self.scrambler.rotate_rotors()
        wheels = self.scrambler._find_rotors_permitted_to_rotate()
        self.assert_rotor_1_and_2_selected(wheels)

    def test_find_wheels_permitted_to_rotate(self):
        self.scrambler._rotors[0].set_current_position("V")
        wheels = self.scrambler._find_rotors_permitted_to_rotate()
        self.assert_rotor_1_and_2_selected(wheels)

    def test_rotate_wheels(self):
        self.assertEqual("B", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("A", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("A", self.scrambler._rotors[2].get_current_position())
        self.scrambler.rotate_rotors()
        self.assertEqual("C", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("A", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("A", self.scrambler._rotors[2].get_current_position())

    def test_MEU_double_step(self):
        self.scrambler._rotors[0].set_current_position("U")
        self.scrambler._rotors[1].set_current_position("E")
        self.scrambler._rotors[2].set_current_position("M")
        self.assertEqual("U", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("E", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("M", self.scrambler._rotors[2].get_current_position())
        self.scrambler.rotate_rotors()
        self.assertEqual("V", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("F", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("N", self.scrambler._rotors[2].get_current_position())
        self.scrambler.rotate_rotors()
        self.assertEqual("W", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("G", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("N", self.scrambler._rotors[2].get_current_position())
        self.scrambler.rotate_rotors()
        self.assertEqual("X", self.scrambler._rotors[0].get_current_position())
        self.assertEqual("G", self.scrambler._rotors[1].get_current_position())
        self.assertEqual("N", self.scrambler._rotors[2].get_current_position())

    def assert_rotor_1_and_2_selected(self, wheels):
        self.assertEqual(2, len(wheels))

        self.assertEqual("BDFHJLCPRTXVZNYEIWGAKMUSQO", wheels[0]._letters)
        self.assertEqual("B", wheels[0]._starting_pos)
        self.assertEqual("V", wheels[0]._turnover)

        self.assertEqual("AJDKSIRUXBLHWTMCQGZNPYFVOE", wheels[1]._letters)
        self.assertEqual("A", wheels[1]._starting_pos)
        self.assertEqual("E", wheels[1]._turnover)

    def assert_all_rotors_selected(self, wheels):
        self.assertEqual(3, len(wheels))

        self.assertEqual("BDFHJLCPRTXVZNYEIWGAKMUSQO", wheels[0]._letters)
        self.assertEqual("B", wheels[0]._starting_pos)
        self.assertEqual("V", wheels[0]._turnover)

        self.assertEqual("AJDKSIRUXBLHWTMCQGZNPYFVOE", wheels[1]._letters)
        self.assertEqual("A", wheels[1]._starting_pos)
        self.assertEqual("E", wheels[1]._turnover)

        self.assertEqual("EKMFLGDQVZNTOWYHXUSPAIBRCJ", wheels[2]._letters)
        self.assertEqual("B", wheels[0]._starting_pos)
        self.assertEqual("V", wheels[0]._turnover)

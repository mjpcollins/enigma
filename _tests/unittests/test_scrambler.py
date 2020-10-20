from unittest import TestCase
from utils import Scrambler, Settings, Data


class Test_Scrambler(TestCase):

    def setUp(self):
        settings = Settings()
        settings_4th_rotor = Settings()

        self.data = Data()
        self.data.set_machine("example_machine")
        self.gamma = self.data.get_rotor("gamma")
        self.i = self.data.get_rotor("i")
        self.ii = self.data.get_rotor("ii")
        self.iii = self.data.get_rotor("iii")
        self.gamma.update({"start_position": "A", "position": 1})
        self.i.update({"start_position": "A", "position": 2})
        self.ii.update({"start_position": "A", "position": 3})
        self.iii.update({"start_position": "B", "position": 4})

        settings.set_reflector(**self.data.get_reflector("b"))
        settings.add_rotors([self.i, self.ii, self.iii])
        self.scrambler = Scrambler(settings=settings)

        settings_4th_rotor.add_rotors([self.i, self.ii, self.iii, self.gamma])
        settings_4th_rotor.set_reflector(**self.data.get_reflector("b"))
        self.scrambler_with_fourth_rotor = Scrambler(settings=settings_4th_rotor)

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

    def test_find_fourth_rotor(self):
        self.assertEqual(None, self.scrambler._find_fourth_rotor())
        self.assertEqual("FSOKANUERHMBTIYCWLQPZXVGJD", self.scrambler_with_fourth_rotor._find_fourth_rotor()._letters)

    def test_remove_fourth_rotor(self):
        rotors_selected = set(self.scrambler_with_fourth_rotor._rotors[0:])
        expected = set(self.scrambler_with_fourth_rotor._rotors[0:3])
        self.scrambler_with_fourth_rotor._remove_fourth_rotor(rotors_selected)
        self.assertSetEqual(expected, rotors_selected)

    def test_never_move_4th_rotor(self):
        self.scrambler_with_fourth_rotor._rotors[0].set_current_position("V")
        self.scrambler_with_fourth_rotor._rotors[1].set_current_position("E")
        self.scrambler_with_fourth_rotor._rotors[2].set_current_position("Q")
        self.scrambler_with_fourth_rotor.rotate_rotors()
        self.assertEqual("W", self.scrambler_with_fourth_rotor._rotors[0].get_current_position())
        self.assertEqual("F", self.scrambler_with_fourth_rotor._rotors[1].get_current_position())
        self.assertEqual("R", self.scrambler_with_fourth_rotor._rotors[2].get_current_position())
        self.assertEqual("A", self.scrambler_with_fourth_rotor._rotors[3].get_current_position())

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

    def test_non_notch_rotor_preventing_rotations(self):
        settings = Settings()
        data = Data()
        data.set_machine("example_machine")

        iv = data.get_rotor("iv")
        v = data.get_rotor("v")
        beta = data.get_rotor("beta")
        i = data.get_rotor("i")

        iv.update({"start_position": "E", "ring_setting": 18, "position": 1})
        v.update({"start_position": "Z", "ring_setting": 24, "position": 2})
        beta.update({"start_position": "G", "ring_setting": 3, "position": 3})
        i.update({"start_position": "P", "ring_setting": 5, "position": 4})

        settings.add_rotors([iv, v, beta, i])
        settings.set_reflector(**data.get_reflector("a"))

        scrambler = Scrambler(settings=settings)
        self.assertEqual("E", scrambler._rotors[3].get_current_position())
        self.assertEqual("Z", scrambler._rotors[2].get_current_position())
        self.assertEqual("G", scrambler._rotors[1].get_current_position())
        self.assertEqual("P", scrambler._rotors[0].get_current_position())
        scrambler.rotate_rotors()
        self.assertEqual("E", scrambler._rotors[3].get_current_position())
        self.assertEqual("Z", scrambler._rotors[2].get_current_position())
        self.assertEqual("G", scrambler._rotors[1].get_current_position())
        self.assertEqual("Q", scrambler._rotors[0].get_current_position())


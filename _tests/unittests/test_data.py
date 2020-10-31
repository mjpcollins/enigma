from unittest import TestCase
from utils import Data


class Test_Data(TestCase):

    def setUp(self):
        self.data = Data()

    def test_init(self):
        self.assertEqual("./data/rotors.json", self.data._filename)
        self.assertEqual(True, "example_machine" in self.data._loaded_json.keys())
        self.assertEqual(None, self.data._machine)

    def test_get_machine(self):
        self.assertEqual(None, self.data.get_machine())
        self.data._machine = "example_machine"
        self.assertEqual("example_machine", self.data.get_machine())

    def test_set_machine(self):
        self.assertEqual(None, self.data._machine)
        self.data.set_machine("example_machine")
        self.assertEqual("example_machine", self.data._machine)

    def test_get_rotor(self):
        self.data._machine = "example_machine"
        self.assertEqual({"letters": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                          "turnover": "E"}, self.data.get_rotor("ii"))
        self.assertEqual({"letters": "VZBRGITYUPSDNHLXAWMJQOFECK",
                          "turnover": "Z"}, self.data.get_rotor("v"))
        self.assertEqual(None, self.data.get_rotor("abba"))

    def test_get_reflector(self):
        self.data._machine = "example_machine"
        self.assertEqual({"letters": "EJMZALYXVBWFCRQUONTSPIKHGD"}, self.data.get_reflector("a"))
        self.assertEqual({"letters": "YRUHQSLDPXNGOKMIEBFZCWVJAT"}, self.data.get_reflector("b"))
        self.assertEqual(None, self.data.get_reflector("abba"))

    def test_get_entry_wheel(self):
        self.data._machine = "example_machine"
        self.assertEqual({"letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}, self.data.get_entry_wheel("etw"))
        self.assertEqual(None, self.data.get_entry_wheel("abba"))

    def test_list_rotors(self):
        self.data._machine = "example_machine"
        self.assertListEqual(["beta", "gamma", "i", "ii", "iii", "iv", "v"], self.data.list_rotors())

    def test_list_reflectors(self):
        self.data._machine = "example_machine"
        self.assertListEqual(["a", "b", "c"], self.data.list_reflectors())

    def test_list_entry_wheels(self):
        self.data._machine = "example_machine"
        self.assertListEqual(["etw"], self.data.list_entry_wheels())

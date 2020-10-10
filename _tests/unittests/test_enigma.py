from unittest import TestCase
from utils import Enigma, Settings


class Test_Enigma(TestCase):

    def setUp(self):
        self.settings = Settings()
                                   #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.set_reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_wheel(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                start_position="E",
                                turnover="Q",
                                position=0)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_wheel(letters="ESOVPZJAYQUIRHXLNFTGKDCMWB",
                                start_position="E",
                                turnover="J",
                                position=1)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_wheel(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                                start_position="B",
                                turnover="V",
                                position=2)
        self.settings.set_switchboard_pairs(["NI", "KF", "PY", "VB", "CG", "WR", "TQ", "OS", "LH", "DZ"])
        self.enigma = Enigma(settings=self.settings)

    def test_press_key_A(self):
        self.assertEqual("C", self.enigma.press_key("A"))

    def test_press_key_C(self):
        self.assertEqual("A", self.enigma.press_key("C"))
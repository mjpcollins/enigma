from unittest import TestCase
from utils import Enigma, Settings


class Test_Enigma(TestCase):

    def setUp(self):
        self.settings = Settings()
                                   #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.set_reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                start_position="E",
                                turnover="Q",
                                position=0)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="ESOVPZJAYQUIRHXLNFTGKDCMWB",
                                start_position="E",
                                turnover="J",
                                position=1)
                                       #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                                start_position="B",
                                turnover="V",
                                position=2)
        self.settings.set_switchboard_pairs(["NI", "KF", "PY", "VB", "CG", "WR", "TQ", "OS", "LH", "DZ"])
        self.enigma = Enigma(settings=self.settings)

    # def test_press_key_A(self):
    #     self.assertEqual("C", self.enigma.press_key("A"))
    #
    # def test_press_key_C(self):
    #     self.assertEqual("A", self.enigma.press_key("C"))

    def test_MCK(self):
        settings = Settings()
        settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                           start_position="M",
                           turnover="Q",
                           position=1)
        settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                           start_position="C",
                           turnover="E",
                           position=2)
        settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                           start_position="K",
                           turnover="V",
                           position=3)
        enigma = Enigma(settings=settings)
        self.assertEqual("A", enigma.press_key("T"))
        self.assertEqual("P", enigma.press_key("H"))
        self.assertEqual("Z", enigma.press_key("E"))
        self.assertEqual("M", enigma.press_key("Q"))
        self.assertEqual("T", enigma.press_key("U"))

    def test_MEU(self):
        settings = Settings()
        settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                           start_position="M",
                           turnover="Q",
                           position=1)
        settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                           start_position="E",
                           turnover="E",
                           position=2)
        settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                           start_position="U",
                           turnover="V",
                           position=3)
        enigma = Enigma(settings=settings)
        self.assertEqual("G", enigma.press_key("A"))
        self.assertEqual("D", enigma.press_key("A"))
        self.assertEqual("X", enigma.press_key("A"))
        self.assertEqual("T", enigma.press_key("A"))
        self.assertEqual("Z", enigma.press_key("A"))

from unittest import TestCase
from utils import Enigma, Settings


class Test_Enigma(TestCase):

    def test_AAZ(self):
        settings = Settings()
        settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                           start_position="A",
                           turnover="Q",
                           position=1)
        settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                           start_position="A",
                           turnover="E",
                           position=2)
        settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                           start_position="Z",
                           turnover="V",
                           position=3)
        enigma = Enigma(settings=settings)
        self.assertEqual("U", enigma.press_key("A"))

    def test_AAA(self):
        settings = Settings()
        settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                           start_position="A",
                           turnover="Q",
                           position=1)
        settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                           start_position="A",
                           turnover="E",
                           position=2)
        settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                           start_position="A",
                           turnover="V",
                           position=3)
        enigma = Enigma(settings=settings)
        self.assertEqual("B", enigma.press_key("A"))

    def test_QEV(self):
        settings = Settings()
        settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                           start_position="Q",
                           turnover="Q",
                           position=1)
        settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                           start_position="E",
                           turnover="E",
                           position=2)
        settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                           start_position="V",
                           turnover="V",
                           position=3)
        enigma = Enigma(settings=settings)
        self.assertEqual("L", enigma.press_key("A"))

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

    # def test_IV_V_Beta_B_AAA_ring_settings_14_09_24(self):
    #     settings = Settings()
    #     settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
    #     settings.add_rotor(letters="ESOVPZJAYQUIRHXLNFTGKDCMWB",
    #                        start_position="A",
    #                        turnover="J",
    #                        position=1,
    #                        ring_setting=14)
    #     settings.add_rotor(letters="VZBRGITYUPSDNHLXAWMJQOFECK",
    #                        start_position="A",
    #                        turnover="Z",
    #                        position=2,
    #                        ring_setting=9)
    #     settings.add_rotor(letters="EYJVCNIXWPBQMDRTAKZGFUHOS",
    #                        start_position="A",
    #                        turnover="",
    #                        position=3,
    #                        ring_setting=24)
    #     enigma = Enigma(settings=settings)
    #     self.assertEqual("Y", enigma.press_key("H"))

    def test_parse(self):
        settings = Settings()
        settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                           start_position="A",
                           turnover="Q",
                           position=1)
        settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                           start_position="A",
                           turnover="E",
                           position=2)
        settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                           start_position="Z",
                           turnover="V",
                           position=3)
        settings.set_switchboard_pairs(["HL", "MO", "AJ", "CX", "BZ",
                                        "SR", "NI", "YW", "DG", "PK"])
        enigma = Enigma(settings=settings)
        self.assertEqual("RFKTMBXVVW", enigma.parse("HELLOWORLD"))


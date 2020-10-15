from unittest import TestCase
from utils import Enigma, Settings, Data


class Test_Enigma(TestCase):

    def setUp(self):
        self.data_obj = Data()
        self.data_obj.set_machine("example_machine")
        self.settings = Settings()
        self.I = self.data_obj.get_rotor("i")
        self.II = self.data_obj.get_rotor("ii")
        self.III = self.data_obj.get_rotor("iii")
        self.IV = self.data_obj.get_rotor("iv")
        self.V = self.data_obj.get_rotor("v")
        self.Beta = self.data_obj.get_rotor("beta")
        self.Gamma = self.data_obj.get_rotor("gamma")
        self.A = self.data_obj.get_reflector("a")
        self.B = self.data_obj.get_reflector("b")
        self.C = self.data_obj.get_reflector("c")

    def test_AAZ(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A", "position": 2})
        self.III.update({"start_position": "Z", "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("U", Enigma(settings=self.settings).press_key("A"))

    def test_AAA(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A", "position": 2})
        self.III.update({"start_position": "A", "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("B", Enigma(settings=self.settings).press_key("A"))

    def test_QEV(self):
        self.I.update({"start_position": "Q", "position": 1})
        self.II.update({"start_position": "E", "position": 2})
        self.III.update({"start_position": "V", "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("L", Enigma(settings=self.settings).press_key("A"))

    def test_MCK(self):
        self.I.update({"start_position": "M", "position": 1})
        self.II.update({"start_position": "C", "position": 2})
        self.III.update({"start_position": "K", "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("APZMT", Enigma(settings=self.settings).parse("THEQU"))

    def test_MEU(self):
        self.I.update({"start_position": "M", "position": 1})
        self.II.update({"start_position": "E", "position": 2})
        self.III.update({"start_position": "U", "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("GDXTZ", Enigma(settings=self.settings).parse("AAAAA"))

    def test_IV_V_Beta_B_AAA_ring_settings_14_09_24(self):
        self.IV.update({"start_position": "A", "ring_setting": 14, "position": 1})
        self.V.update({"start_position": "A", "ring_setting": 9, "position": 2})
        self.Beta.update({"start_position": "A", "ring_setting": 24, "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.IV, self.V, self.Beta])
        self.assertEqual("Y", Enigma(settings=self.settings).press_key("H"))

    def test_I_II_III_IV_C_QEVZ_ring_settings_07_11_15_19(self):
        self.I.update({"start_position": "Q", "ring_setting": 7, "position": 1})
        self.II.update({"start_position": "E", "ring_setting": 11, "position": 2})
        self.III.update({"start_position": "V", "ring_setting": 15, "position": 3})
        self.IV.update({"start_position": "Z", "ring_setting": 19, "position": 4})
        self.settings.set_reflector(**self.C)
        self.settings.add_rotors([self.I, self.II, self.III, self.IV])
        self.assertEqual("V", Enigma(settings=self.settings).press_key("Z"))

    def test_I_II_III_B_AAA_ring_settings_01_01_02(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A",  "position": 2})
        self.III.update({"start_position": "A", "ring_setting": 2, "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("U", Enigma(settings=self.settings).press_key("A"))

    def test_parse(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A", "position": 2})
        self.III.update({"start_position": "Z", "position": 3})
        self.settings.set_reflector(**self.B)
        self.settings.add_rotors([self.I, self.II, self.III])
        self.settings.set_switchboard_pairs(["HL", "MO", "AJ", "CX", "BZ",
                                             "SR", "NI", "YW", "DG", "PK"])
        self.assertEqual("RFKTMBXVVW", Enigma(settings=self.settings).parse("HELLOWORLD"))

    def test_m4_Beta_I_II_III_B_Thin_AAA(self):
        settings = Settings()
        data = Data()
        data.set_machine("m4")
        beta = data.get_rotor("beta")
        i = data.get_rotor("i")
        ii = data.get_rotor("ii")
        iii = data.get_rotor("iii")
        beta.update({"start_position": "A", "position": 1})
        i.update({"start_position": "P", "position": 2})
        ii.update({"start_position": "E", "position": 3})
        iii.update({"start_position": "V", "position": 4})
        settings.add_rotors([beta, i, ii, iii])
        settings.set_reflector(**data.get_reflector("b-thin"))
        self.assertEqual("QNPJG", Enigma(settings=settings).parse("AAAAA"))

        settings = Settings()
        beta.update({"start_position": "A", "position": 1})
        i.update({"start_position": "Q", "position": 2})
        ii.update({"start_position": "E", "position": 3})
        iii.update({"start_position": "V", "position": 4})
        settings.add_rotors([beta, i, ii, iii])
        settings.set_reflector(**data.get_reflector("b-thin"))
        enigma = Enigma(settings=settings)
        print(enigma.scrambler._rotors[0].get_current_position())
        print(enigma.scrambler._rotors[1].get_current_position())
        print(enigma.scrambler._rotors[2].get_current_position())
        print(enigma.scrambler._rotors[3].get_current_position())
        print("----")
        print(enigma.press_key("A"))
        print("----")
        print(enigma.scrambler._rotors[0].get_current_position())
        print(enigma.scrambler._rotors[1].get_current_position())
        print(enigma.scrambler._rotors[2].get_current_position())
        print(enigma.scrambler._rotors[3].get_current_position())
        print("----")
        print(enigma.press_key("A"))
        print("----")
        print(enigma.scrambler._rotors[0].get_current_position())
        print(enigma.scrambler._rotors[1].get_current_position())
        print(enigma.scrambler._rotors[2].get_current_position())
        print(enigma.scrambler._rotors[3].get_current_position())
        print("----")
        print(enigma.press_key("A"))
        print("----")
        print(enigma.scrambler._rotors[0].get_current_position())
        print(enigma.scrambler._rotors[1].get_current_position())
        print(enigma.scrambler._rotors[2].get_current_position())
        print(enigma.scrambler._rotors[3].get_current_position())

        self.assertEqual("KNEKO", "AAAAA")

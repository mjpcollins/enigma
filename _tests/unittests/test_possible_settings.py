from unittest import TestCase
from utils import PossibleSettings, Reflector, EntryWheel


class Test_PossibleSettings(TestCase):

    def setUp(self):
        self.ps = PossibleSettings()
        self.expected_m4_settings = {'rotor_choices': [{"letters": "VZBRGITYUPSDNHLXAWMJQOFECK", "turnover": "Z"},
                                                       {"letters": "JPGVOUMFYQBENHZRDKASXLICTW", "turnover": "ZM"},
                                                       {"letters": "NZJHGRCXMYSWBOUFAIVLPEKQDT", "turnover": "ZM"}],
                                     'ring_settings': [1, 5, 7],
                                     'start_positions': 'ABCDEF'}
        self.ps.set_machine("m4")

    def test_init(self):
        self.assertEqual("./data/rotors.json", self.ps._data._filename)
        self.assertEqual("m4", self.ps._data._machine)
        self.assertDictEqual({"entry_wheels": [], "rotor_1": {}, "rotor_2": {}, "rotor_3": {},
                              "reflectors": [], "switchboards": []}, self.ps._possible_settings)

    def test_set_machine(self):
        self.assertEqual("m4", self.ps._data._machine)
        self.ps.set_machine("example_machine")
        self.assertEqual("example_machine", self.ps._data._machine)

    def test_generate_rotor_possible_settings_all(self):
        self.ps.set_machine("example_machine")
        expected_dict = {'rotor_choices': [{'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': ''}, {'letters': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'turnover': ''}, {'letters': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'turnover': 'Q'}, {'letters': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'turnover': 'E'}, {'letters': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'turnover': 'V'}, {'letters': 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'turnover': 'J'}, {'letters': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'turnover': 'Z'}],
                         'ring_settings': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
                         'start_positions': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        actual_dict = self.ps._generate_rotor_options()
        self.assertEqual(expected_dict, actual_dict)

    def test_generate_rotor_possible_settings_limited(self):
        actual_dict = self.ps._generate_rotor_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(self.expected_m4_settings, actual_dict)

    def test_generate_rotor_1_options(self):
        self.ps.generate_rotor_1_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(self.expected_m4_settings, self.ps._possible_settings['rotor_1'])

    def test_generate_rotor_2_options(self):
        self.ps.generate_rotor_2_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(self.expected_m4_settings, self.ps._possible_settings['rotor_2'])

    def test_generate_rotor_3_options(self):
        self.ps.generate_rotor_3_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(self.expected_m4_settings, self.ps._possible_settings['rotor_3'])

    def test_generate_reflector_options(self):
        expected_list = [Reflector(letters="ENKQAUYWJICOPBLMDXZVFTHRGS")._letters,
                         Reflector(letters="RDOBJNTKVEHMLFCWZAXGYIPSUQ")._letters]
        self.ps.generate_reflector_options()

        self.assertEqual(len(expected_list), len(self.ps._possible_settings['reflectors']))
        for reflector in self.ps._possible_settings['reflectors']:
            self.assertIn(reflector._letters, expected_list)

    def test_generate_reflector_options_limited(self):
        expected_list = [Reflector(letters="ENKQAUYWJICOPBLMDXZVFTHRGS")._letters]
        self.ps.generate_reflector_options(reflectors=["b-thin"])

        self.assertEqual(len(expected_list), len(self.ps._possible_settings['reflectors']))
        for reflector in self.ps._possible_settings['reflectors']:
            self.assertIn(reflector._letters, expected_list)

    def test_generate_entry_wheel_options(self):
        expected_list = [EntryWheel()._letters]
        self.ps.generate_entry_wheel_options()

        self.assertEqual(len(expected_list), len(self.ps._possible_settings['entry_wheels']))
        for etw in self.ps._possible_settings['entry_wheels']:
            self.assertIn(etw._letters, expected_list)

    def test_generate_iter_list(self):
        expected_pairs = ['AB', 'AC', 'AD', 'AE', 'AF',
                          'AG', 'AH', 'AI', 'AJ', 'AK',
                          'AL', 'AM', 'AN', 'AO', 'AP',
                          'AQ', 'AR', 'AS', 'AT', 'AU',
                          'AV', 'AW', 'AX', 'AY', 'AZ']
        self.assertListEqual(expected_pairs, self.ps._generate_pairs_options_list("A?"))

    def test_generate_iter_list_with_exclusions(self):
        expected_pairs = ['AG', 'AH', 'AI', 'AJ', 'AK',
                          'AL', 'AM', 'AN', 'AO', 'AP',
                          'AQ', 'AR', 'AS', 'AT', 'AU',
                          'AV', 'AW', 'AX', 'AY', 'AZ']
        self.assertListEqual(expected_pairs, self.ps._generate_pairs_options_list("A?", exclusions="BCDEF"))

    def test_generate_switchboard_options_one_unknown(self):
        expected_list = [['AB', 'ZR', 'XC'], ['AB', 'ZR', 'XD'], ['AB', 'ZR', 'XE'],
                         ['AB', 'ZR', 'XF'], ['AB', 'ZR', 'XG'], ['AB', 'ZR', 'XH'],
                         ['AB', 'ZR', 'XI'], ['AB', 'ZR', 'XJ'], ['AB', 'ZR', 'XK'],
                         ['AB', 'ZR', 'XL'], ['AB', 'ZR', 'XM'], ['AB', 'ZR', 'XN'],
                         ['AB', 'ZR', 'XO'], ['AB', 'ZR', 'XP'], ['AB', 'ZR', 'XQ'],
                         ['AB', 'ZR', 'XS'], ['AB', 'ZR', 'XT'], ['AB', 'ZR', 'XU'],
                         ['AB', 'ZR', 'XV'], ['AB', 'ZR', 'XW'], ['AB', 'ZR', 'XY']]
        input_list = ['AB', 'ZR', 'X?']
        self.assertListEqual(expected_list, self.ps.generate_switchboard_options(input_list))

    def test_remove_contradictions_from_switchboard(self):
        input_list = [['AB', 'ZR', 'XC'], ['AB', 'ZR', 'XD'], ['AB', 'ZR', 'XZ']]
        expected_list = [['AB', 'ZR', 'XC'], ['AB', 'ZR', 'XD']]
        self.assertListEqual(expected_list, self.ps._remove_contradictions_from_switchboard(input_list))


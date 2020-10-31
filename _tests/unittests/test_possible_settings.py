from unittest import TestCase
from utils import PossibleSettings, Data


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
        self.assertDictEqual({"machine": "m4", "entry_wheels": [], "rotor_1": {}, "rotor_2": {}, "rotor_3": {}, "rotor_4": {},
                              "reflectors": [], "switchboards": []}, self.ps._possible_settings)

    def test_set_machine(self):
        self.assertEqual("m4", self.ps._data._machine)
        self.assertEqual("m4", self.ps._possible_settings['machine'])
        self.ps.set_machine("example_machine")
        self.assertEqual("example_machine", self.ps._data._machine)
        self.assertEqual("example_machine", self.ps._possible_settings['machine'])

    def test_generate_rotor_possible_settings_all(self):
        self.ps.set_machine("example_machine")
        expected_dict = {'rotor_choices': [{'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1},
                                           {'letters': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'turnover': '', 'position': 1},
                                           {'letters': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'turnover': 'Q', 'position': 1},
                                           {'letters': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'turnover': 'E', 'position': 1},
                                           {'letters': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'turnover': 'V', 'position': 1},
                                           {'letters': 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'turnover': 'J', 'position': 1},
                                           {'letters': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'turnover': 'Z', 'position': 1}],
                         'ring_settings': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
                         'start_positions': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

        actual_dict = self.ps._generate_rotor_options(machine_position=1)
        self.assertEqual(expected_dict, actual_dict)

    def test_generate_rotor_1_options(self):
        expected_r1_settings = {'rotor_choices': [{"letters": "VZBRGITYUPSDNHLXAWMJQOFECK", "turnover": "Z", "position": 1},
                                                  {"letters": "JPGVOUMFYQBENHZRDKASXLICTW", "turnover": "ZM", "position": 1},
                                                  {"letters": "NZJHGRCXMYSWBOUFAIVLPEKQDT", "turnover": "ZM", "position": 1}],
                                'ring_settings': [1, 5, 7],
                                'start_positions': 'ABCDEF'}
        self.ps.generate_rotor_1_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(expected_r1_settings, self.ps._possible_settings['rotor_1'])

    def test_generate_rotor_2_options(self):
        expected_r2_settings = {'rotor_choices': [{"letters": "VZBRGITYUPSDNHLXAWMJQOFECK", "turnover": "Z", "position": 2},
                                                  {"letters": "JPGVOUMFYQBENHZRDKASXLICTW", "turnover": "ZM", "position": 2},
                                                  {"letters": "NZJHGRCXMYSWBOUFAIVLPEKQDT", "turnover": "ZM", "position": 2}],
                                'ring_settings': [1, 5, 7],
                                'start_positions': 'ABCDEF'}
        self.ps.generate_rotor_2_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(expected_r2_settings, self.ps._possible_settings['rotor_2'])

    def test_generate_rotor_3_options(self):
        expected_r3_settings = {'rotor_choices': [{"letters": "VZBRGITYUPSDNHLXAWMJQOFECK", "turnover": "Z", "position": 3},
                                                  {"letters": "JPGVOUMFYQBENHZRDKASXLICTW", "turnover": "ZM", "position": 3},
                                                  {"letters": "NZJHGRCXMYSWBOUFAIVLPEKQDT", "turnover": "ZM", "position": 3}],
                                'ring_settings': [1, 5, 7],
                                'start_positions': 'ABCDEF'}
        self.ps.generate_rotor_3_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(expected_r3_settings, self.ps._possible_settings['rotor_3'])

    def test_generate_rotor_4_options(self):
        expected_r4_settings = {'rotor_choices': [{"letters": "VZBRGITYUPSDNHLXAWMJQOFECK", "turnover": "Z", "position": 4},
                                                  {"letters": "JPGVOUMFYQBENHZRDKASXLICTW", "turnover": "ZM", "position": 4},
                                                  {"letters": "NZJHGRCXMYSWBOUFAIVLPEKQDT", "turnover": "ZM", "position": 4}],
                                'ring_settings': [1, 5, 7],
                                'start_positions': 'ABCDEF'}
        self.ps.generate_rotor_4_options(rotors=['v', 'vi', 'vii'], ring_settings=[1, 5, 7], start_positions="ABCDEF")
        self.assertEqual(expected_r4_settings, self.ps._possible_settings['rotor_4'])

    def test_generate_reflector_options(self):
        self.ps.generate_reflector_options()
        self.assertListEqual([{"letters": "ENKQAUYWJICOPBLMDXZVFTHRGS"}, {"letters": "RDOBJNTKVEHMLFCWZAXGYIPSUQ"}],
                             self.ps._possible_settings['reflectors'])

    def test_generate_reflector_options_limited(self):
        self.ps.generate_reflector_options(reflectors=["b-thin"])
        self.assertListEqual([{"letters": "ENKQAUYWJICOPBLMDXZVFTHRGS"}], self.ps._possible_settings['reflectors'])

    def test_generate_entry_wheel_options(self):
        self.ps.generate_entry_wheel_options()
        self.assertListEqual([{"letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}], self.ps._possible_settings['entry_wheels'])

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
        self.ps.generate_switchboard_options(input_list)
        self.assertListEqual(expected_list, self.ps._possible_settings['switchboards'])

    def test_remove_contradictions_from_switchboard(self):
        input_list = [['AB', 'ZR', 'XC'], ['AB', 'ZR', 'XD'], ['AB', 'ZR', 'XZ']]
        expected_list = [['AB', 'ZR', 'XC'], ['AB', 'ZR', 'XD']]
        self.assertListEqual(expected_list, self.ps._remove_contradictions_from_switchboard(input_list))

    def test_non_standard_reflector_generator(self):
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "EJMZALYXVBWFCRQUONTSPIKHGD"

    def test_swap_one_rotor_wire(self):
        reflector = Data(machine="example_machine").get_reflector("a")
        swapped_reflector = self.ps._swap_one_reflector_wire(reflector, "AB")
        self.assertEqual("EJMZALYXVBWFCRQUONTSPIKHGD", reflector['letters'])
        self.assertEqual("JEMZBLYXVAWFCRQUONTSPIKHGD", swapped_reflector['letters'])

    def test_generate_custom_wiring_options_1_alteration(self):
        self.assertEqual(325, len(self.ps._generate_custom_wiring_options(1)))
        self.assertEqual('AB', self.ps._generate_custom_wiring_options(1)[0])
        self.assertEqual('AV', self.ps._generate_custom_wiring_options(1)[20])

    def test_generate_custom_wiring_options_2_alterations(self):
        self.assertEqual(89700, len(self.ps._generate_custom_wiring_options(2)))
        self.assertEqual('ABCD', self.ps._generate_custom_wiring_options(2)[0])
        self.assertEqual('ABCX', self.ps._generate_custom_wiring_options(2)[20])

    def test_swap_reflector_wires(self):
        reflector = Data(machine="example_machine").get_reflector("a")
        swapped_reflector = self.ps._swap_reflector_wires(reflector, "ABCD")
        self.assertEqual("EJMZALYXVBWFCRQUONTSPIKHGD", reflector['letters'])
        self.assertEqual("JEZMBLYXVAWFDRQUONTSPIKHGC", swapped_reflector['letters'])

    def test_swap_reflector_wires_not_possible(self):
        reflector = Data(machine="example_machine").get_reflector("a")
        swapped_reflector = self.ps._swap_reflector_wires(reflector, "EA")
        self.assertEqual(None, swapped_reflector)

    def test_generate_custom_reflector_options(self):
        self.ps.set_machine("example_machine")
        self.ps.generate_custom_reflector_options(reflectors='a', alterations=1)
        self.assertEqual(312, len(self.ps._possible_settings['reflectors']))
        self.assertEqual({'letters': 'KJMZWLYXVBAFCRQUONTSPIEHGD'}, self.ps._possible_settings['reflectors'][20])
        self.assertEqual({'letters': 'JEMZBLYXVAWFCRQUONTSPIKHGD'}, self.ps._possible_settings['reflectors'][0])

    def test_generate_custom_reflector_options_2_alterations(self):
        self.ps.set_machine("example_machine")
        self.ps.generate_custom_reflector_options(reflectors='a', alterations=2)
        self.assertEqual(82680, len(self.ps._possible_settings['reflectors']))
        self.assertEqual({'letters': 'JEGZBLCXVAWFYRQUONTSPIKHMD'}, self.ps._possible_settings['reflectors'][20])
        self.assertEqual({'letters': 'JEZMBLYXVAWFDRQUONTSPIKHGC'}, self.ps._possible_settings['reflectors'][0])

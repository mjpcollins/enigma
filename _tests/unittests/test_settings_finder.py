from unittest import TestCase
from utils import PossibleSettings, SettingsFinder


class Test_PossibleSettings(TestCase):

    def setUp(self):
        self.code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
        self.ps = PossibleSettings()
        self.ps.generate_entry_wheel_options()
        self.ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
        self.ps.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
        self.ps.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
        self.ps.generate_reflector_options()
        self.ps.generate_switchboard_options(['KI', 'XN', 'FL'])

        self.sf = SettingsFinder(code=self.code,
                                 cribs=['SECRETS'],
                                 possible_settings=self.ps,
                                 starting_position="MJM")
        self.expected_clues = {'SECRETS': [{'code': 'DMEXBMK', 'position': 0}, {'code': 'EXBMKYC', 'position': 2}, {'code': 'XBMKYCV', 'position': 3}, {'code': 'BMKYCVP', 'position': 4}, {'code': 'MKYCVPN', 'position': 5}, {'code': 'YCVPNQB', 'position': 7}, {'code': 'CVPNQBE', 'position': 8}, {'code': 'VPNQBED', 'position': 9},
                                           {'code': 'NQBEDHX', 'position': 11}, {'code': 'QBEDHXV', 'position': 12}, {'code': 'EDHXVPZ', 'position': 14}, {'code': 'DHXVPZG', 'position': 15}, {'code': 'HXVPZGK', 'position': 16}, {'code': 'XVPZGKM', 'position': 17}, {'code': 'VPZGKMT', 'position': 18}, {'code': 'ZGKMTFF', 'position': 20},
                                           {'code': 'GKMTFFB', 'position': 21}, {'code': 'KMTFFBJ', 'position': 22}, {'code': 'MTFFBJR', 'position': 23}, {'code': 'TFFBJRP', 'position': 24}, {'code': 'FFBJRPJ', 'position': 25}, {'code': 'JRPJTLH', 'position': 28}, {'code': 'RPJTLHL', 'position': 29}, {'code': 'PJTLHLC', 'position': 30},
                                           {'code': 'JTLHLCH', 'position': 31}, {'code': 'TLHLCHO', 'position': 32}, {'code': 'LHLCHOT', 'position': 33}, {'code': 'LCHOTKO', 'position': 35}, {'code': 'CHOTKOY', 'position': 36}, {'code': 'HOTKOYX', 'position': 37}, {'code': 'OTKOYXG', 'position': 38}, {'code': 'TKOYXGG', 'position': 39},
                                           {'code': 'KOYXGGH', 'position': 40}]}

    def test_init(self):
        self.assertEqual(self.code, self.sf._code)
        self.assertEqual(['SECRETS'], self.sf._cribs)
        self.assertEqual(self.ps._possible_settings, self.sf._possible_settings)
        self.assertEqual("DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ", self.sf.cf._code)
        self.assertEqual(self.expected_clues, self.sf._clues)
        self.assertEqual("MJM", self.sf._starting_position)

    def test_find_clues(self):
        self.sf._clues = {}
        self.assertEqual({}, self.sf._clues)
        self.sf._find_clues()
        self.assertEqual(self.expected_clues, self.sf._clues)

    def test_create_rotor_slot_generator(self):
        rotor_slot = self.sf._possible_settings['rotor_1'].copy()
        rotor_slot['start_positions'] = "ABC"
        rotor_slot_generator = self.sf._create_rotor_slot_generator(rotor_slot)
        self.assertEqual("<class 'generator'>", str(type(rotor_slot_generator)))
        self.assertListEqual([{'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'A'},
                              {'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'B'},
                              {'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'C'}],
                             list(rotor_slot_generator))

    def test_create_rotor_settings_generator_object(self):
        self.sf._possible_settings['rotor_1']['start_positions'] = "A"
        self.sf._possible_settings['rotor_2']['start_positions'] = "A"
        self.sf._possible_settings['rotor_3']['start_positions'] = "A"
        self.assertEqual("<class 'itertools.product'>", str(type(self.sf._create_rotor_settings_generator_object())))
        self.assertListEqual([({'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'A'}, {'letters': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'turnover': '', 'position': 2, 'ring_setting': 2, 'start_position': 'A'}, {'letters': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'turnover': 'Z', 'position': 3, 'ring_setting': 14, 'start_position': 'A'})],
                             list(self.sf._create_rotor_settings_generator_object()))

    def test_create_settings_generator_object(self):
        self.sf._possible_settings['rotor_1']['start_positions'] = "A"
        self.sf._possible_settings['rotor_2']['start_positions'] = "A"
        self.sf._possible_settings['rotor_3']['start_positions'] = "A"
        self.assertEqual("<class 'generator'>", str(type(self.sf._create_settings_generator_object())))

    def test_find_settings(self):
        ps = PossibleSettings()
        ps.generate_entry_wheel_options()
        ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
        ps.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
        ps.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
        ps.generate_reflector_options('c')
        ps.generate_switchboard_options(['KI', 'XN', 'FL'])
        sf = SettingsFinder(code=self.code,
                            cribs=['SECRETS'],
                            possible_settings=ps,
                            starting_position="MJM")
        s = sf.find_settings()
        self.assertEqual({'letters': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'},
                         s.get_reflector_data())
        self.assertEqual([{'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'start_position': 'M', 'turnover': '', 'position': 1, 'ring_setting': 3},
                          {'letters': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'start_position': 'K', 'turnover': '', 'position': 2, 'ring_setting': 1},
                          {'letters': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'start_position': 'W', 'turnover': 'Z', 'position': 3, 'ring_setting': 13}],
                         s.get_rotors_data())

    def test_estimate_rotor_positions(self):
        self.sf._starting_position = "AAA"
        self.assertEqual(["AB", "AB", "B"], self.sf._estimate_rotor_positions(1))
        self.assertEqual(['AB', 'ABC', 'P'], self.sf._estimate_rotor_positions(15))
        self.sf._starting_position = "ZZZ"
        self.assertEqual(['AZ', 'ABZ', 'O'], self.sf._estimate_rotor_positions(15))

from unittest import TestCase
from utils import PossibleSettings, EnigmaCracker, Enigma, Data, Settings


class Test_EnigmaCracker(TestCase):

    def setUp(self):
        self.code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
        self.ps = PossibleSettings()
        self.ps.generate_entry_wheel_options()
        self.ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
        self.ps.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
        self.ps.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
        self.ps.generate_reflector_options()
        self.ps.generate_switchboard_options(['KI', 'XN', 'FL'])

        self.cracker = EnigmaCracker(possible_settings=self.ps,
                                     starting_position="MJM")
        self.expected_clues = {'SECRETS': [{'code': 'DMEXBMK', 'position': 0}, {'code': 'EXBMKYC', 'position': 2}, {'code': 'XBMKYCV', 'position': 3}, {'code': 'BMKYCVP', 'position': 4}, {'code': 'MKYCVPN', 'position': 5}, {'code': 'YCVPNQB', 'position': 7}, {'code': 'CVPNQBE', 'position': 8}, {'code': 'VPNQBED', 'position': 9},
                                           {'code': 'NQBEDHX', 'position': 11}, {'code': 'QBEDHXV', 'position': 12}, {'code': 'EDHXVPZ', 'position': 14}, {'code': 'DHXVPZG', 'position': 15}, {'code': 'HXVPZGK', 'position': 16}, {'code': 'XVPZGKM', 'position': 17}, {'code': 'VPZGKMT', 'position': 18}, {'code': 'ZGKMTFF', 'position': 20},
                                           {'code': 'GKMTFFB', 'position': 21}, {'code': 'KMTFFBJ', 'position': 22}, {'code': 'MTFFBJR', 'position': 23}, {'code': 'TFFBJRP', 'position': 24}, {'code': 'FFBJRPJ', 'position': 25}, {'code': 'JRPJTLH', 'position': 28}, {'code': 'RPJTLHL', 'position': 29}, {'code': 'PJTLHLC', 'position': 30},
                                           {'code': 'JTLHLCH', 'position': 31}, {'code': 'TLHLCHO', 'position': 32}, {'code': 'LHLCHOT', 'position': 33}, {'code': 'LCHOTKO', 'position': 35}, {'code': 'CHOTKOY', 'position': 36}, {'code': 'HOTKOYX', 'position': 37}, {'code': 'OTKOYXG', 'position': 38}, {'code': 'TKOYXGG', 'position': 39},
                                           {'code': 'KOYXGGH', 'position': 40}]}

    def test_init(self):
        self.assertEqual("", self.cracker._code)
        self.assertEqual([], self.cracker._cribs)
        self.assertEqual(self.ps._possible_settings, self.cracker._possible_settings)
        self.assertEqual({}, self.cracker._clues)
        self.assertEqual("MJM", self.cracker._starting_position)

    def test_find_clues(self):
        self.assertEqual({}, self.cracker._clues)
        self.cracker._code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
        self.cracker._cribs = ['SECRETS']
        self.cracker._find_clues()
        self.assertEqual(self.expected_clues, self.cracker._clues)

    def test_create_rotor_slot_generator(self):
        rotor_slot = self.cracker._possible_settings['rotor_1'].copy()
        rotor_slot['start_positions'] = "ABC"
        rotor_slot_generator = self.cracker._create_rotor_slot_generator(rotor_slot)
        self.assertEqual("<class 'generator'>", str(type(rotor_slot_generator)))
        self.assertListEqual([{'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'A'},
                              {'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'B'},
                              {'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'C'}],
                             list(rotor_slot_generator))

    def test_create_rotor_settings_generator_object(self):
        self.cracker._possible_settings['rotor_1']['start_positions'] = "A"
        self.cracker._possible_settings['rotor_2']['start_positions'] = "A"
        self.cracker._possible_settings['rotor_3']['start_positions'] = "A"
        self.assertEqual("<class 'generator'>", str(type(self.cracker._create_rotor_settings_generator_object())))
        self.assertListEqual([({'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'A'}, {'letters': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'turnover': '', 'position': 2, 'ring_setting': 2, 'start_position': 'A'}, {'letters': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'turnover': 'Z', 'position': 3, 'ring_setting': 14, 'start_position': 'A'})],
                             list(self.cracker._create_rotor_settings_generator_object()))

    def test_create_settings_generator_object(self):
        self.cracker._possible_settings['rotor_1']['start_positions'] = "A"
        self.cracker._possible_settings['rotor_2']['start_positions'] = "A"
        self.cracker._possible_settings['rotor_3']['start_positions'] = "A"
        self.assertEqual("<class 'generator'>", str(type(self.cracker._create_settings_generator_object())))

    def test_find_settings(self):
        ps = PossibleSettings()
        ps.generate_entry_wheel_options()
        ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
        ps.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
        ps.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
        ps.generate_reflector_options('c')
        ps.generate_switchboard_options(['KI', 'XN', 'FL'])
        cracker = EnigmaCracker(possible_settings=ps,
                                starting_position="MJM")
        cracker._code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
        cracker._cribs = ['SECRETS']
        cracker._find_clues()
        settings = cracker._find_settings()
        s = settings['settings']
        self.assertEqual({'code': 'CHOTKOY', 'position': 36}, settings['crib'])
        self.assertEqual({'letters': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'},
                         s.get_reflector_data())
        self.assertEqual([{'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'start_position': 'M', 'turnover': '', 'position': 1, 'ring_setting': 3},
                          {'letters': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'start_position': 'K', 'turnover': '', 'position': 2, 'ring_setting': 1},
                          {'letters': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'start_position': 'W', 'turnover': 'Z', 'position': 3, 'ring_setting': 13}],
                         s.get_rotors_data())

    def test_estimate_rotor_positions(self):
        self.cracker._starting_position = "AAA"
        self.assertEqual(["AB", "AB", "B"], self.cracker._estimate_rotor_positions(1))
        self.assertEqual(['AB', 'ABC', 'P'], self.cracker._estimate_rotor_positions(15))
        self.cracker._starting_position = "ZZZ"
        self.assertEqual(['AZ', 'ABZ', 'O'], self.cracker._estimate_rotor_positions(15))

    def test_crack_code(self):
        ps = PossibleSettings()
        ps.generate_entry_wheel_options()
        ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
        ps.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
        ps.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
        ps.generate_reflector_options('c')
        ps.generate_switchboard_options(['KI', 'XN', 'FL'])
        cracker = EnigmaCracker(possible_settings=ps,
                                starting_position="MJM")
        answer = cracker.crack_code(code="DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ",
                                    cribs=['SECRETS'])
        self.assertEqual("NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING",
                         answer['cracked_code'])

    def test_match(self):
        settings = Settings()
        data = Data()
        data.set_machine("example_machine")
        ii = data.get_rotor("ii")
        iv = data.get_rotor("iv")
        beta = data.get_rotor("beta")
        gamma = data.get_rotor("gamma")
        ii.update({"start_position": "V", "ring_setting": 4, "position": 1})
        iv.update({"start_position": "E", "ring_setting": 24, "position": 2})
        beta.update({"start_position": "Q", "ring_setting": 17, "position": 3})
        gamma.update({"start_position": "J", "ring_setting": 7, "position": 4})
        settings.add_rotors([ii, iv, beta, gamma])
        settings.set_reflector(**data.get_reflector("b"))
        settings.set_switchboard_pairs(["AT", "LU", "NR", "IG"])
        enigma = Enigma(settings=settings)

        self.assertEqual(True, self.cracker._match(code="BHCHR", clue="ACOMP", enigma_machine=enigma))

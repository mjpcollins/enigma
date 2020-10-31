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

    def test_init(self):
        self.assertEqual("", self.cracker._code)
        self.assertEqual([], self.cracker._cribs)
        self.assertEqual(self.ps._possible_settings, self.cracker._possible_settings)
        self.assertEqual("MJM", self.cracker._starting_position)

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
                         answer[0]['cracked_code'])


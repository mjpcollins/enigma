import io
from unittest import TestCase, mock
from utils import PossibleSettings, EnigmaCracker


class Test_EnigmaCracker(TestCase):

    def setUp(self):
        self.code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
        self.ps_B_G_V_C = PossibleSettings()
        self.ps_B_G_V_C.generate_entry_wheel_options()
        self.ps_B_G_V_C.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
        self.ps_B_G_V_C.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
        self.ps_B_G_V_C.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
        self.ps_B_G_V_C.generate_reflector_options('c')
        self.ps_B_G_V_C.generate_switchboard_options(['KI', 'XN', 'FL'])
        self.cracker_c = EnigmaCracker(possible_settings=self.ps_B_G_V_C,
                                       starting_position="MJM")

        self.ps_B_G_V_all = PossibleSettings()
        self.ps_B_G_V_all.generate_entry_wheel_options()
        self.ps_B_G_V_all.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
        self.ps_B_G_V_all.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
        self.ps_B_G_V_all.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
        self.ps_B_G_V_all.generate_reflector_options()
        self.ps_B_G_V_all.generate_switchboard_options(['KI', 'XN', 'FL'])

        self.cracker_all = EnigmaCracker(possible_settings=self.ps_B_G_V_all,
                                         starting_position="MJM")

    def test_init(self):
        self.assertEqual("", self.cracker_all._code)
        self.assertEqual([], self.cracker_all._cribs)
        self.assertEqual(self.ps_B_G_V_all._possible_settings, self.cracker_all._possible_settings)
        self.assertEqual("M", self.cracker_all._possible_settings['rotor_1']['start_positions'])
        self.assertEqual("J", self.cracker_all._possible_settings['rotor_2']['start_positions'])
        self.assertEqual("M", self.cracker_all._possible_settings['rotor_3']['start_positions'])

    def test_create_rotor_slot_generator(self):
        rotor_slot = self.cracker_all._possible_settings['rotor_1'].copy()
        rotor_slot['start_positions'] = "ABC"
        rotor_slot_generator = self.cracker_all._rotor_slot_generator(rotor_slot)
        self.assertEqual("<class 'generator'>", str(type(rotor_slot_generator)))
        self.assertListEqual([{'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'A'},
                              {'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'B'},
                              {'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'C'}],
                             list(rotor_slot_generator))

    def test_create_rotor_settings_generator_object(self):
        self.cracker_all._possible_settings['rotor_1']['start_positions'] = "A"
        self.cracker_all._possible_settings['rotor_2']['start_positions'] = "A"
        self.cracker_all._possible_settings['rotor_3']['start_positions'] = "A"
        self.assertEqual("<class 'generator'>", str(type(self.cracker_all._create_rotor_settings_generator_object())))
        self.assertListEqual([({'letters': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'turnover': '', 'position': 1, 'ring_setting': 4, 'start_position': 'A'}, {'letters': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'turnover': '', 'position': 2, 'ring_setting': 2, 'start_position': 'A'}, {'letters': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'turnover': 'Z', 'position': 3, 'ring_setting': 14, 'start_position': 'A'})],
                             list(self.cracker_all._create_rotor_settings_generator_object()))

    def test_create_settings_generator_object(self):
        self.cracker_all._possible_settings['rotor_1']['start_positions'] = "A"
        self.cracker_all._possible_settings['rotor_2']['start_positions'] = "A"
        self.cracker_all._possible_settings['rotor_3']['start_positions'] = "A"
        self.assertEqual("<class 'generator'>", str(type(self.cracker_all._settings_generator())))

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_crack_code(self, mock_stdout):
        answer = self.cracker_c.crack_code(code="DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ",
                                    cribs=['SECRETS'])
        self.assertEqual("NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING",
                         answer[0]['cracked_code'])
        self.assertEqual("{'letters': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'} SECRETS NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING\n",
                         mock_stdout.getvalue())

    @mock.patch('sys.stdout', new_callable=io.StringIO)  # Silencing the print statement
    def test_crack_code_mp(self, mock_stdout):
        answer = self.cracker_c.crack_code(code="DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ",
                                           cribs=['SECRETS'],
                                           multiprocess=True)
        self.assertEqual("NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING",
                         answer[0]['cracked_code'])

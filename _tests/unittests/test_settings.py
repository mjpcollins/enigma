from unittest import TestCase
from utils import Settings


class Test_Settings(TestCase):

    def setUp(self):
        self.settings = Settings()

    def test_init(self):
        self.assertDictEqual({}, self.settings._reflector_data)
        self.assertListEqual([], self.settings._rotors_data)
        self.assertDictEqual({"letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}, self.settings._entry_wheel_data)
        self.assertDictEqual({"pairs": []}, self.settings._switchboard_data)

    def test_set_reflector(self):
        self.assertDictEqual({}, self.settings._reflector_data)
        self.settings.set_reflector("CDEMUXPNVZBHYFQWKIATGLORSJ")
        self.assertDictEqual({"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ"}, self.settings._reflector_data)

    def test_add_wheel(self):
        self.assertListEqual([], self.settings._rotors_data)
        self.settings.add_rotor(letters="CDEMUXPNVZBHYFQWKIATGLORSJ",
                                start_position="G",
                                turnover="AM",
                                position=0)
        self.assertListEqual([{"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ", "start_position": "G",
                               "turnover": "AM", "position": 0}],
                             self.settings._rotors_data)
        self.settings.add_rotor(letters="YFQWKIATGLORSJCDEMUXPNVZBH",
                                start_position="F",
                                turnover="KG",
                                position=1)
        self.assertListEqual([{"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ", "start_position": "G",
                               "turnover": "AM", "position": 0},
                              {"letters": "YFQWKIATGLORSJCDEMUXPNVZBH", "start_position": "F",
                               "turnover": "KG", "position": 1}],
                             self.settings._rotors_data)

    def test_set_entry_wheel(self):
        self.assertDictEqual({"letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}, self.settings._entry_wheel_data)
        self.settings.set_entry_wheel("YFQWKIATGLORSJCDEMUXPNVZBH")
        self.assertDictEqual({"letters": "YFQWKIATGLORSJCDEMUXPNVZBH"}, self.settings._entry_wheel_data)

    def test_set_switchboard_pairs(self):
        self.assertDictEqual({"pairs": []}, self.settings._switchboard_data)
        self.settings.set_switchboard_pairs(["NI", "KF", "PY", "VB", "CG", "WR", "TQ", "OS", "LH", "DZ"])
        self.assertDictEqual({"pairs": ["NI", "KF", "PY", "VB", "CG", "WR", "TQ", "OS", "LH", "DZ"]},
                             self.settings._switchboard_data)

    def test_remove_wheel(self):
        self.settings._rotors_data = [{"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ", "start_position": "G", "turnover": "AM"},
                                      {"letters": "YFQWKIATGLORSJCDEMUXPNVZBH", "start_position": "F", "turnover": "KG"}]
        self.settings.remove_rotor()
        self.assertListEqual([{"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ", "start_position": "G", "turnover": "AM"}],
                             self.settings._rotors_data)

    def test_remove_all_wheels(self):
        self.settings._rotors_data = [{"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ", "start_position": "G", "turnover": "AM"},
                                      {"letters": "YFQWKIATGLORSJCDEMUXPNVZBH", "start_position": "F", "turnover": "KG"}]
        self.settings.remove_all_rotors()
        self.assertListEqual([], self.settings._rotors_data)

    def test_get_wheels_data(self):
        self.settings._rotors_data = [{"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ", "start_position": "G", "turnover": "AM", "position": 0},
                                      {"letters": "YFQWKIATGLORSJCDEMUXPNVZBH", "start_position": "F", "turnover": "KG", "position": 1}]
        self.assertListEqual([{"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ", "start_position": "G", "turnover": "AM", "position": 0},
                              {"letters": "YFQWKIATGLORSJCDEMUXPNVZBH", "start_position": "F", "turnover": "KG", "position": 1}],
                             self.settings.get_rotors_data())

    def test_get_reflector_data(self):
        self.assertDictEqual({}, self.settings.get_reflector_data())
        self.settings._reflector_data = {"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ"}
        self.assertDictEqual({"letters": "CDEMUXPNVZBHYFQWKIATGLORSJ"}, self.settings.get_reflector_data())

    def test_get_entry_wheel_data(self):
        self.assertDictEqual({"letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}, self.settings.get_entry_wheel_data())
        self.settings._entry_wheel_data = {"letters": "YFQWKIATGLORSJCDEMUXPNVZBH"}
        self.assertDictEqual({"letters": "YFQWKIATGLORSJCDEMUXPNVZBH"}, self.settings.get_entry_wheel_data())

    def test_get_switchboard_data(self):
        self.assertDictEqual({"pairs": []}, self.settings.get_switchboard_data())
        self.settings._switchboard_data = {"pairs": ["NI", "KF", "PY", "VB", "CG", "WR", "TQ", "OS", "LH", "DZ"]}
        self.assertDictEqual({"pairs": ["NI", "KF", "PY", "VB", "CG", "WR", "TQ", "OS", "LH", "DZ"]},
                             self.settings.get_switchboard_data())

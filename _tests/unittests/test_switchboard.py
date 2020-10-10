from unittest import TestCase
from utils import Switchboard


class Test_Switchboard(TestCase):

    def setUp(self):
        self.swapper = Switchboard(pairs=["NI", "KF", "PY", "VB", "CG",
                                          "WR", "TQ", "OS", "LH", "DZ"])
        # 2020-10-10 MC: Might be worth adding another pairs_dict for the other test cases.
        self.expected_pairs_dict = {"N": "I", "K": "F", "P": "Y", "V": "B", "C": "G",
                                    "W": "R", "T": "Q", "O": "S", "L": "H", "D": "Z",
                                    "I": "N", "F": "K", "Y": "P", "B": "V", "G": "C",
                                    "R": "W", "Q": "T", "S": "O", "H": "L", "Z": "D"}
        self.assertDictEqual(self.expected_pairs_dict, self.swapper._pairs_dict)

    def test_init(self):
        self.assertListEqual(["NI", "KF", "PY", "VB", "CG",  "WR", "TQ", "OS", "LH", "DZ"],
                             self.swapper._pairs)

    def test_flow_through(self):
        self.swapper._pairs_dict = self.expected_pairs_dict
        self.assertEqual("A", self.swapper.flow_through("A"))
        self.assertEqual("F", self.swapper.flow_through("K"))
        self.assertEqual("K", self.swapper.flow_through("F"))

    def test_handle_pairs(self):
        self.swapper._pairs_dict = {}
        self.assertDictEqual({}, self.swapper._pairs_dict)
        self.assertDictEqual(self.expected_pairs_dict, self.swapper._handle_pairs())
        self.assertDictEqual(self.expected_pairs_dict, self.swapper._pairs_dict)

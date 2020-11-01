from unittest import TestCase
from utils import Plugboard, PlugLead


class Test_Plugboard(TestCase):

    def setUp(self):
        self.swapper = Plugboard(pairs=["NI", "KF", "PY", "VB", "CG",
                                          "WR", "TQ", "OS", "LH", "DZ"])
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
        self.assertEqual("A", self.swapper.encode("A"))
        self.assertEqual("F", self.swapper.encode("K"))
        self.assertEqual("K", self.swapper.encode("F"))

    def test_handle_pairs(self):
        self.swapper._pairs_dict = {}
        self.assertDictEqual({}, self.swapper._pairs_dict)
        self.assertDictEqual(self.expected_pairs_dict, self.swapper._handle_pairs())
        self.assertDictEqual(self.expected_pairs_dict, self.swapper._pairs_dict)

    def test_required_for_coursework_pluglead(self):
        lead = PlugLead("AG")
        self.assertEqual("G", lead.encode("A"))
        self.assertEqual("D", lead.encode("D"))

        lead = PlugLead("DA")
        self.assertEqual("D", lead.encode("A"))
        self.assertEqual("A", lead.encode("D"))

    def test_required_for_coursework_plugboard(self):
        plugboard = Plugboard()

        plugboard.add(PlugLead("SZ"))
        plugboard.add(PlugLead("GT"))
        plugboard.add(PlugLead("DV"))
        plugboard.add(PlugLead("KU"))

        self.assertEqual("U", plugboard.encode("K"))
        self.assertEqual("A", plugboard.encode("A"))

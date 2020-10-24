from unittest import TestCase
from utils import CribFinder


class Test_CribFinder(TestCase):

    def setUp(self):
        self.cf = CribFinder(code="JXATQBGGYWCRYBGDTAA")

    def test_init(self):
        self.assertEqual("JXATQBGGYWCRYBGDTAA", self.cf._code)

    def test_find_crib_in_code(self):
        self.assertListEqual(["ATQBGGYWCRYBG", "BGGYWCRYBGDTA"],
                             self.cf.find_crib_in_code(crib="WETTERBERICHT"))

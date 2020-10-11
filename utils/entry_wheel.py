from string import ascii_uppercase
from utils.swapper import Swapper


class EntryWheel(Swapper):

    def __init__(self, letters=ascii_uppercase):
        super(EntryWheel, self).__init__(letters=letters)

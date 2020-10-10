from utils.swapper import Swapper


class EntryWheel(Swapper):

    def __init__(self, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        super(EntryWheel, self).__init__(letters=letters)

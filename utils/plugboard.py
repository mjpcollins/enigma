
class Plugboard:

    def __init__(self, pairs=None):
        if not pairs:
            pairs = []
        self._pairs = pairs
        self._pairs_dict = {}
        self._handle_pairs()

    def encode(self, letter):
        return self._pairs_dict.get(letter, letter)

    def _handle_pairs(self):
        for pair in self._pairs:
            self._pairs_dict.update({pair[0]: pair[1],
                                     pair[1]: pair[0]})
        return self._pairs_dict

    def add(self, pluglead):
        """
        Required for passing the coursework tests, but not actually used anywhere in the enigma machine code.
        """
        self._pairs_dict.update(pluglead.encoding)


class PlugLead:
    """
    Required for passing the coursework tests, but not actually used anywhere in the enigma machine code.
    """

    def __init__(self, pair):
        self.encoding = {pair[0]: pair[1],
                         pair[1]: pair[0]}

    def encode(self, letter):
        return self.encoding.get(letter, letter)


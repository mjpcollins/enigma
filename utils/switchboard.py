
class Switchboard:

    def __init__(self, pairs):
        self._pairs = pairs
        self._pairs_dict = {}
        self._handle_pairs()

    def flow_through(self, letter):
        return self._pairs_dict.get(letter, letter)

    def _handle_pairs(self):
        for pair in self._pairs:
            self._pairs_dict.update({pair[0]: pair[1],
                                     pair[1]: pair[0]})
        return self._pairs_dict

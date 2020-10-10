

class Swapper:

    # Simulation is a bit broken at the moment. I need to offset the turning of the rotors
    # Assumed design of rotors was incorrect.

    def __init__(self, letters):
        self._letters = str(letters)
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._offset = 0

    def forward_flow(self, letter):
        idx = self._alphabet.index(letter) + self._offset
        return self._letters[idx]

    def reverse_flow(self, letter):
        idx = self._letters.index(letter)
        return self._alphabet[idx]



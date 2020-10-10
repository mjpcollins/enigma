

class Swapper:

    def __init__(self, letters):
        self._letters = str(letters)
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def forward_flow(self, letter):
        idx = self._alphabet.index(letter)
        return self._letters[idx]

    def reverse_flow(self, letter):
        idx = self._letters.index(letter)
        return self._alphabet[idx]



from utils.scrambler import Scrambler
from utils.switchboard import Switchboard


class Enigma:

    def __init__(self, settings):
        self.scrambler = Scrambler(settings=settings)
        self.switchboard = Switchboard(**settings.get_switchboard_data())

    def press_key(self, letter):
        current_letter = self.switchboard.flow_through(letter=letter)
        current_letter = self.scrambler.scramble_letter(letter=current_letter)
        current_letter = self.switchboard.flow_through(letter=current_letter)
        return current_letter



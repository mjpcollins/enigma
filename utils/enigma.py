from utils.scrambler import Scrambler
from utils.switchboard import Switchboard


class Enigma:

    def __init__(self, settings, error_checks=True):
        self.scrambler = Scrambler(settings=settings)
        self.switchboard = Switchboard(**settings.get_switchboard_data())
        self._error_checks = error_checks

    def parse(self, message):
        if self._error_checks:
            self._run_error_parse_checks(message)
        return "".join([self.press_key(letter) for letter in message])

    def press_key(self, letter):
        if self._error_checks:
            self._run_error_key_checks(letter)
        current_letter = self.switchboard.flow_through(letter=letter)
        current_letter = self.scrambler.scramble_letter(letter=current_letter)
        current_letter = self.switchboard.flow_through(letter=current_letter)
        return current_letter

    def _run_error_parse_checks(self, letter):
        pass

    def _run_error_key_checks(self, letter):
        pass

from string import ascii_uppercase
from utils.scrambler import Scrambler
from utils.switchboard import Switchboard


class Enigma:

    def __init__(self, settings, error_checks=True, correct_case=True):
        self.scrambler = Scrambler(settings=settings)
        self.switchboard = Switchboard(**settings.get_switchboard_data())
        self._error_checks = error_checks
        self._correct_case = correct_case

    def parse(self, message):
        if self._error_checks:
            self._run_error_parse_checks(message)
        return "".join([self.press_key(letter) for letter in message])

    def press_key(self, letter):
        if self._error_checks:
            self._run_error_key_checks(letter)
        if self._correct_case:
            letter = letter.upper()
        current_letter = self.switchboard.flow_through(letter=letter)
        current_letter = self.scrambler.scramble_letter(letter=current_letter)
        current_letter = self.switchboard.flow_through(letter=current_letter)
        return current_letter

    def _run_error_parse_checks(self, message):
        try:
            assert type(message) == str
            for letter in message:
                self._run_error_key_checks(letter)
        except AssertionError:
            raise TypeError(f"{type(message)} is not a valid message type. Please try a string.")

    def _run_error_key_checks(self, letter):
        try:
            assert type(letter) == str
            if not self._correct_case:
                try:
                    assert letter in ascii_uppercase
                except AssertionError:
                    raise SyntaxError("Please ensure input letter is an alphabet character, no spaces")
            else:
                try:
                    assert letter.upper() in ascii_uppercase
                except AssertionError:
                    raise SyntaxError("Please ensure input letter is an all upper case alphabet character, no spaces")
        except AssertionError:
            raise TypeError(f"{type(letter)} is not a valid letter type. Please try a string.")


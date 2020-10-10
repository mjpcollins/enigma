from utils.swapper import Swapper


class Wheel(Swapper):

    def __init__(self, wiring_letters, starting_position, turnover):
        super(Wheel, self).__init__(letters=wiring_letters)
        self._starting_pos = starting_position
        self._turnover = turnover
        self._current_pos = self._letters[0]
        self.set_current_position(self._starting_pos)

    def get_current_position(self):
        return self._current_pos

    def set_current_position(self, letter):
        while self._current_pos != letter:
            self.rotate_once()

    def rotate_once(self):
        cause_turnover = self.get_current_position() in self._turnover
        self._letters = self._letters[1:] + self._letters[0]
        self._current_pos = self._letters[0]
        return cause_turnover


from utils.swapper import Swapper


class Wheel(Swapper):

    def __init__(self, letters, start_position, turnover, position):
        super(Wheel, self).__init__(letters=letters)
        self._starting_pos = start_position
        self._turnover = turnover
        self._current_pos = self._letters[0]
        self.set_current_position(self._starting_pos)
        self._position = position

    def __gt__(self, other_wheel):
        return self.get_position_in_machine() > other_wheel.get_position_in_machine()

    def get_position_in_machine(self):
        return self._position

    def get_current_position(self):
        return self._current_pos

    def set_current_position(self, letter):
        while self._current_pos != letter:
            self.rotate_once()

    def will_cause_turnover(self):
        return self.get_current_position() in self._turnover

    def rotate_once(self):
        cause_turnover = self.will_cause_turnover()
        self._letters = self._letters[1:] + self._letters[0]
        self._current_pos = self._letters[0]
        return cause_turnover


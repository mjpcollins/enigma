from utils.swapper import Swapper
from utils.misc import number_to_alpha


class Rotor(Swapper):

    def __init__(self, letters, start_position, turnover,
                 position, ring_setting=0):
        super(Rotor, self).__init__(letters=letters)
        self._starting_pos = start_position
        self._turnover = turnover
        self.set_current_position(self._starting_pos)
        self._position = position
        self.set_ring_setting(ring_setting)

    def __gt__(self, other_rotor):
        return other_rotor.position_in_machine() > self.position_in_machine()

    def position_in_machine(self):
        return self._position

    def get_current_position(self):
        return number_to_alpha(self._offset)

    def set_current_position(self, letter):
        while self.get_current_position() != letter:
            self.rotate_once()

    def will_cause_turnover(self):
        return self.get_current_position() in self._turnover

    def previous_letter_caused_turnover(self):
        return number_to_alpha(self._offset - 1) in self._turnover

    def rotate_once(self):
        self.increase_offset()



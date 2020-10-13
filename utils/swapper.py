from utils.misc import alpha_to_number, number_to_alpha


class Swapper:

    # Simulation is a bit broken at the moment. I need to offset the turning of the rotors
    # Assumed design of rotors was incorrect.

    def __init__(self, letters):
        self._letters = str(letters)
        self._offset = 0
        self._ring_offset = 0

    def forward_flow(self, letter):
        input_letter = self._add_letter_offset(letter)
        mapped_letter = self._right_to_left(input_letter)
        offset_letter = self._minus_letter_offset(mapped_letter)
        return offset_letter

    def reverse_flow(self, letter):
        input_letter = self._add_letter_offset(letter)
        mapped_letter = self._left_to_right(input_letter)
        offset_letter = self._minus_letter_offset(mapped_letter)
        return offset_letter

    def increase_offset(self):
        self._offset = (self._offset + 1) % 26

    def decrease_offset(self):
        self._offset = (self._offset - 1) % 26

    def get_ring_setting(self):
        return self._ring_offset

    def set_ring_setting(self, position):
        self._ring_offset = position % 26

    def _add_offset(self, indx):
        return (indx + self._offset - self._ring_offset) % 26

    def _minus_offset(self, indx):
        return (indx - self._offset + self._ring_offset) % 26

    def _add_letter_offset(self, letter):
        return number_to_alpha(self._add_offset(alpha_to_number(letter)))

    def _minus_letter_offset(self, letter):
        return number_to_alpha(self._minus_offset(alpha_to_number(letter)))

    def _right_to_left(self, letter):
        return self._letters[alpha_to_number(letter)]

    def _left_to_right(self, letter):
        return number_to_alpha(self._letters.index(letter))




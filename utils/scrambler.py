from utils.rotor import Rotor
from utils.reflector import Reflector
from utils.entry_wheel import EntryWheel


class Scrambler:

    def __init__(self, settings):
        self._settings = settings
        self._reflector = Reflector(**self._settings.get_reflector_data())
        self._rotors = [Rotor(**data) for data in self._settings.get_rotors_data()]
        self._entry_wheel = EntryWheel(**self._settings.get_entry_wheel_data())

    def scramble_letter(self, letter):
        self.rotate_rotors()
        return self.flow_through(letter)

    def rotate_rotors(self):
        for rotor in self._find_rotors_permitted_to_rotate():
            rotor.rotate_once()

    def _find_rotors_permitted_to_rotate(self):
        fast_rotor = [self._find_fast_rotor()]
        turnovers = self._find_rotors_to_turnover()
        rotors_to_turn = list(set(fast_rotor + turnovers))
        rotors_to_turn.sort()
        return rotors_to_turn

    def _find_fast_rotor(self):
        return self._rotors[0]

    def _find_rotors_to_turnover(self):
        turnover_rotors = []
        for idx in range(len(self._rotors) - 1):
            if self._rotors[idx].will_cause_turnover():
                turnover_rotors.append(self._rotors[idx])
                turnover_rotors.append(self._rotors[idx + 1])
            else:
                break
        return turnover_rotors

    def flow_through(self, letter):
        current_letter = self._entry_wheel_in(letter)
        current_letter = self._flow_forward_through_rotors(current_letter)
        current_letter = self._reflect(current_letter)
        current_letter = self._flow_back_through_rotors(current_letter)
        current_letter = self._entry_wheel_out(current_letter)
        return current_letter

    def _entry_wheel_in(self, letter):
        return self._entry_wheel.forward_flow(letter=letter)

    def _entry_wheel_out(self, letter):
        return self._entry_wheel.reverse_flow(letter=letter)

    def _reflect(self, letter):
        return self._reflector.forward_flow(letter=letter)

    def _flow_forward_through_rotors(self, letter):
        for rotor in self._rotors:
            letter = rotor.forward_flow(letter=letter)
        return letter

    def _flow_back_through_rotors(self, letter):
        for rotor in self._rotors[::-1]:
            letter = rotor.reverse_flow(letter=letter)
        return letter

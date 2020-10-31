from utils.rotor import Rotor
from utils.reflector import Reflector
from utils.entry_wheel import EntryWheel


class Scrambler:

    def __init__(self, settings):
        self._settings = settings
        self._reflector = Reflector(**self._settings.get_reflector_data())
        self._rotors = [Rotor(**data) for data in self._settings.get_rotors_data()]
        self._entry_wheel = EntryWheel(**self._settings.get_entry_wheel_data())
        self._rotors.sort()

    def scramble_letter(self, letter):
        self.rotate_rotors()
        return self.flow_through(letter)

    def rotate_rotors(self):
        for rotor in self._find_rotors_permitted_to_rotate():
            rotor.rotate_once()

    def _find_rotors_permitted_to_rotate(self):
        rotors_to_turn = set([self._find_fast_rotor()] + self._find_rotors_to_turnover())
        self._remove_fourth_rotor(rotors_to_turn)
        return rotors_to_turn

    def _find_fast_rotor(self):
        return self._rotors[0]

    def _remove_fourth_rotor(self, rotors_set):
        # It's faster and more "proper" in python to try & catch the error than to use an if statement
        # https://stackoverflow.com/questions/7604636/better-to-try-something-and-catch-the-exception-or-test-if-its-possible-first
        try:
            rotors_set.remove(self._rotors[3])
        except KeyError:
            pass
        except IndexError:
            pass

    def _find_rotors_to_turnover(self):
        turnover_rotors = []
        for idx, this_rotor in enumerate(self._rotors[:-1]):
            previous_rotor = self._rotors[idx - 1]
            next_rotor = self._rotors[idx + 1]
            if this_rotor.will_cause_turnover():
                if (idx == 0) or previous_rotor.has_notches():
                    turnover_rotors.append(this_rotor)
                    turnover_rotors.append(next_rotor)
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

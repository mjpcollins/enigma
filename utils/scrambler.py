from utils.wheel import Wheel
from utils.reflector import Reflector
from utils.entry_wheel import EntryWheel


class Scrambler:

    def __init__(self, settings):
        self._settings = settings
        self._reflector = Reflector(**self._settings.get_reflector_data())
        self._wheels = [Wheel(**data) for data in self._settings.get_wheels_data()]
        self._entry_wheel = EntryWheel(**self._settings.get_entry_wheel_data())

    def scramble_letter(self, letter):
        self.rotate_wheels()
        return self.flow_through(letter)

    def rotate_wheels(self):
        for wheel in self._find_wheels_permitted_to_rotate():
            wheel.rotate_once()

    def _find_wheels_permitted_to_rotate(self):
        fast_wheel = [self._find_fast_wheel()]
        turnovers = self._find_wheels_to_turnover()
        wheels_to_turn = list(set(fast_wheel + turnovers))
        wheels_to_turn.sort()
        return wheels_to_turn

    def _find_fast_wheel(self):
        return self._wheels[0]

    def _find_wheels_to_turnover(self):
        turnover_wheels = []
        for idx in range(len(self._wheels) - 1):
            if self._wheels[idx].will_cause_turnover():
                turnover_wheels.append(self._wheels[idx])
                turnover_wheels.append(self._wheels[idx + 1])
            else:
                break
        return turnover_wheels

    def flow_through(self, letter):
        current_letter = self._entry_wheel_in(letter)
        current_letter = self._flow_forward_through_wheels(current_letter)
        current_letter = self._reflect(current_letter)
        current_letter = self._flow_back_through_wheels(current_letter)
        current_letter = self._entry_wheel_out(current_letter)
        return current_letter

    def _entry_wheel_in(self, letter):
        return self._entry_wheel.forward_flow(letter=letter)

    def _entry_wheel_out(self, letter):
        return self._entry_wheel.reverse_flow(letter=letter)

    def _reflect(self, letter):
        return self._reflector.forward_flow(letter=letter)

    def _flow_forward_through_wheels(self, letter):
        for wheel in self._wheels:
            letter = wheel.forward_flow(letter=letter)
        return letter

    def _flow_back_through_wheels(self, letter):
        for wheel in self._wheels[::-1]:
            letter = wheel.reverse_flow(letter=letter)
        return letter

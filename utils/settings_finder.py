import itertools
from utils.crib_finder import CribFinder
from utils.settings import Settings
from utils.enigma import Enigma
from utils.misc import shift_letter


class SettingsFinder:

    def __init__(self, code, cribs, possible_settings, starting_position=""):
        self._code = code
        self._cribs = cribs
        self._possible_settings = possible_settings.get_settings()
        self.cf = CribFinder(code=code)
        self._clues = {}
        self._find_clues()
        self._starting_position = starting_position

    def find_settings(self):
        for clue in self._clues:
            for encoded_clue in self._clues[clue]:
                offset = encoded_clue['position']
                code = encoded_clue['code']
                if self._starting_position:
                    possible_positions = self._estimate_rotor_positions(offset)
                    self._possible_settings['rotor_1']['start_positions'] = possible_positions[0]
                    self._possible_settings['rotor_2']['start_positions'] = possible_positions[1]
                    self._possible_settings['rotor_3']['start_positions'] = possible_positions[2]
                for settings in self._create_settings_generator_object():
                    engima = Enigma(settings=settings)
                    parsed = engima.parse(clue)
                    if code == parsed:
                        return settings
        return None

    def _estimate_rotor_positions(self, offset):
        rotor_1 = set(self._starting_position[0])
        rotor_2 = set(self._starting_position[1])
        most_possible_fast_turnovers = (offset // 12) + 2
        most_possible_medium_turnovers = (offset // (12 * 12)) + 2
        rotor_3 = set(shift_letter(self._starting_position[2], offset))
        for rotations2 in range(most_possible_fast_turnovers):
            rotor_2.add(shift_letter(self._starting_position[1], rotations2))
        for rotations1 in range(most_possible_medium_turnovers):
            rotor_1.add(shift_letter(self._starting_position[0], rotations1))
        positions = []
        for rotor in [rotor_1, rotor_2, rotor_3]:
            chars_list = list(rotor)
            chars_list.sort()
            positions.append("".join(chars_list))
        return positions

    def _find_clues(self):
        for crib in self._cribs:
            self._clues[crib] = self.cf.find_crib_in_code(crib=crib)

    def _create_settings_generator_object(self):
        for entry_wheel in self._possible_settings['entry_wheels']:
            for pairs in self._possible_settings['switchboards']:
                for rotors in self._create_rotor_settings_generator_object():
                    for reflector in self._possible_settings['reflectors']:
                        settings = Settings()
                        settings.set_entry_wheel(**entry_wheel)
                        settings.add_rotors(rotors)
                        settings.set_reflector(**reflector)
                        settings.set_switchboard_pairs(pairs)
                        yield settings

    def _create_rotor_settings_generator_object(self):
        rotor_settings = [self._possible_settings['rotor_1'],
                          self._possible_settings['rotor_2'],
                          self._possible_settings['rotor_3'],
                          self._possible_settings['rotor_4']]
        slots = [self._create_rotor_slot_generator(rotor_slot) for rotor_slot in rotor_settings if rotor_slot]
        return itertools.product(*slots)

    @staticmethod
    def _create_rotor_slot_generator(rotor_slot):
        for rotor_choice in rotor_slot['rotor_choices']:
            for ring_setting in rotor_slot['ring_settings']:
                for start_position in rotor_slot['start_positions']:
                    rotor_data = rotor_choice.copy()
                    rotor_data.update({'ring_setting': ring_setting,
                                       'start_position': start_position})
                    yield rotor_data


import itertools
from string import ascii_uppercase
from utils.crib_finder import CribFinder
from utils.settings import Settings
from utils.enigma import Enigma
from utils.misc import shift_letter


class EnigmaCracker:

    def __init__(self, possible_settings, starting_position=""):
        self._code = ""
        self._cribs = []
        self._possible_settings = possible_settings.get_settings()
        self._clues = {}
        self._starting_position = starting_position

    def crack_code(self, code, cribs):
        self._code = code
        self._cribs = cribs
        self._find_clues()
        data = self._find_settings()
        settings = data['settings']
        if not self._starting_position:
            self._starting_position = self._find_starting_position(data)
        for indx, position in enumerate(self._starting_position):
            settings.set_rotor_start_position(rotor_position=indx,
                                              start_position=position)
        enigma = Enigma(settings)
        cracked_code = enigma.parse(self._code)
        return {'settings': settings, 'cracked_code': cracked_code}

    def _find_settings(self):
        for clue in self._clues:
            for encoded_clue in self._clues[clue]:
                offset = encoded_clue['position']
                code = encoded_clue['code']
                if self._starting_position:
                    possible_positions = self._estimate_rotor_positions(offset)
                    self._possible_settings['rotor_1']['start_positions'] = possible_positions[0]
                    self._possible_settings['rotor_2']['start_positions'] = possible_positions[1]
                    self._possible_settings['rotor_3']['start_positions'] = possible_positions[2]
                for idx, settings in enumerate(self._create_settings_generator_object()):
                    print(encoded_clue, idx)
                    if self._match(code=code, clue=clue, enigma_machine=Enigma(settings=settings)):
                        return {'settings': settings, 'crib': encoded_clue, 'clue': clue}
        return None

    def _match(self, code, clue, enigma_machine):
        if len(clue) == 0:
            return True
        else:
            if enigma_machine.press_key(clue[0]) == code[0]:
                return self._match(code=code[1:], clue=clue[1:], enigma_machine=enigma_machine)
            return False

    def _find_starting_position(self, cracked_data):
        settings = cracked_data['settings']
        clue = cracked_data['clue']
        for rotor1_letter in ascii_uppercase:
            for rotor2_letter in ascii_uppercase:
                for rotor3_letter in ascii_uppercase:
                    settings.set_rotor_start_position(0, rotor1_letter)
                    settings.set_rotor_start_position(1, rotor2_letter)
                    settings.set_rotor_start_position(2, rotor3_letter)
                    enigma = Enigma(settings)
                    if clue in enigma.parse(self._code):
                        return rotor1_letter + rotor2_letter + rotor3_letter

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
            self._clues[crib] = CribFinder(code=self._code).find_crib_in_code(crib=crib)

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
        for rotors_combination in itertools.product(*slots):
            if self._distinct_rotors(rotors_combination):
                yield rotors_combination

    @staticmethod
    def _create_rotor_slot_generator(rotor_slot):
        for rotor_choice in rotor_slot['rotor_choices']:
            for ring_setting in rotor_slot['ring_settings']:
                for start_position in rotor_slot['start_positions']:
                    rotor_data = rotor_choice.copy()
                    rotor_data.update({'ring_setting': ring_setting,
                                       'start_position': start_position})
                    yield rotor_data

    @staticmethod
    def _distinct_rotors(rotor_combinations):
        r1_letters = rotor_combinations[0]['letters']
        r2_letters = rotor_combinations[1]['letters']
        r3_letters = rotor_combinations[2]['letters']
        letters_set = {r1_letters, r2_letters, r3_letters}
        return len(letters_set) == len(rotor_combinations)

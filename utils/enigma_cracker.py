import itertools
from utils.settings import Settings
from utils.enigma import Enigma
from multiprocessing import Pool


class EnigmaCracker:

    def __init__(self, possible_settings, starting_position=""):
        self._code = ""
        self._cribs = []
        self._possible_settings = possible_settings.get_settings()
        self._starting_position = starting_position

    def crack_code(self, code, cribs, multiprocess=False):
        self._code = code
        self._cribs = cribs
        if self._starting_position:
            self._possible_settings['rotor_1']['start_positions'] = self._starting_position[0]
            self._possible_settings['rotor_2']['start_positions'] = self._starting_position[1]
            self._possible_settings['rotor_3']['start_positions'] = self._starting_position[2]
        if multiprocess:
            return [data for data in self._find_settings_brute_force_multiprocess()]
        return [data for data in self._find_settings_brute_force()]

    def _find_settings_brute_force(self):
        for crib in self._cribs:
            for settings in self._create_settings_generator_object():
                yield self._try_these_settings({'crib': crib, 'settings': settings, 'code': self._code})
        return None

    def _find_settings_brute_force_multiprocess(self):
        data = self._multiprocessing_data_generator()
        pool = Pool()
        result = pool.map(self._try_these_settings, data)
        pool.close()
        return result

    def _multiprocessing_data_generator(self):
        for crib in self._cribs:
            for settings in self._create_settings_generator_object():
                yield {'crib': crib, 'settings': settings, 'code': self._code}

    @staticmethod
    def _try_these_settings(data):
        cracked_code = Enigma(settings=data['settings']).parse(data['code'])
        if data['crib'] in cracked_code:
            print(data['settings'].get_reflector_data(), data['crib'], cracked_code)
            return {'settings': data['settings'], 'crib': data['crib'], 'cracked_code': cracked_code}

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

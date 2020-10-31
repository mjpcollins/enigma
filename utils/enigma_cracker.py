import itertools
from string import ascii_uppercase
from utils.settings import Settings
from utils.enigma import Enigma
from multiprocessing import Pool


class EnigmaCracker:

    def __init__(self, possible_settings, starting_position=""):
        self._code = ""
        self._cribs = []
        self._possible_settings = possible_settings.get_settings()
        self._set_starting_positions(starting_position)

    def crack_code(self, code, cribs, multiprocess=False):
        self._input_checks(code, cribs)
        self._code = code
        self._cribs = cribs
        if multiprocess:
            found_settings = self._find_settings_brute_force_multiprocess()
        else:
            found_settings = self._find_settings_brute_force()
        return [settings_data for settings_data in found_settings if settings_data]

    def _set_starting_positions(self, starting_position):
        for idx, position in enumerate(starting_position):
            self._possible_settings[f'rotor_{idx + 1}']['start_positions'] = position

    def _find_settings_brute_force_multiprocess(self):
        pool = Pool()
        result = pool.map(func=self._try_these_settings,
                          iterable=self._data_generator())
        pool.close()
        return result

    def _find_settings_brute_force(self):
        for settings in self._data_generator():
            yield self._try_these_settings(settings)

    def _data_generator(self):
        for crib in self._cribs:
            for settings in self._settings_generator():
                yield {'crib': crib, 'settings': settings, 'code': self._code}

    @staticmethod
    def _try_these_settings(data):
        enigma = Enigma(settings=data['settings'], error_checks=False, correct_case=False)
        cracked_code = enigma.parse(data['code'])
        if data['crib'] in cracked_code:
            print({'cracked_code': cracked_code, 'crib': data['crib'], 'settings': str(data['settings'])})
            return {'cracked_code': cracked_code, 'crib': data['crib'], 'settings': data['settings']}

    def _settings_generator(self):
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
        rotor_settings = [self._possible_settings[key] for key in self._possible_settings if "rotor_" in key]
        slots = [self._rotor_slot_generator(rotor_slot) for rotor_slot in rotor_settings]
        for rotors_combination in itertools.product(*slots):
            if self._distinct_rotors(rotors_combination):
                yield rotors_combination

    @staticmethod
    def _rotor_slot_generator(rotor_slot):
        for rotor_choice in rotor_slot['rotor_choices']:
            for ring_setting in rotor_slot['ring_settings']:
                for start_position in rotor_slot['start_positions']:
                    rotor_data = rotor_choice.copy()
                    rotor_data.update({'ring_setting': ring_setting,
                                       'start_position': start_position})
                    yield rotor_data

    @staticmethod
    def _distinct_rotors(rotor_combinations):
        rotor_letters_set = {rc['letters'] for rc in rotor_combinations}
        return len(rotor_letters_set) == len(rotor_combinations)

    def _input_checks(self, code, cribs):
        self._test_input(code)
        try:
            assert type(cribs) is list
        except AssertionError:
            raise ValueError("Please give input cribs as as list")
        try:
            assert len(cribs)
        except AssertionError:
            raise ValueError("Please input at least one crib")
        for crib in cribs:
            self._test_input(crib)

    @staticmethod
    def _test_input(input_text):
        try:
            assert type(input_text) == str
            for letter in input_text:
                try:
                    assert letter.upper() in ascii_uppercase
                except AssertionError:
                    raise SyntaxError("Please ensure input only contains all upper case alphabet characters, no spaces")

        except AssertionError:
            raise TypeError(f"{type(input_text)} is not a valid code or crib type. Please try a string.")
        return True
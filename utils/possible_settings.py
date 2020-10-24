from string import ascii_uppercase
from itertools import product
from utils.data import Data
from utils.reflector import Reflector
from utils.entry_wheel import EntryWheel


class PossibleSettings:

    def __init__(self, data=None):
        if data is None:
            data = Data()
        self._data = data
        self.set_machine("example_machine")
        self._possible_settings = {"entry_wheels": [],
                                   "rotor_1": {},
                                   "rotor_2": {},
                                   "rotor_3": {},
                                   "reflectors": [],
                                   "switchboards": []}

    def set_machine(self, machine):
        self._data.set_machine(machine)

    def generate_rotor_1_options(self, **kwargs):
        self._possible_settings['rotor_1'] = self._generate_rotor_options(**kwargs)

    def generate_rotor_2_options(self, **kwargs):
        self._possible_settings['rotor_2'] = self._generate_rotor_options(**kwargs)

    def generate_rotor_3_options(self, **kwargs):
        self._possible_settings['rotor_3'] = self._generate_rotor_options(**kwargs)

    def _generate_rotor_options(self, rotors=None,
                                ring_settings=None, start_positions=None):
        if start_positions is None:
            start_positions = ascii_uppercase
        if ring_settings is None:
            ring_settings = [i + 1 for i in range(26)]
        if rotors is None:
            rotors = self._data.list_rotors()

        rotor_choices = [self._data.get_rotor(rotor) for rotor in rotors]
        return_dict = {"rotor_choices": rotor_choices,
                       "ring_settings": ring_settings,
                       "start_positions": start_positions}
        return return_dict

    def generate_reflector_options(self, reflectors=None):
        if reflectors is None:
            reflectors = self._data.list_reflectors()
        self._possible_settings['reflectors'] = [Reflector(**self._data.get_reflector(reflector))
                                                 for reflector in reflectors]

    def generate_entry_wheel_options(self, entry_wheels=None):
        if entry_wheels is None:
            entry_wheels = self._data.list_entry_wheels()
        self._possible_settings['entry_wheels'] = [EntryWheel(**self._data.get_entry_wheel(entry_wheel))
                                                   for entry_wheel in entry_wheels]

    def generate_switchboard_options(self, switchboard_setup=None):
        if switchboard_setup is None:
            switchboard_setup = list()  # Definitely not generating all combinations.
        iter_lists = [[swap_pair] for swap_pair in switchboard_setup if "?" not in swap_pair]
        all_letters = "".join(switchboard_setup)
        for swap_pair in switchboard_setup:
            if '?' in swap_pair:
                iter_lists.append(self._generate_pairs_options_list(swap_pair, exclusions=all_letters))
        all_switchboard_combinations = [list(option) for option in product(*iter_lists)]
        possible_switchboards = self._remove_contradictions_from_switchboard(all_switchboard_combinations)
        return possible_switchboards

    def _generate_pairs_options_list(self, swap_pair, exclusions=""):
        remove_exclusions = str.maketrans("", "", exclusions)
        if swap_pair[0] is "?":
            left_options = ascii_uppercase.translate(remove_exclusions)
        else:
            left_options = swap_pair[0]

        if swap_pair[1] is "?":
            right_options = ascii_uppercase.translate(remove_exclusions)
        else:
            right_options = swap_pair[1]
        possible_pairs = ["".join(option) for option in product(left_options, right_options)
                          if option[0] != option[1]]
        return possible_pairs

    @staticmethod
    def _remove_contradictions_from_switchboard(switchboard_options):
        possible_switchboards = list()
        for option in switchboard_options:
            all_letters = "".join(option)
            if len(set(all_letters)) == len(all_letters):
                possible_switchboards.append(option)
        return possible_switchboards

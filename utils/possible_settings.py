import itertools
from string import ascii_uppercase
from utils.enigma_machine_data import EnigmaMachineData
from utils.misc import letter_to_prime, alpha_to_number
from utils.reflector import Reflector


class PossibleSettings:

    def __init__(self, data=None):
        if data is None:
            data = EnigmaMachineData()
        self._data = data
        self._possible_settings = {}
        self.set_machine("example_machine")

    def set_machine(self, machine):
        self._data.set_machine(machine)
        self._possible_settings['machine'] = machine

    def get_settings(self):
        return self._possible_settings

    def generate_rotor_1_options(self, **kwargs):
        self._possible_settings['rotor_1'] = self._generate_rotor_options(machine_position=1,
                                                                          **kwargs)

    def generate_rotor_2_options(self, **kwargs):
        self._possible_settings['rotor_2'] = self._generate_rotor_options(machine_position=2,
                                                                          **kwargs)

    def generate_rotor_3_options(self, **kwargs):
        self._possible_settings['rotor_3'] = self._generate_rotor_options(machine_position=3,
                                                                          **kwargs)

    def generate_rotor_4_options(self, **kwargs):
        self._possible_settings['rotor_4'] = self._generate_rotor_options(machine_position=4,
                                                                          **kwargs)

    def _generate_rotor_options(self, machine_position, rotors=None,
                                ring_settings=None, start_positions=None):
        if start_positions is None:
            start_positions = ascii_uppercase
        if ring_settings is None:
            ring_settings = [i + 1 for i in range(26)]
        if rotors is None:
            rotors = self._data.list_rotors()

        rotor_choices = list()
        for rotor in rotors:
            rotor_data = self._data.get_rotor(rotor).copy()
            rotor_data['position'] = machine_position
            rotor_choices.append(rotor_data)

        return_dict = {"rotor_choices": rotor_choices,
                       "ring_settings": ring_settings,
                       "start_positions": start_positions}
        return return_dict

    def generate_reflector_options(self, reflectors=None):
        if reflectors is None:
            reflectors = self._data.list_reflectors()
        self._possible_settings['reflectors'] = [self._data.get_reflector(reflector)
                                                 for reflector in reflectors]

    def generate_custom_reflector_options(self, reflectors=None, alterations=1):
        if reflectors is None:
            reflectors = self._data.list_reflectors()
        custom_reflectors = []
        reflector_letters_set = set()
        for reflector in reflectors:
            for custom_wiring in self._generate_custom_wiring_options(alterations=alterations):
                custom_reflector = self._swap_reflector_wires(reflector_settings=self._data.get_reflector(reflector),
                                                              swap_letters=custom_wiring)
                if custom_reflector:
                    if custom_reflector['letters'] not in reflector_letters_set:
                        custom_reflectors.append(custom_reflector)
                        reflector_letters_set.add(custom_reflector['letters'])
        print(f"Set up for {len(custom_reflectors)} reflector combinations!")
        self._possible_settings['reflectors'] = custom_reflectors

    def generate_entry_wheel_options(self, entry_wheels=None):
        if entry_wheels is None:
            entry_wheels = self._data.list_entry_wheels()
        self._possible_settings['entry_wheels'] = [self._data.get_entry_wheel(entry_wheel)
                                                   for entry_wheel in entry_wheels]

    def generate_switchboard_options(self, switchboard_setup=None):
        if switchboard_setup is None:
            switchboard_setup = list()  # Definitely not generating all combinations.
        iter_lists = [[swap_pair] for swap_pair in switchboard_setup if "?" not in swap_pair]
        all_letters = "".join(switchboard_setup)
        for swap_pair in switchboard_setup:
            if '?' in swap_pair:
                iter_lists.append(self._generate_pairs_options_list(swap_pair, exclusions=all_letters))
        all_switchboard_combinations = [list(option) for option in itertools.product(*iter_lists)]
        possible_switchboards = self._remove_contradictions_from_switchboard(all_switchboard_combinations)
        self._possible_settings['switchboards'] = possible_switchboards

    @staticmethod
    def _generate_pairs_options_list(swap_pair, exclusions=""):
        remove_exclusions = str.maketrans("", "", exclusions)
        if swap_pair[0] is "?":
            left_options = ascii_uppercase.translate(remove_exclusions)
        else:
            left_options = swap_pair[0]

        if swap_pair[1] is "?":
            right_options = ascii_uppercase.translate(remove_exclusions)
        else:
            right_options = swap_pair[1]
        possible_pairs = ["".join(option) for option in itertools.product(left_options, right_options)
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

    def _swap_reflector_wires(self, reflector_settings, swap_letters):
        for letter_idx in range(len(swap_letters)):
            if letter_idx % 2 == 0:
                swap = swap_letters[letter_idx] + swap_letters[letter_idx + 1]
                reflector_settings = self._swap_one_reflector_wire(reflector_settings, swap)
                if reflector_settings is None:
                    return None
        return reflector_settings

    def _swap_one_reflector_wire(self, reflector_settings, swap_letters):
        re = Reflector(**reflector_settings)
        swap_pair1 = [alpha_to_number(swap_letters[0]),
                      alpha_to_number(swap_letters[1])]
        swap_pair2 = [alpha_to_number(re.forward_flow(swap_letters[0])),
                      alpha_to_number(re.forward_flow(swap_letters[1]))]

        if len(set(swap_pair1 + swap_pair2)) != 4:
            return None

        output_reflector_settings = reflector_settings.copy()
        letters = self._swap_letter_position(output_reflector_settings['letters'], swap_pair1)
        letters = self._swap_letter_position(letters, swap_pair2)
        output_reflector_settings['letters'] = letters
        return output_reflector_settings

    @staticmethod
    def _swap_letter_position(letters, swap_pair):
        letters_list = list(letters)
        letters_list[swap_pair[0]], letters_list[swap_pair[1]] = letters_list[swap_pair[1]], letters_list[swap_pair[0]]
        return "".join(letters_list)

    def _generate_custom_wiring_options(self, alterations):
        all_combos = []
        res = []
        combination_set = set()
        combinations = list(itertools.combinations(ascii_uppercase, 2))
        for _ in range(alterations):
            all_combos.append(["".join(combo) for combo in combinations if combo[0] != combo[1]])
        for item in itertools.product(*all_combos):
            combos = "".join(item)
            if self._combos_are_unique_wire_swaps(combos) and self._combos_not_in_set(combos, combination_set):
                res.append(combos)
        return res

    @staticmethod
    def _combos_are_unique_wire_swaps(combination):
        return len(combination) == len(set(combination))

    @staticmethod
    def _combos_not_in_set(combination, set_of_combinations):
        """
        When swapping wires, an AC swap followed by an IJ swap is identical to JI followed by CA. However,
        CJ followed by IA is not the same. Checking for this can be tricky, but prime numbers make it easier.

        Every letter is mapped to a prime number (from 2, to 101), multiplied with its pair, and then placed in a list.
        The list is sorted to give a standard way of representing the various ways of performing identical swaps. This
        list is added to a set if it hasn't been seen before and ignored if it has been.

        :param combination: String, A combination of pairs to check if it has been seen
        :param set_of_combinations: Set, All combinations of pairs that have been seen
        :return: Boolean, True if not in set, False if in set.
        """

        total = list()
        previous = 0
        for idx, letter in enumerate(combination):
            prime_of_letter = letter_to_prime(letter=letter)
            if idx % 2 == 0:
                previous = prime_of_letter
            else:
                total.append(previous * prime_of_letter)
                previous = 0
        total.sort()
        if str(total) in set_of_combinations:
            return False
        set_of_combinations.add(str(total))
        return True

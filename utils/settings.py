from string import ascii_uppercase


class Settings:

    def __init__(self):
        self._reflector_data = {}
        self._rotors_data = list()
        self._entry_wheel_data = {"letters": ascii_uppercase}
        self._switchboard_data = {"pairs": list()}

    def set_reflector(self, letters):
        self._reflector_data = {"letters": letters}

    def add_rotors(self, list_of_rotors):
        for rotor in list_of_rotors:
            self.add_rotor(**rotor)

    def add_rotor(self, letters, start_position, position, turnover="", ring_setting=1):
        rotor_data = {"letters": letters,
                      "start_position": start_position,
                      "turnover": turnover,
                      "position": position,
                      "ring_setting": ring_setting - 1}
        self._rotors_data.append(rotor_data)
        self._rotors_data.sort(key=lambda x: x['position'])

    def set_rotor_start_position(self, rotor_position, start_position):
        self._rotors_data[rotor_position]['start_position'] = start_position

    def set_entry_wheel(self, letters=ascii_uppercase):
        self._entry_wheel_data = {"letters": letters}

    def set_switchboard_pairs(self, pairs):
        self._switchboard_data = {"pairs": pairs}

    def remove_rotor(self):
        self._rotors_data.pop()

    def remove_all_rotors(self):
        self._rotors_data = list()

    def get_rotors_data(self):
        return self._rotors_data

    def get_switchboard_data(self):
        return self._switchboard_data

    def get_reflector_data(self):
        return self._reflector_data

    def get_entry_wheel_data(self):
        return self._entry_wheel_data

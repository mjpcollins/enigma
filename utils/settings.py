

class Settings:

    def __init__(self):
        self._reflector_data = {}
        self._wheels_data = list()
        self._entry_wheel_data = {"letters": "ABCEDFGHIJKLMNOPQRSTUVWXYZ"}
        self._switchboard_data = {"pairs": list()}

    def set_reflector(self, letters):
        self._reflector_data = {"letters": letters}

    def add_wheel(self, letters, start_position, turnover, position):
        wheel_data = {"letters": letters,
                      "start_position": start_position,
                      "turnover": turnover,
                      "position": position}
        self._wheels_data.append(wheel_data)

    def set_entry_wheel(self, letters="ABCEDFGHIJKLMNOPQRSTUVWXYZ"):
        self._entry_wheel_data = {"letters": letters}

    def set_switchboard_pairs(self, pairs):
        self._switchboard_data = {"pairs": pairs}

    def remove_wheel(self):
        self._wheels_data.pop()

    def remove_all_wheels(self):
        self._wheels_data = list()

    def get_wheels_data(self):
        return self._wheels_data

    def get_switchboard_data(self):
        return self._switchboard_data

    def get_reflector_data(self):
        return self._reflector_data

    def get_entry_wheel_data(self):
        return self._entry_wheel_data
import json


class EnigmaMachineData:

    def __init__(self, filename="./data/rotors.json", machine=None):
        self._filename = filename
        self._loaded_json = self._load_json(filename)
        self._machine = machine

    def get_machine(self):
        return self._machine

    def set_machine(self, machine):
        self._machine = machine

    def get_rotor(self, rotor):
        return self._loaded_json[self._machine]['rotor'].get(rotor)

    def get_reflector(self, reflector):
        return self._loaded_json[self._machine]['reflector'].get(reflector)

    def get_entry_wheel(self, entry_wheel):
        return self._loaded_json[self._machine]['entry_wheel'].get(entry_wheel)

    def list_rotors(self):
        rotors = list(self._loaded_json[self._machine]['rotor'].keys())
        rotors.sort()
        return rotors

    def list_reflectors(self):
        reflectors = list(self._loaded_json[self._machine]['reflector'].keys())
        reflectors.sort()
        return reflectors

    def list_entry_wheels(self):
        etw = list(self._loaded_json[self._machine]['entry_wheel'].keys())
        etw.sort()
        return etw

    @staticmethod
    def _load_json(path):
        with open(path, "r") as F:
            j = json.load(F)
        return j

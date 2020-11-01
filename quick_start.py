from utils import EnigmaMachineData, Enigma, Settings

machine_data = EnigmaMachineData()
settings = Settings()

machine_data.set_machine("m4")
etw = machine_data.get_entry_wheel('etw')
rotor_1 = machine_data.get_rotor("gamma")
rotor_2 = machine_data.get_rotor("iv")
rotor_3 = machine_data.get_rotor("vii")
rotor_4 = machine_data.get_rotor("i")
ref = machine_data.get_reflector("b-thin")
rotor_1.update({'start_position': 'A', 'position': 1})
rotor_2.update({'start_position': 'A', 'position': 2})
rotor_3.update({'start_position': 'A', 'position': 3})
rotor_4.update({'start_position': 'A', 'position': 4})

settings.add_entry_wheel(etw)
settings.add_rotors([rotor_1, rotor_2, rotor_3, rotor_4])
settings.add_reflector(ref)
settings.set_switchboard_pairs(['AB', 'XW'])

enigma = Enigma(settings=settings)

print(enigma.parse("HELLOWORLD"))

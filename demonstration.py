from utils import EnigmaMachineData, Enigma, Settings, Rotor

machine_data = EnigmaMachineData()
machine_data.set_machine("example_machine")


def rotor_from_name(name_of_rotor):
    data = machine_data.get_rotor(name_of_rotor)
    data.update({'start_position': 'A', 'position': 1})
    return Rotor(**data)


def multiple_rotors_1():
    rotor_1 = machine_data.get_rotor("i")
    rotor_2 = machine_data.get_rotor("ii")
    rotor_3 = machine_data.get_rotor("iii")
    etw = machine_data.get_entry_wheel('etw')
    reflector = machine_data.get_reflector("b")

    rotor_1.update({'start_position': 'A', 'position': 1})
    rotor_2.update({'start_position': 'A', 'position': 2})
    rotor_3.update({'start_position': 'Z', 'position': 3})

    settings = Settings()
    settings.add_entry_wheel(etw)
    settings.add_rotors([rotor_1, rotor_2, rotor_3])
    settings.add_reflector(reflector)

    enigma = Enigma(settings=settings)

    print(enigma.parse("A"))


def multiple_rotors_2():
    rotor_1 = machine_data.get_rotor("i")
    rotor_2 = machine_data.get_rotor("ii")
    rotor_3 = machine_data.get_rotor("iii")
    etw = machine_data.get_entry_wheel('etw')
    reflector = machine_data.get_reflector("b")

    rotor_1.update({'start_position': 'A', 'position': 1})
    rotor_2.update({'start_position': 'A', 'position': 2})
    rotor_3.update({'start_position': 'A', 'position': 3})

    settings = Settings()
    settings.add_entry_wheel(etw)
    settings.add_rotors([rotor_1, rotor_2, rotor_3])
    settings.add_reflector(reflector)

    enigma = Enigma(settings=settings)

    print(enigma.parse("A"))


def multiple_rotors_3():
    rotor_1 = machine_data.get_rotor("i")
    rotor_2 = machine_data.get_rotor("ii")
    rotor_3 = machine_data.get_rotor("iii")
    etw = machine_data.get_entry_wheel('etw')
    reflector = machine_data.get_reflector("b")

    rotor_1.update({'start_position': 'Q', 'position': 1})
    rotor_2.update({'start_position': 'E', 'position': 2})
    rotor_3.update({'start_position': 'V', 'position': 3})

    settings = Settings()
    settings.add_entry_wheel(etw)
    settings.add_rotors([rotor_1, rotor_2, rotor_3])
    settings.add_reflector(reflector)

    enigma = Enigma(settings=settings)

    print(enigma.parse("A"))


def multiple_rotors_4():
    rotor_1 = machine_data.get_rotor("iv")
    rotor_2 = machine_data.get_rotor("v")
    rotor_3 = machine_data.get_rotor("beta")
    etw = machine_data.get_entry_wheel('etw')
    reflector = machine_data.get_reflector("b")

    rotor_1.update({'start_position': 'A', 'position': 1, 'ring_setting': 14})
    rotor_2.update({'start_position': 'A', 'position': 2, 'ring_setting': 9})
    rotor_3.update({'start_position': 'A', 'position': 3, 'ring_setting': 24})

    settings = Settings()
    settings.add_entry_wheel(etw)
    settings.add_rotors([rotor_1, rotor_2, rotor_3])
    settings.add_reflector(reflector)

    enigma = Enigma(settings=settings)

    print(enigma.parse("H"))


def multiple_rotors_5():
    rotor_1 = machine_data.get_rotor("I")
    rotor_2 = machine_data.get_rotor("ii")
    rotor_3 = machine_data.get_rotor("III")
    rotor_4 = machine_data.get_rotor("iv")
    etw = machine_data.get_entry_wheel('etw')
    reflector = machine_data.get_reflector("c")

    rotor_1.update({'start_position': 'Q', 'position': 1, 'ring_setting': 7})
    rotor_2.update({'start_position': 'e', 'position': 2, 'ring_setting': 11})
    rotor_3.update({'start_position': 'V', 'position': 3, 'ring_setting': 15})
    rotor_4.update({'start_position': 'Z', 'position': 4, 'ring_setting': 19})

    settings = Settings()
    settings.add_entry_wheel(etw)
    settings.add_rotors([rotor_1, rotor_2, rotor_3, rotor_4])
    settings.add_reflector(reflector)

    enigma = Enigma(settings=settings)

    print(enigma.parse("Z"))


def example_1():
    rotor_1 = machine_data.get_rotor("i")
    rotor_2 = machine_data.get_rotor("ii")
    rotor_3 = machine_data.get_rotor("iii")
    etw = machine_data.get_entry_wheel('etw')
    reflector = machine_data.get_reflector("b")

    rotor_1.update({'start_position': 'A', 'position': 1})
    rotor_2.update({'start_position': 'A', 'position': 2})
    rotor_3.update({'start_position': 'Z', 'position': 3})

    settings = Settings()
    settings.add_entry_wheel(etw)
    settings.add_rotors([rotor_1, rotor_2, rotor_3])
    settings.add_reflector(reflector)
    settings.set_switchboard_pairs(['HL', 'MO', 'AJ', 'CX', 'BZ', 'SR', 'NI', 'YW', 'DG', 'PK'])

    enigma = Enigma(settings=settings)

    print(enigma.parse("HELLOWORLD"))


def example_2():
    rotor_1 = machine_data.get_rotor("iv")
    rotor_2 = machine_data.get_rotor("v")
    rotor_3 = machine_data.get_rotor("beta")
    rotor_4 = machine_data.get_rotor("i")
    etw = machine_data.get_entry_wheel('etw')
    reflector = machine_data.get_reflector("a")

    rotor_1.update({'start_position': 'E', 'position': 1, 'ring_setting': 18})
    rotor_2.update({'start_position': 'Z', 'position': 2, 'ring_setting': 24})
    rotor_3.update({'start_position': 'G', 'position': 3, 'ring_setting': 3})
    rotor_4.update({'start_position': 'P', 'position': 4, 'ring_setting': 5})

    settings = Settings()
    settings.add_entry_wheel(etw)
    settings.add_rotors([rotor_1, rotor_2, rotor_3, rotor_4])
    settings.add_reflector(reflector)
    settings.set_switchboard_pairs(['PC', 'XZ', 'FM', 'QA', 'ST',
                                    'NB', 'HY', 'OR', 'EV', 'IU'])

    enigma = Enigma(settings=settings)

    print(enigma.parse("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI"))


def run():
    assert(rotor_from_name("I").encode_right_to_left("A") == "E")
    assert(rotor_from_name("I").encode_left_to_right("A") == "U")
    multiple_rotors_1()
    multiple_rotors_2()
    multiple_rotors_3()
    multiple_rotors_4()
    multiple_rotors_5()
    example_1()
    example_2()


if __name__ == '__main__':
    run()

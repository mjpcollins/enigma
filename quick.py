from utils import EnigmaCracker, PossibleSettings

def odd_num_in_num(num):
    for number in str(num):
        if int(number) % 2 != 0:
            return True
    return False
ring_sets = [num for num in range(1, 27) if not odd_num_in_num(num)]

ps = PossibleSettings()
ps.generate_entry_wheel_options()
ps.generate_rotor_1_options(rotors=["beta", "gamma", "ii", "iv"], ring_settings=ring_sets)
ps.generate_rotor_2_options(rotors=["beta", "gamma", "ii", "iv"], ring_settings=ring_sets)
ps.generate_rotor_3_options(rotors=["beta", "gamma", "ii", "iv"], ring_settings=ring_sets)
ps.generate_reflector_options()
ps.generate_switchboard_options(['FH', 'TS', 'BE', 'UQ', 'KD', 'AL'])
cracker = EnigmaCracker(possible_settings=ps,
                        starting_position="EMY")
answer = cracker.crack_code(code="ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY",
                            cribs=['THOUSANDS'])
print(answer)
print(answer['settings'].get_rotors_data())


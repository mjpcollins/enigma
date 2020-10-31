from utils import EnigmaCracker, PossibleSettings
import time


def code_3():
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
    run_crack(cracker=cracker,
              code="ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY",
              cribs=['THOUSANDS'])


def code_4():
    ps = PossibleSettings()
    ps.generate_entry_wheel_options()
    ps.generate_rotor_1_options(rotors=["v"], ring_settings=[24])
    ps.generate_rotor_2_options(rotors=["iii"], ring_settings=[12])
    ps.generate_rotor_3_options(rotors=["iv"], ring_settings=[10])
    ps.generate_reflector_options(reflectors=['a'])
    ps.generate_switchboard_options(['WP', 'RJ', 'A?', 'VF', 'I?', 'HN', "CG", "BS"])
    cracker = EnigmaCracker(possible_settings=ps,
                            starting_position="SWU")
    run_crack(cracker=cracker,
              code="SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW",
              cribs=['TUTOR'])


def code_5():
    ps = PossibleSettings()
    ps.generate_entry_wheel_options()
    ps.generate_rotor_1_options(rotors=["v"], ring_settings=[6])
    ps.generate_rotor_2_options(rotors=["ii"], ring_settings=[18])
    ps.generate_rotor_3_options(rotors=["iv"], ring_settings=[7])
    ps.generate_custom_reflector_options(alterations=2)
    ps.generate_switchboard_options(['UG', 'IE', 'PO', 'NX', 'WT'])
    cracker = EnigmaCracker(possible_settings=ps,
                            starting_position="AJL")
    run_crack(cracker=cracker,
              code="HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX",
              cribs=['INSTAGRAM'])


def run_crack(cracker, cribs, code):
    t1 = time.time()
    cracker.crack_code(code=code,
                       cribs=cribs,
                       multiprocess=True)
    t2 = time.time()
    print(f"\nTime to crack: {t2 - t1} seconds")


if __name__ == '__main__':
    code_4()

from utils import EnigmaCracker, PossibleSettings
import time


def code_1():
    """
    Cracked code: NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING
    Crib: SECRETS
    Rotors: Beta Gamma V
    Reflector: C
    Ring settings: 4 2 14
    Starting positions: MJM
    Plug board: KI XN FL
    """
    ps = PossibleSettings()
    ps.generate_entry_wheel_options()
    ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
    ps.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
    ps.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
    ps.generate_reflector_options()
    ps.generate_switchboard_options(['KI', 'XN', 'FL'])
    cracker = EnigmaCracker(possible_settings=ps,
                            starting_position="MJM")
    run_crack(cracker=cracker,
              code="DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ",
              cribs=['SECRETS'])


def code_2():
    """
    Cracked code: IHOPEYOUAREENJOYINGTHEUNIVERSITYOFBATHEXPERIENCESOFAR
    Crib: UNIVERSITY
    Rotors: Beta I III
    Reflector: B
    Ring settings: 23 2 10
    Starting positions: IMG
    Plug board: FH TS BE UQ KD AL
    """
    ps = PossibleSettings()
    ps.generate_entry_wheel_options()
    ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[23])
    ps.generate_rotor_2_options(rotors=["i"], ring_settings=[2])
    ps.generate_rotor_3_options(rotors=["iii"], ring_settings=[10])
    ps.generate_reflector_options(reflectors=["b"])
    ps.generate_switchboard_options(['VH', 'PT', 'ZG', 'BJ', 'EY', 'FS'])
    cracker = EnigmaCracker(possible_settings=ps)
    run_crack(cracker=cracker,
              code="CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH",
              cribs=['UNIVERSITY'])


def code_3():
    """
    Cracked code: SQUIRRELSPLANTTHOUSANDSOFNEWTREESEACHYEARBYMERELYFORGETTINGWHERETHEYPUTTHEIRACORNS
    Crib: THOUSANDS
    Rotors: II Gamma IV
    Reflector: C
    Ring settings: 24 8 20
    Starting positions: EMY
    Plug board: FH TS BE UQ KD AL
    """
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
    """
    Cracked code: NOTUTORSWEREHARMEDNORIMPLICATEDOFCRIMESDURINGTHEMAKINGOFTHESEEXAMPLES
    Crib: TUTOR
    Rotors: V III IV
    Reflector: A
    Ring settings: 24 12 10
    Starting positions: SWU
    Plug board: WP RJ VF HN CG BS AT IK
    """
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
    """
    Cracked code: YOUCANFOLLOWMYDOGONINSTAGRAMATTALESOFHOFFMANN
    Crib: INSTAGRAM
    Rotors: V II IV
    Reflector: B, with alterations (PQUHRSLDYXNGOKMABEFZCWVJIT)
    Ring settings: 6 18 7
    Starting positions: AJL
    Plug board: UG IE PO NX WT
    """
    ps = PossibleSettings()
    ps.generate_entry_wheel_options()
    ps.generate_rotor_1_options(rotors=["v"], ring_settings=[6])
    ps.generate_rotor_2_options(rotors=["ii"], ring_settings=[18])
    ps.generate_rotor_3_options(rotors=["iv"], ring_settings=[7])
    ps.generate_custom_reflector_options(reflectors=['b'], alterations=2)
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
    print(f"\nTime to check all possible settings: {t2 - t1} seconds\n")


if __name__ == '__main__':
    code_1()
    code_2()
    code_3()
    code_4()
    code_5()

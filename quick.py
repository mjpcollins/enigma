from utils import PossibleSettings, CribFinder

cf = CribFinder(code="DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ")
cribs = cf.find_crib_in_code("SECRETS")
print(cribs)

ps = PossibleSettings()
ps.generate_entry_wheel_options()
ps.generate_rotor_1_options(rotors=["beta"], ring_settings=[4])
ps.generate_rotor_2_options(rotors=["gamma"], ring_settings=[2])
ps.generate_rotor_3_options(rotors=["v"], ring_settings=[14])
ps.generate_reflector_options()
ps.generate_switchboard_options(['KI', 'XN', 'FL'])
print()


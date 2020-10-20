from utils import Settings, Enigma, Data

settings = Settings()
data = Data()
data.set_machine("example_machine")

iv = data.get_rotor("iv")
v = data.get_rotor("v")
beta = data.get_rotor("beta")
i = data.get_rotor("i")

# Bug is due to V rotating even though G doesn't rotate????
iv.update({"start_position": "E", "ring_setting": 18, "position": 1})
v.update({"start_position": "Z", "ring_setting": 24, "position": 2})
beta.update({"start_position": "G", "ring_setting": 3, "position": 3})
i.update({"start_position": "P", "ring_setting": 5, "position": 4})

settings.add_rotors([iv, v, beta, i])
settings.set_reflector(**data.get_reflector("a"))
settings.set_switchboard_pairs(["PC", "XZ", "FM", "QA", "ST",
                                "NB", "HY", "OR", "EV", "IU"])
enigma = Enigma(settings=settings)

# print(enigma.scrambler._rotors[3].get_current_position())
# print(enigma.scrambler._rotors[2].get_current_position())
# print(enigma.scrambler._rotors[1].get_current_position())
# print(enigma.scrambler._rotors[0].get_current_position())
# print("---")
#
# enigma.press_key("B")
# print(enigma.scrambler._rotors[3].get_current_position())
# print(enigma.scrambler._rotors[2].get_current_position())
# print(enigma.scrambler._rotors[1].get_current_position())
# print(enigma.scrambler._rotors[0].get_current_position())

# enigma.scrambler._rotors[0].set_current_position("Q")
# print(enigma.scrambler._rotors[3].get_current_position())
# print(enigma.scrambler._rotors[2].get_current_position())
# print(enigma.scrambler._rotors[1].get_current_position())
# print(enigma.scrambler._rotors[0].get_current_position())
# print("---")
# l = enigma.switchboard.flow_through("B")
# l = enigma.scrambler.flow_through(l)
# print(enigma.switchboard.flow_through(l))

message = enigma.parse("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI")
print(message)


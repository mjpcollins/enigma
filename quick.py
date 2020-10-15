from utils import Settings, Enigma, Data

settings = Settings()
data = Data()
data.set_machine("example_machine")
iv = data.get_rotor("iv")
v = data.get_rotor("v")
beta = data.get_rotor("beta")
i = data.get_rotor("i")
a = data.get_reflector("a")
iv.update({"start_position": "E", "ring_setting": 18, "position": 1})
v.update({"start_position": "Z", "ring_setting": 24, "position": 2})
beta.update({"start_position": "G", "ring_setting": 3, "position": 3})
i.update({"start_position": "P", "ring_setting": 5, "position": 4})
settings.add_rotors([iv, v, beta, i])
settings.set_reflector(**a)
settings.set_switchboard_pairs(["PC", "XZ", "FM", "QA", "ST",
                                "NB", "HY", "OR", "EV", "IU"])
message = Enigma(settings=settings).parse("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI")
print(message)


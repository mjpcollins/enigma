from utils import Settings, Enigma

settings = Settings()
settings.add_rotor(letters="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                   start_position="M",
                   turnover="Q",
                   position=0)
settings.add_rotor(letters="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                   start_position="E",
                   turnover="E",
                   position=1)
settings.add_rotor(letters="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                   start_position="U",
                   turnover="V",
                   position=2)
settings.set_reflector(letters="YRUHQSLDPXNGOKMIEBFZCWVJAT")
# p = ["bq", "cr", "di", "ej", "kw", "mt", "os", "px", "uz", "gh"]
# pairs = [pair.upper() for pair in p]
# settings.set_switchboard_pairs(pairs)
enigma = Enigma(settings=settings)
print(enigma.press_key("A"))

# enigma
Project for MSc AI course with Bath University

This is an [Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine) simulator and brute force cracker with implementations for the following machines:
- Example Machine for course ([Engima I](https://cryptomuseum.com/crypto/enigma/i/index.htm) plus a beta and gamma wheel from the [Enigma M4](https://cryptomuseum.com/crypto/enigma/m4/index.htm))
- [M3](https://cryptomuseum.com/crypto/enigma/m3/index.htm)
- [M4](https://cryptomuseum.com/crypto/enigma/m4/index.htm)
- [Norenigma](https://cryptomuseum.com/crypto/enigma/wiring.htm#8)
- [Sondermaschine](https://cryptomuseum.com/crypto/enigma/wiring.htm#9)

## Quick Start Enigma Machine

The Engima machine is best used in conjunction with the EnigmaMachineData class. An example of this use is copied below.

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


## Quick Start Enigma Machine Cracker

TODO


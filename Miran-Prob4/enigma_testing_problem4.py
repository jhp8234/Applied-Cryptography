
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

def print_configuration_info(config_number, config_desc, rotor_settings, reflector_settings, plugboard_settings, initial_display):
    print(f"Configuration {config_number}: {config_desc}")
    print(f"Rotor Settings: {rotor_settings}")
    print(f"Reflector Settings: {reflector_settings}")
    print(f"Plugboard Settings: {plugboard_settings}")
    print(f"Initial Display Position: {initial_display}")
    #print()

def format_plugboard_settings(plugboard):
  if plugboard is None:
    return "No plugboard"

  wiring = plugboard.wiring_map
  return ", ".join([f"{wiring[i]}->{wiring[j]}" for i, j in wiring if i != j])



# Configuration 1: Default Settings
rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')
reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')
machine = EnigmaMachine([rL, rM, rR], reflector, pb)
machine.set_display('UPS')
output = machine.process_text('HELLO')
#plugboard_settings = format_plugboard_settings(pb)
plugboard_settings = "AK BZ CG DL FU HJ MX NR OY PW"
config_desc = "Default Settings"
print_configuration_info(1, config_desc, [rL.ring_setting, rM.ring_setting, rR.ring_setting], reflector.ring_setting, plugboard_settings, machine.get_display())
print("Ciphertext:", output)
print()

# Configuration 2: Different Plugboard Settings
pb = Plugboard.from_key_sheet('AQ BF CK DL EU HJ MI NW OR PV')
machine = EnigmaMachine([rL, rM, rR], reflector, pb)
machine.set_display('UPS')
output = machine.process_text('HELLO')
#plugboard_settings = format_plugboard_settings(pb)
plugboard_settings = "AQ BF CK DL EU HJ MI NW OR PV"
config_desc = "Different Plugboard Settings"
print_configuration_info(2, config_desc, [rL.ring_setting, rM.ring_setting, rR.ring_setting], reflector.ring_setting, plugboard_settings, machine.get_display())
print("Ciphertext:", output)

#plaintext = machine.process_text('KFTIE')
#print("Plaintext:", plaintext)

print()

# Configuration 3: Different Ring Settings
rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=1, stepping='Q')
rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=2, stepping='V')
rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=3, stepping='J')
machine = EnigmaMachine([rL, rM, rR], reflector, pb)
machine.set_display('UPS')
output = machine.process_text('HELLO')
config_desc = "Different Ring Settings"
print_configuration_info(3, config_desc, [rL.ring_setting, rM.ring_setting, rR.ring_setting], reflector.ring_setting, plugboard_settings, machine.get_display())
print("Ciphertext:", output)
print()

# Configuration 4: Different Wiring
rL = Rotor('my rotor1', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=0, stepping='Q')
rM = Rotor('my rotor2', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=5, stepping='V')
rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')
machine = EnigmaMachine([rL, rM, rR], reflector, pb)
machine.set_display('UPS')
output = machine.process_text('HELLO')
config_desc = "Different Wiring"
print_configuration_info(4, config_desc, [rL.ring_setting, rM.ring_setting, rR.ring_setting], reflector.ring_setting, plugboard_settings, machine.get_display())
print("Ciphertext:", output)
print()

# Configuration 5: Different Reflector
reflector = Rotor('my reflector', 'FNUHYWAKEMTXDJQGBZCISORVLP')
machine = EnigmaMachine([rL, rM, rR], reflector, pb)
machine.set_display('UPS')
output = machine.process_text('HELLO')
#plugboard_settings = format_plugboard_settings(pb)
config_desc = "Different Reflector"
print_configuration_info(5, config_desc, [rL.ring_setting, rM.ring_setting, rR.ring_setting], reflector.ring_setting, plugboard_settings, machine.get_display())
print("Ciphertext:", output)
print()

# Configuration 6: Different Initial Display Position
machine.set_display('XYZ')
output = machine.process_text('HELLO')
config_desc = "Different Initial Display Position"
print_configuration_info(6, config_desc, [rL.ring_setting, rM.ring_setting, rR.ring_setting], reflector.ring_setting, plugboard_settings, machine.get_display())
print("Ciphertext:", output)
print()

# Configuration 7: Without Plugboard
machine = EnigmaMachine([rL, rM, rR], reflector, Plugboard())
machine.set_display('UPS')
output = machine.process_text('HELLO')
plugboard_settings = "No plugboard"
config_desc = "Without Plugboard"
print_configuration_info(7, config_desc, [rL.ring_setting, rM.ring_setting, rR.ring_setting], reflector.ring_setting, plugboard_settings, machine.get_display())
print("Ciphertext:", output)
print()

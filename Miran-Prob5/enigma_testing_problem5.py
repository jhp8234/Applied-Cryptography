
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

def decrypt(ciphertext, machine):
  """Decrypts the given ciphertext using the given Enigma machine."""
  plaintext = machine.process_text(ciphertext)
  return plaintext

# Load the Enigma machine configuration
rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')
reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
# Configuration 2: Different Plugboard Settings
pb = Plugboard.from_key_sheet('AQ BF CK DL EU HJ MI NW OR PV')


machine = EnigmaMachine([rL, rM, rR], reflector, pb)
machine.set_display('UPS')

#encrypt the 
ciphertext = machine.process_text('HELLO')
print(f"ciphertext: {ciphertext}")

# Decrypt the ciphertext
# Set the initial display position
machine.set_display('UPS')
plaintext = machine.process_text(ciphertext)
#plaintext = decrypt(ciphertext="KFTIE", machine=machine)

# Print the plaintext
print(f"Plaintext: {plaintext}")

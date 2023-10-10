
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

def bf_encrypt(rotor_positions):
    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display(rotor_positions)
    decrypted_text = machine.process_text('ATTACK AT 5PM AT ATLANTIC Z ISLAND')
    return decrypted_text

def find_rotor_position(ciphertext):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                rotor_positions = f'{chr(i+ord("A"))}{chr(j+ord("A"))}{chr(k+ord("A"))}'
                computed_ciphertext = bf_encrypt(rotor_positions)
                print(f"rotor_position: {rotor_positions} Input: {ciphertext} Computed: {computed_ciphertext}")
                if computed_ciphertext == ciphertext:
                    return rotor_positions

ciphertext = "WVUVJCSQBFLWSGTHDREWOSXYIAYEUBHHXY"
initial_position = find_rotor_position(ciphertext)
print(f"Initial Rotor Position: {initial_position}")

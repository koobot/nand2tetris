# Converts to binary
import re
from HackParser import Parser

# Convert decimal to binary

# C-instruction look up table
comp_dict = {
        "0":   "101010",
        "1":   "111111",
        "-1":  "111010",
        "D":   "001100",
        "X":   "110000",
        "!D":  "001101",
        "!X":  "110001",
        "-D":  "001111",
        "-X":  "110011",
        "D+1": "011111",
        "X+1": "110111",
        "D-1": "001110",
        "X-1": "110010",
        "D+X": "000010",
        "D-X": "010011",
        "X-D": "000111",
        "D&X": "000000",
        "D|X": "010101",
        }

# Destination lookup
dest_dict = {
        "null": "000",
        "M":    "001",
        "D":    "010",
        "MD":   "011",
        "A":    "100",
        "AM":   "101",
        "AD":   "110",
        "AMD":  "111"
        }

jmp_dict = {
        "null": "000",
        "JGT":  "001",
        "JEQ":  "010",
        "JGE":  "011",
        "JLT":  "100",
        "JNE":  "101",
        "JLE":  "110",
        "JMP":  "111"
        }

class Code(Parser):
    ''' Code object. Inherits from Parser object '''

    def convert_comp_field(self, string):
        ''' Called from convert_to_binary.
        Just does comp_bits of C-instruction
        Comp bits structure: a c1 c2 c3 c4 c5 c6 '''
        # Initialise comp_bits
        comp_bits = []

        # Derive 1st comp_bit (a)
        if re.search("M", string):
            comp_bits.append("1")
        else:
            comp_bits.append("0")

        # Then replace A or M with X. This makes look up easier.
        comp_key = re.sub("A|M", "X", string)
        c_bits = comp_dict[comp_key]
        comp_bits.append(c_bits)

        # Join to get full binary string
        comp_bin = "".join(comp_bits)

        return comp_bin


    def convert_to_binary(self):
        ''' Converts decimal to binary '''
        if self.instruction_type == "A-instruction":
            # Remove @
            addr_dec = int(re.sub("@", "", self))
            # Removes the '0b' from string
            addr_bin = bin(addr_dec)[2:]
            # Pad with 0's - assume 16-bit
            addr_bin = addr_bin.zfill(16)

            return addr_bin
        
        elif self.instruction_type == "C-instruction":
            ''' Converts command to binary '''
            # bits[0:3] C instruction always starts with 111
            c_components = ["111"]
            # bits[3:10] Convert computation field to binary
            comp_bin = self.convert_comp_field(self.comp())
            c_components.append(comp_bin)
            # bits[10:13] Convert destination field to binary
            dest_bin = dest_dict[self.dest()]
            c_components.append(dest_bin)
            # bits[13:16] Convert jump field to binary
            jmp_bin = jmp_dict[self.jmp()]
            c_components.append(jmp_bin)
            # Join all bits into string
            c_bin = "".join(c_components)

            return c_bin

            
        else:
            return "not A-instruction"
            


# Parser
# Takes an *.asm file path and unpacks each instruction into its underlying
# fields.

import re

def get_valid_commands(path):
    ''' Reads *.asm file path and returns a list of valid commands '''
    valid_commands = []
    file = open(path, 'r')
    
    for line in file.readlines():
        # Remove any comments (start with '//')
        line = re.sub("//.+$", "", line)
        # Ignore white space
        line = line.strip()
        if not line:
            continue # Next iteration of loop
        
        # Else valid command
        valid_commands.append(line)
    return valid_commands

class Parser(str):
    ''' For a given command '''
#    def __init__(self, command):
#        self.command = command

#    def __repr__(self):
#        return self.command

    @property
    def instruction_type(self):
        ''' Gets the instruction type. Returns string.
        Can be A-instruction, C-instruction, or label '''

        # A-instructions contain @
        if re.search("@", self):
            instruction = "A-instruction"
        # C-instructions always contain = or ;
        elif re.search("=|;", self):
            instruction = "C-instruction"
        # Label should start with open bracket
        elif re.search("\(", self):
            instruction = "label"
        else:
            print("Error - not valid instruction type")
        return instruction

    def check_c_instruct():
        ''' Splits a C-instruction into its separate fields.
        Returns a list '''
        # Check it's C-instruction
        if not self.instruction_type == "C-instruction":
            print("Can only get fields for C-instruction.")

        # Only split on = or ;
#        return re.split("[=;]", self)
 
    def dest(self):
        ''' Gets "destination" field for C-instruction.
        Returns string. '''
        # Only want first part before =
        if re.search("=", self):
            destination = re.search("(\w+)[=]", self).group(1)
        else:
            destination = "null"
        return destination

    def comp(self):
        ''' Gets "computation" field for C-instruction.
        Returns string.
        Three possible formats:
            1) dest=comp;jmp
            2) dest=comp
            3) comp;jmp
        Formats 1 & 2 can be consolidated in same search
        '''
        # Only want part after = but before optional ;
        format_a = re.search("=", self)
        format_b = re.match("(?<!\=)[-+!&|a-zA-Z0-9]+;", self)
        
        if format_a:
            computation = re.search("=([^;]+);*", self).group(1)
        elif format_b:
            computation = re.search("([^;]+);", self).group(1)
        
#        if computation:
#            return computation.group(1)
        else:
            #computation = "null"
            print("Something's wrong with computation")
        return computation

    def jmp(self):
        ''' Gets "jump" field for C-instruction.
        Returns string. '''
        # Only want after ; Allows for optional space after semi-colon
        jump = re.search(";\s*(\w+)", self)
        if jump:
            return jump.group(1)
        else:
            return "null"



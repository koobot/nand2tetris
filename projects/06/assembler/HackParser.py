# Parser
# Takes an *.asm file path and unpacks each instruction into its underlying
# fields.

import re

class Commands():
    ''' Read input and build list of valid commands '''
    def __init__(self, file_path):
        self.file_path = file_path
        self.commands = []
 
    def __repr__(self):
        return "path: " + self.file_path

    def get_valid_commands(self):
        ''' Takes *.asm file path and returns a list of valid commands '''
        file = open(self.file_path, 'r')
        
        for line in file.readlines():
            # Ignore white space
            line = line.strip()
            if not line:
                continue # Next iteration of loop
            # Ignore comments (start with `//`)
            if re.search("//", line):
                continue
            # Else valid command
            self.commands.append(line)

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
        elif re.search("(", self):
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
        # Only want first part before = or ;
        destination = re.search("(\w+)[=;]", self).group(1)
        return destination

    def comp(self):
        ''' Gets "computation" field for C-instruction.
        Returns string. '''
        # Only want part after = but before optional ;
        computation = re.search("=([^;]+);*", self)
        
        if computation:
            return computation.group(1)
        else:
            return "null"

    def jmp(self):
        ''' Gets "jump" field for C-instruction.
        Returns string. '''
        # Only want after ; Allows for optional space after semi-colon
        jump = re.search(";\s*(\w+)", self)
        if jump:
            return jump.group(1)
        else:
            return "null"



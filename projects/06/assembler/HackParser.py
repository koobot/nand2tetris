# Constructor for a parser object

import re

class Parser(str: file_path):
    ''' Parser object
    Takes a *.asm file path and unpacks each instruction into its underlying
    fields. '''
    def __init__(self, str: file_path):
        self.file_path = file_path

        # Key attributes
        self.commands = []

        # For iteration
        #self.count = 0

    def __repr__(self):
        return self.file_path
    
    def build(self):
        ''' Reads in assembly file, and generates list of commands '''
        file = open(self.file_name, 'r')
        
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

    def get_fields(self):
        ''' Splits a command into its separate fields '''
        # Split commands into type
        A_instruct = []
        C_instruct = []
        label = []

        for command in self.commands:
            # A-instructions contain @
            if re.search("@", command):
                A_instruct.append(command)
            # C-instructions always contain = or ;
        elif re.search("=|;", command):
            pass
        

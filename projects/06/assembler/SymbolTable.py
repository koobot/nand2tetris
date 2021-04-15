# Manages the Symbol Table
import re

# Predefined symbols
predefined_symbols = {
        "R0": "0",
        "R1": "1",
        "R2": "2",
        "R3": "3",
        "R4": "4",
        "R5": "5",
        "R6": "6",
        "R7": "7",
        "R8": "8",
        "R9": "9",
        "R10": "10",
        "R11": "11",
        "R12": "12",
        "R13": "13",
        "R14": "14",
        "R15": "15",
        "SCREEN": "16384",
        "KBD": "24576",
        "SP": "0",
        "LCL": "1",
        "ARG":"2",
        "THIS": "3",
        "THAT": "4"
        }

class SymbolTable(list):
    ''' Expects a list of valid commands '''
    def __init__(self, *args):
        # Inherits from list
        list.__init__(self, *args)
        # New property
        self.symbol_table = predefined_symbols

    def _add_labels(self) -> None:
        ''' First pass. Modifies in place.
        Add label symbols to symbol table.
        Label symbols format: (XXX)
        Returns nothing '''
        # Initialise line counter
        line_counter = 0

        print("First pass. Adding labels to symbol table.")
        for command in self:
            # if contains ( should be label
            if re.search("\(", command):
                label = re.search("\(([\w\.\$]+)\)", command).group(1)
                address = line_counter
                #print(label, address)
                self.symbol_table[label] = address
                # Don't count labels
            else:
                line_counter += 1

    def _add_variables(self) -> None:
        ''' Second pass. Modifies in place.
        Add variable symboles to symbol table.
        Variable symbol format: @a-zA-Z '''
        # Initalise memory address counter
        mem_addr = 16
        
        print("Second pass. Adding variables to symbol table.")
        for command in self:
            # if variable symbol
            if re.search("@[a-zA-Z]", command):
                var_sym = re.search("@([\w\.\$]+)", command).group(1)
                if var_sym not in self.symbol_table:
                    self.symbol_table[var_sym] = mem_addr
                    mem_addr += 1

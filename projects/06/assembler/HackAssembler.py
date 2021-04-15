import HackParser as hp
import CommandConverter as cc
import SymbolTable as st
import re

def main():
    #ass_files = [
    #        "C:/Users/kooste/Documents/nand2tetris/projects/06/add/Add.asm",
    #        "C:/Users/kooste/Documents/nand2tetris/projects/06/max/MaxL.asm",
    #        "C:/Users/kooste/Documents/nand2tetris/projects/06/rect/RectL.asm",
    #        "C:/Users/kooste/Documents/nand2tetris/projects/06/pong/PongL.asm"
    #        ]

    ass_files = [
            "C:/Users/kooste/Documents/nand2tetris/projects/06/max/Max.asm",
            "C:/Users/kooste/Documents/nand2tetris/projects/06/rect/Rect.asm",
            "C:/Users/kooste/Documents/nand2tetris/projects/06/pong/Pong.asm"
            ]
    for file in ass_files:
        # New file name replaces .asm with .hack
        output_path = re.sub("asm$", "hack", file)
        print(output_path)

        # Read in file
        source = hp.get_valid_commands(file)
        print(source)
        
        # Create symbol table
        symbol_table = st.SymbolTable(source)
        # First pass
        symbol_table._add_labels()
        # Second pass
        symbol_table._add_variables()
        
        print(symbol_table.symbol_table)

        # Convert each command to binary
        binary = []
        for line in source:
            # Get individual command from source
            command = hp.Parser(line)
            
            # Convert to binary
            command_binary = cc.Code(command).convert_to_binary(sym_tab=symbol_table.symbol_table)

            # Append to list
            binary.append(command_binary)

        # Removes empty commands from binary list
        binary = filter(None, binary)

        # Output hack file
        with open(output_path, 'w') as f:
            for l in binary:
                f.writelines(l + "\n")

main()

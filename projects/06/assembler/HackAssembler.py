import HackParser as hp
import CommandConverter as cc
import re

def main():
    ass_files = [
            "C:/Users/kooste/Documents/nand2tetris/projects/06/add/Add.asm",
            "C:/Users/kooste/Documents/nand2tetris/projects/06/max/MaxL.asm",
            "C:/Users/kooste/Documents/nand2tetris/projects/06/rect/RectL.asm",
            "C:/Users/kooste/Documents/nand2tetris/projects/06/pong/PongL.asm"
            ]

    for file in ass_files:
        # New file name replaces .asm with .hack
        output_path = re.sub("asm$", "hack", file)
        print(output_path)

        # Read in file
        source = hp.Commands(file)
        print(source)
        source.get_valid_commands()
        print(source.commands)
    
        # Convert each command to binary
        binary = []
        for line in source.commands:
            # Get individual command from source
            command = hp.Parser(line)
            #print(command)
            #print(command.instruction_type)
            
            # Testing attributes work
            #if command.instruction_type == "C-instruction":
                #print(command.dest())
                #print(command.comp())
                #print(type(command.comp()))
                #print(command.jmp())
            
            # Convert to binary
            command_binary = cc.Code(command).convert_to_binary()
            #print(command_binary)

            # Append to list
            binary.append(command_binary)

        #print(binary)
        # Output hack file
        with open(output_path, 'w') as f:
            for l in binary:
                f.writelines(l + "\n")

main()

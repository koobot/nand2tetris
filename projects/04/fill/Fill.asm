// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

    // Fills and clears row-wise

(PRESS)
    // initialise variables
    @SCREEN
    D=A
    @addr
    M=D     // addr = RAM[16384] (screen's base address)
    @i
    M=0     // i = 0 (index screen memory map at 0 - first word)
    @8191
    D=A     // Note to self: Remember M = 0 so don't assign to M
    @n
    M=D     // n = 8191 (last register/word in screen memory map)

    // Check key press
    @KBD    // key = RAM[24576] (keyboard's base address)
    D=M

    @CLEAR
    D; JEQ  // if key == 0 goto CLEAR
    @FILL
    D; JGT  // if key > 0 goto FILL 

(CLEAR)
    @i
    D=M
    @n
    D=D-M
    @PRESS
    D; JGT  // if i > n, exit loop check for key press

    @addr
    A=M
    M=0     // RAM[addr] = 0x16 (clears the 16px register/word)

    @i
    M=M+1   // i = i + 1
    @addr
    M=M+1   // next register/word in screen memory map
    @CLEAR
    0; JMP  // goto CLEAR

(FILL)
    @i
    D=M
    @n
    D=D-M
    @PRESS
    D; JGT  // if i > n, exit loop check for key press

    @addr
    A=M
    M=-1    // RAM[addr] = 1111111111111111 (blackens the 16px register/word)

    @i
    M=M+1   // i = i + 1
    @addr
    M=M+1   // next register/word in screen memory map
    @FILL
    0; JMP  // goto FILL

(END)
    @END
    0; JMP

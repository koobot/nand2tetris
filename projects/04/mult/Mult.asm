// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

    // x * n = { x + ... + x } n times
    // initialise vars
    @R0
    D=M
    @x  // x = R0
    M=D

    @R1
    D=M
    @n
    M=D // n = R1
    
    @R2
    M=0 // R2 = 0 or else program doesn't work - not sure why STOP isn't sufficient

    @i
    M=0 // i = 0
    @mult
    M=0 // mult = 0

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @STOP
    D; JEQ  // if i == n goto STOP

    @mult
    D=M
    @x
    D=D+M
    @mult
    M=D     // mult = mult + x
    @i
    M=M+1   // i = i + 1
    @LOOP
    0; JMP  // Loop again

(STOP)
    @mult
    D=M
    @R2
    M=D     // RAM[2] = mult

(END)
    @END
    0; JMP


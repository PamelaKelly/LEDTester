# Software Engineering Assignment

Brief Problem Description: 

The Science Centre is installing a new display board which is constructed from LED lights. 
The board is a square grid of LEDs which we control by sending commands to the unit to turn on or off certain
rectangular regions. 

The lights are either on or off. 

The program here should test the lights. We test them by sending instructions to turn on, turn off, or switch
various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a 
rectangle, inclusive; a coordinate pair like 0, 0 through 2, 2 therefore refers to 9 lights in a 3x3 square. 

The program will read a list of instructions from a file and then determine how many lights are on after all
the instructions have been applied. 
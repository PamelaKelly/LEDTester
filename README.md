# assignment3-PamelaKelly

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

I am approaching this project with a Test Driven Development approach - as directed in the project brief. 

Planned Approach: 

Step 1: 
Parse the file and determine the following: 
> Grid Size 
> Lines with Valid Commands

Step 2: 
Store all of the coordinates (as determined by the grid size) in a dictionary where
the value of each key is a boolean representing on (true) or off (false). All lights start off. 

Step 3: 
Parse the commands in such a way that they are easy to pass to a helper function that will execute them. 
Variables could be: 
>Command
>Range of coordinates

Step 4: 
Execute the commands. 

Step 5: 
Check the number of lights that are on or off. Check which specific lights are on or off. 

Notes on design and complexity: 



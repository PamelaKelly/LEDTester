"""This is the set of tests - written in advance of the program 
to test the accuracy and functionality of the lightswitch program"""

import lightswitch

#test 1 - does the program access the file correctly. 

def parse_file_test(file, output):
    try: 
        result = lightswitch.main.parse_file(file)
        if result == output: 
            print("File Handler Test Passed")
        else: 
            print("You have an error in your file handler function")
    except:
        print("You have an error in your file handler function")

#test 2 - does the program correctly identify and implement the grid size.

def create_grid_test(grid, size):
    try: 
        result = lightswitch.main.create_grid()
        if result == grid and result.length() == size: 
            print("Grid Size Test Passed")
        else:
            print("You have an error in your get grid size function")
    except: 
        print("You have an error in your get grid size function")

#test 3 - does the program read commands correctly. 

def parse_command_test(line, command, coordinates):
    try: 
        result = lightswitch.main.parse_command(line)
        if result[0] == command and result[1] == coordinates: 
            print("Command Parsing Test Passed")
        else: 
            print("You have an error in your command parsing function")
    except: 
        print("You have an error in your command parsing function")

#test 4 - does the program implement the commands correctly. 

def execute_command_test(command, coordinates, output):
    try: 
        result = lightswitch.main.execute_command(command, coordinates)
        if result == output: 
            print("Execute Commands Test Passed")
        else: 
            print("You have an error in your execute commands test")
    except: 
        print("You have an error in your execute commands test")


#test 5 - does the program count the number of lights on correctly. 

def count_lights_test(grid, count):
    try: 
        result = lightswitch.main.count_lights(grid)
        if result == count: 
            print("Count Lights Test Passed")
        else: 
            print("You have an error in your count lights test")
    except: 
        print("You have an error in your count lights test")

#test 6 - does the program correctly identify the lights that are on

def check_lights_test(grid, count_on, count_off):
    try: 
        result = lightswitch.main.check_lights(grid)
        if result[0] == count_on and result[1] == count_off:
            print("Lights On Test Passed")
        else: 
            print("You have an error in your check lights test")
    except: 
        print("You have an error in your check lights test")
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

def check_lights_test(grid, list_on, list_off):
    try: 
        result = lightswitch.main.check_lights(grid)
        if result[0] == count_on and result[1] == count_off:
            print("Lights On Test Passed")
        else: 
            print("You have an error in your check lights test")
    except: 
        print("You have an error in your check lights test")

####################################################
#test calls

#parse_file_test()

#sample data
sample_grid = {'0, 0': False, '0, 1': False, '0, 2': False, '0, 3': False, '0, 4': False, 
               '1, 0': False, '1, 1': False, '1, 2': False, '1, 3': False, '1, 4': False,
               '2, 0': False, '2, 1': False, '2, 2': False, '2, 3': False, '2, 4': False, 
               '3, 0': False, '3, 1': False, '3, 2': False, '3, 3': False, '3, 4': False, 
               '4, 0': False, '4, 1': False, '4, 2': False, '4, 3': False, '4, 4': False}
sample_line_1 = "turn on 0, 0 through 3, 3"
sample_coordinates = ('0, 0', '0, 1', '0, 2', '0, 3','1, 0', '1, 1', '1, 2', '1, 3',
                      '2, 0', '2, 1', '2, 2', '2, 3', '3, 0', '3, 1', '3, 2', '3, 3')
sample_grid_33 = {'0, 0': True, '0, 1': True, '0, 2': True, '0, 3': True, '0, 4': False, 
                  '1, 0': True, '1, 1': True, '1, 2': True, '1, 3': True, '1, 4': False,
                  '2, 0': True, '2, 1': True, '2, 2': True, '2, 3': True, '2, 4': False, 
                  '3, 0': True, '3, 1': True, '3, 2': True, '3, 3': True, '3, 4': False, 
                  '4, 0': False, '4, 1': False, '4, 2': False, '4, 3': False, '4, 4': False}
lights_on_sample = ['0, 0', '0, 1', '0, 2', '0, 3', '1, 0', '1, 1', '1, 2', '1, 3', '2, 0', '2, 1', 
                    '2, 2', '2, 3', '3, 0', '3, 1', '3, 2', '3, 3']
lights_off_sample = ['0, 4', '1, 4', '2, 4', '3, 4', '4, 0', '4, 1', '4, 2', '4, 3', '4, 4']

#test calls
#create grid
create_grid_test(sample_grid, 25)
#parse commands
parse_command_test(sample_line_1, "turn on", sample_coordinates)
execute_command_test("turn on", sample_coordinates, sample_grid_33)
count_lights_test(sample_grid_33, 16)
check_lights_test(sample_grid_33, lights_on_sample, lights_off_sample)
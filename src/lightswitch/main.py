from pathlib import Path
import os
def parse_file(file):
    os.chdir('../tests')
    command_list = []
    fh = open(file)
    grid_size = fh.readline().strip()
    while True: 
        line = fh.readline()
        if not line: 
            break
        words = line.split()
        if words[0] + words[1] == "turnon" or words[0] + words[1] == "turnoff" or words[0] == "switch":
            command_list.append(line.strip())
    return command_list, grid_size

def create_grid():
    pass

def parse_command(line):
    pass

def execute_command(command, coordinates):
    pass

def count_lights(grid):
    pass

def check_lights(grid):
    pass


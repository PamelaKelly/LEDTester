import urllib.request, os.path, argparse

def main():
    pass

def count_lights(grid):
    """
    Function to count the number of lights turned
    on in a grid given a grid (dictionary).
    Returns an integer value
    """
    lights_on = 0
    for elem in grid: 
        if grid[elem] == True:
            lights_on += 1
    return lights_on


def check_lights(grid):
    """
    Function to identify which exact lights are turned
    on in a given grid (dictionary). 
    Returns a list of lights that are on and a list
    or lights that are off. 
    """
    #didn't end up using this function but it could be useful if someone wanted
    #to check that the correct lights were on as well as the number of lights
    lights_on = []
    lights_off = []
    for elem in grid: 
        if grid[elem] == True:
            lights_on.append(elem)
        else:
            lights_off.append(elem)
    return lights_on, lights_off

def lightswitch():
    """
    Function that given a file or  using the entry points
    defined in the setup.py file creates a grid to
    represent the grid size given in the file, and executes
    all commands in the file. 
    Returns the name of the file, and the number of lights on.
    """
    #parse command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    file = args.input
    try:
        file_info = validate_file(file)
        file = file_info[0]
        file_type = file_info[1]
        grid_info = parse_file(file, file_type)
        commands_lines, grid_size = grid_info[0], int(grid_info[1])
        start_grid = create_grid(grid_size)
        for line in commands_lines:
            command_full = parse_command(line, grid_size)
            command_key, coordinates = command_full[0], command_full[1]
            grid_updated = execute_command(start_grid, command_key, coordinates)
        num_lights_on = count_lights(grid_updated)
        print(args.input, num_lights_on)
        return args.input, num_lights_on
    except: 
        print("Error - please check inputs and try again")



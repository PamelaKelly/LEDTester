import urllib.request, os.path, argparse

def validate_file(file):
    """
    A function to validate that a given file exists in the local
    directory or that a given url exists and is accessible
    Returns the file (decoded if a url) and the file type
    """
    try:
        #check if file is local or a url
        if file.startswith('http'):
            response = urllib.request.urlopen(file)
            file = response.read().decode("utf-8")
            file_type = 'link'
        else:
            if os.path.isfile(file):
                file = file
                file_type = 'local_file'
            else:
                print("Error: File Not Found - Check that you entered the correct file path")
                return None
        return file, file_type
    except:
        print("Error: Invalid File")

def parse_file(file, file_type):
    """
    A function to parse a given file of a specific format. 
    Returns a grid size (first line in the file) and a list of valid commands
    i.e. commands that are either 'turn on', 'turn off' or 'switch'
    """
    #parse file into lines with valid commands & grid size
    command_list = []
    if file_type == 'local_file':
        fh = open(file)
        grid_size = fh.readline().strip()
    
        while True: 
            line = fh.readline()
            if not line: 
                break
            if ("turn" and "on" in line) or ("turn" and "off" in line) or ("switch" in line):
                command_list.append(line.strip())
    elif file_type == 'link':
        lines = file.split('\n')
        grid_size = lines[0]
        lines.pop(0)
        for line in lines:
            #was throwing an error for the last line which was empty
            if line != "":
                command_list.append(line.strip())
    return command_list, grid_size

def create_grid(grid_size):
    """
    Function that creates a representation of a grid, given the
    grid size, using a dictionary. Keys = coordinates, values =
    True/False (Light is On/Off)
    All values set to False as default
    Returns a dictionary representation of the grid
    """
    #create grid represented using a dictionary
    try:
        grid = {}
        for x in range(grid_size):
            for y in range(grid_size):
                key = (x, y)
                key = str(x) + ", " + str(y)
                grid[key] = False;
        return grid
    except Exception as e: 
        print("Error: Could not complete action due to a ", type(e), " error")

def parse_command(line, grid_size):
    """
    Function to parse a given line. Identifies command 
    and coordinates range of lights. 
    Checks for values outside of the boundaries of 
    the grid, given the grid size.
    Returns a command and a list of coordinates (strings)
    """
    words = line.split()
    #identify command and pull coordinates
    if "turn" and "on" in line:
        command = "turn on"
        xAxis = words[2].split(',')
        yAxis = words[4].split(',')
    elif "turn" and "off" in line:
        command = "turn off"
        xAxis = words[2].split(',')
        yAxis = words[4].split(',')
    elif "switch" in line:
        command = "switch"
        xAxis = words[1].split(',')
        yAxis = words[3].split(',')
    #check for coordinates outside grid boundaries    
    for i in range(len(xAxis)):
        if int(xAxis[i]) < 0:
            xAxis[i] = '0'
        elif int(xAxis[i]) > grid_size - 1:
            xAxis[i] = str(grid_size - 1)
    for i in range(len(yAxis)):
        if int(yAxis[i]) < 0:
            yAxis[i] = '0'
        elif int(yAxis[i]) > grid_size - 1:
            yAxis[i] = str(grid_size - 1)
    #loop through coordinates range - store list of coordinates to be modified
    coordinates = []
    for i in range(int(xAxis[0]), int(yAxis[0]) + 1):
        for j in range(int(xAxis[1]), int(yAxis[1]) + 1):
            coordinates.append(str(i) + ", " + str(j))
    return command, coordinates

def execute_command(start_grid, command, coordinates):
    """
    Function that executes a given command on a given list
    of coordinates in a given grid. Identifies command and 
    completes appropriate action. 
    Returns an updated grid (dictionary) with coordinate values 
    changed to reflect the command. 
    """
    grid = start_grid
    for c in coordinates:
        if command == "turn on":
            grid[c] = True
        elif command == "turn off":
            grid[c] = False
        else:
            if grid[c] == True:
                grid[c] = False
            else:
                grid[c] = True
    return grid

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
    print("We are running the correct version!!")
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



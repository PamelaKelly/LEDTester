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
        if ("turn" and "on" in line) or ("turn" and "off" in line) or ("switch" in line):
            command_list.append(line.strip())
    return command_list, grid_size

def create_grid(grid_size):
    grid = {}
    for i in range(grid_size):
        for j in range(grid_size):
            key = str(i) + ", " + str(j)
            grid[key] = False;
    return grid

def parse_command(line, grid_size):
    words = line.split()
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
    coordinates = []
    for i in range(int(xAxis[0]), int(yAxis[0]) + 1):
        for j in range(int(xAxis[1]), int(yAxis[1]) + 1):
            coordinates.append(str(i) + ", " + str(j))
    return command, coordinates

def execute_command(start_grid, command, coordinates):
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
    #should return a new dictionary with changes made to specific coordinates
    #in the overall program this might need to be a global variable
    return grid

def count_lights(grid):
    lights_on = 0
    for elem in grid: 
        if grid[elem] == True:
            lights_on += 1
    return lights_on

def check_lights(grid):
    lights_on = []
    lights_off = []
    for elem in grid: 
        if grid[elem] == True:
            lights_on.append(elem)
        else:
            lights_off.append(elem)
    return lights_on, lights_off

def lightswitch(file):
    grid_info = parse_file(file)
    commands_lines, grid_size = grid_info[0], int(grid_info[1])
    start_grid = create_grid(grid_size)
    for line in commands_lines:
        command_full = parse_command(line, grid_size)
        command_key, coordinates = command_full[0], command_full[1]
        grid_updated = execute_command(start_grid, command_key, coordinates)
    num_lights_on = count_lights(grid_updated)
    lights_check_detail = check_lights(grid_updated)
    lights_on = lights_check_detail[0]
    lights_off = lights_check_detail[1]
    return grid_updated, num_lights_on, lights_on, lights_off


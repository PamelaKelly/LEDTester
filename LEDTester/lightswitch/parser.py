import re

class Parser():
    
    def __init__(self):
        pass
    
    @staticmethod
    def parse_url(self, url):
        pass
    
    @staticmethod
    def parse_file(self, filepath):
        """
        Function which will parse a given file for grid size and list of commands
        """
        command_list = []
        fh = open(filepath, 'r')
        # get the grid size from the first line
        grid_size = fh.readline().strip()
        
        while True: 
            line = fh.readline()
            if not line: 
                break
            if ("turn" and "on" in line) or ("turn" and "off" in line) or ("switch" in line):
                command_list.append(line.strip())
        
        return command_list, grid_size
    
    @staticmethod
    def parse_command(command):
        instruction = re.findall("([a-zA-Z]+\s([a-zA-z]+)?)", command)[0][0]
        match_coordinates = re.findall("\d,\d", command)
        start_coordinates = [int(match_coordinates[0][0]), int(match_coordinates[0][2])]
        end_coordinates = [int(match_coordinates[1][0]), int(match_coordinates[1][2])]
        
        return instruction, start_coordinates, end_coordinates
    
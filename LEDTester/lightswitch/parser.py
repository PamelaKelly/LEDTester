import re

class Parser():
    """ A class which handles all parsing functionality. """
    
    @staticmethod
    def parse_url(self, url):
        """
        A static function which retrieves the text of a url and parses it for the information
        needed to set up the led grid. 
        
        @type url: string
        @param url: a url link to the location of the data
        
        @rtype: list, integer
        @return: a list of commands and a number defining the grid size. 
        """
        pass
    
    @staticmethod
    def parse_file(self, filepath):
        """
        A static function which parses the text of a given file for the information
        needed to set up the led grid. 
        
        @type filepath: string
        @param filepath: the system path to the file. 
        
        @rtype: list, integer
        @return: a list of lists - each containing a command and a range of 
        lights to be affected - and a number defining the grid size. 
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
                command = Parser.__parse_command(line)
                command_list.append(command)
        
        return command_list, grid_size
    
    @staticmethod
    def __parse_command(command):
        """
        A static function which parses a line of text, extracting only the relevant information
        needed for the command. 
        
        @type command: string
        @param command: A line of text containing a command which needs to be
        parsed for keywords and grid coordinates
        
        @rtype: string, list, list
        @return: a list containing: a string representing the command keyword, two lists, 
        each containing two numbers which represent the start and end of the range of 
        lights to be affected. 
        """
        instruction = re.findall("([a-zA-Z]+\s([a-zA-z]+)?)", command)[0][0]
        match_coordinates = re.findall("\d,\d", command)
        start_coordinates = [int(match_coordinates[0][0]), int(match_coordinates[0][2])]
        end_coordinates = [int(match_coordinates[1][0]), int(match_coordinates[1][2])]
        
        return [instruction, start_coordinates, end_coordinates]
    
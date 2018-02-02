import numpy as np

class LED():
    """ Class to represent an LED grid. """
    
    def __init__(self, grid_size):
        """ 
        Constructor which initialises grid size and creates a multidimensional numpy
        array of zeros based on the size given. 
        
        @type grid_size: integer
        @param grid_size: a number which defines the width and height of a square grid
        """
        self.__grid_size = grid_size
        self.__grid = np.zeros((grid_size, grid_size), dtype = np.int)
        
    def get_grid(self):
        """ 
        Getter for retrieving the grid attribute. 
        
        @rtype: numpy matrix
        @return: the grid attribute representing the led grid
        """
        return self.__grid    
    
    def get_status(self):
        """ 
        Getter for retrieving the number of lights turned on in the grid. 
        
        @rtype: integer
        @return: number of lights that are "on", ie equal to 1. 
        """
        return np.count_nonzero(self.__grid == 1)       
    
    def get_light_status(self, coordinates):
        """
        Getter for retrieving the status of a specific light in the grid. 
        
        @type coordinates: list
        @param coordinates: a list of two numbers representing the 
        location of a given light on the led grid. 
        
        @rtype: integer
        @return: 1 if the light's status is "on", 0 if the light's status is "off"
        """
        return self.__grid[coordinates[0], coordinates[1]]
    
    def __set_light_status(self, action, coordinates):
        """
        Private Function for changing the status of a light on the grid,
         given a command and location for the light.
        
        @type action: string
        @param action: one of three options: "turn on", "turn off", "switch"
        all other variations will be ignored
        @type coordinates: list
        @param coordinates: list of two numbers representing the location 
        of a given light on the led grid. 
        
        @rtype: numpy matrix
        @return: updated grid attribute
        """
        current_status = self.__grid[coordinates[0], coordinates[1]]
        if action == "turn on":
            self.__grid[coordinates[0], coordinates[1]] = 1
        elif action == "turn off":
            self.__grid[coordinates[0], coordinates[1]] = 0
        elif action == "switch":
            if current_status == 0:
                self.__grid[coordinates[0], coordinates[1]] = 1
            else:
                self.__grid[coordinates[0], coordinates[1]] = 0
        return self.__grid
                
    def update_grid(self, command, row, column):
        """
        Function to update the grid across a range of lights given 
        a command, and a boundary for both the row and the 
        column of the grid. .
        
        @type command: string
        @param command: "turn on", "turn off" or "switch" all other 
        variations will be ignored
        @type row: integer
        @param row: end point of range for rows
        @type column: integer
        @param column: end point of range for columns
        
        @rtype: numpy matrix
        @return: updated led grid attribute 
        """
        row_limit, column_limit = self.check_range(row, column)
        for row in range(row_limit):
            for column in range(column_limit):
                LED.__set_light_status(command, (row, column))
        return self.__grid
    
    def check_range(self, end_coordinates):
        """
        Function for checking if the given coordinates are within range
        of the edges of the grid. Resets them to the edge of the grid if they are
        outside of the range. 
        
        @type end_coordinates: list
        @param end_coordinates: a list of two numbers representing the 
        end point for the rows and columns of the matrix.
        
        @rtype: integers
        @return: two integers, the row and column range limit, updated
        if required
        """
        if end_coordinates[0] > self.__grid_size -1:
            row_limit = self.__grid_size 
        else: 
            row_limit = end_coordinates[0] + 1
        if end_coordinates[1] > self.__grid_size -1:
            column_limit = self.__grid_size
        else:
            column_limit = end_coordinates[1] + 1
        return row_limit, column_limit

    
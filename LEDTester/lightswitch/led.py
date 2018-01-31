import numpy as np
from numpy import *

class LED():
    
    def __init__(self, grid_size):
        self.__grid_size = grid_size
        self.__grid = np.zeros((grid_size, grid_size), dtype = np.int)
        self.__lights_on = 0
        self.__lights_off = 0 # initialise as number of lights in the grid
        
    def get_grid(self):
        return self.__grid    
    
    def get_status(self):
        return np.count_nonzero(self.__grid == 1)       
    
    def get_light_status(self, coordinates):
        return self.__grid[coordinates[0], coordinates[1]]
    
    def set_light_status(self, action, coordinate):
        current_status = self.__grid[coordinate[0], coordinate[1]]
        if action == "turn on":
            self.__grid[coordinate[0], coordinate[1]] = 1
        elif action == "turn off":
            self.__grid[coordinate[0], coordinate[1]] = 0
        elif action == "switch":
            if current_status == 0:
                self.__grid[coordinate[0], coordinate[1]] = 1
            else:
                self.__grid[coordinate[0], coordinate[1]] = 0
                
    def update_grid(self, command, start, end):
        row_limit, column_limit = self.check_range(start, end)
        for row in range(row_limit):
            for column in range(column_limit):
                self.set_light_status(command, (row, column))
        return self.__grid
    
    def check_range(self, start_coordinates, end_coordinates):
        if end_coordinates[0] > self.__grid_size -1:
            row_limit = self.__grid_size 
        else: 
            row_limit = end_coordinates[0] + 1
        if end_coordinates[1] > self.__grid_size -1:
            column_limit = self.__grid_size
        else:
            column_limit = end_coordinates[1] + 1
        return row_limit, column_limit

    
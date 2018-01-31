class LED():
    
    def __init__(self):
        self.__grid_size = 0
        self.__grid = []
        self.__lights_on = 0
        self.__lights_off = 0 # initialise as number of lights in the grid
        
    def get_grid(self):
        return self.__grid    
    
    def get_status(self):
        pass
    
    def get_light_status(self):
        pass
    
    def set_light_status(self):
        pass
    
    @staticmethod
    def check_range(self, start_coordinates, end_coordinates):
        lower_bound, upper_bound = 0, self.__grid_size - 1
        # check x of start
        if start_coordinates[0] < lower_bound:
            start_coordinates[0] = lower_bound
        elif  start_coordinates[0] > upper_bound:
            start_coordinates[0] = upper_bound
        # check y of start     
        if start_coordinates[1] < lower_bound:
            start_coordinates[1] = lower_bound
        elif start_coordinates[1] > upper_bound:
            start_coordinates[1] = upper_bound
        # check x of end    
        if end_coordinates[0] < lower_bound: 
            end_coordinates[0] = lower_bound
        elif end_coordinates[0] > upper_bound:
            end_coordinates[0] = upper_bound
        # check y of end
        if end_coordinates[1] < lower_bound:
            end_coordinates[1] = lower_bound
        elif end_coordinates[1] > upper_bound:
            end_coordinates[1] = upper_bound
            
        return start_coordinates, end_coordinates
        """ Checks that a set of given coordinates are within the boundaries of the grid """
                #check for coordinates outside grid boundaries    
        """       
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
    """
        pass
    
    
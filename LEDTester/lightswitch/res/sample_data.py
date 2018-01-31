#sample data
sample_grid_size = '5'
sample_commands_list = ['turn on 0,0 through 4,4', 'turn off 0,0 through 4,4', 'turn on 0,0 through 2,2', 
                        'switch 0,0 through 4,4', 'turn off 2,2 through 15,15', 'turn on 0,0 through 4,4',
                        'turn off -10,-10 through 3,3']
sample_file = 'file1.txt'
sample_grid = {'0, 0': False, '0, 1': False, '0, 2': False, '0, 3': False, '0, 4': False, 
               '1, 0': False, '1, 1': False, '1, 2': False, '1, 3': False, '1, 4': False,
               '2, 0': False, '2, 1': False, '2, 2': False, '2, 3': False, '2, 4': False, 
               '3, 0': False, '3, 1': False, '3, 2': False, '3, 3': False, '3, 4': False, 
               '4, 0': False, '4, 1': False, '4, 2': False, '4, 3': False, '4, 4': False}
sample_line_1 = "turn on 0,0 through 3,3"
sample_coordinates = ['0, 0', '0, 1', '0, 2', '0, 3','1, 0', '1, 1', '1, 2', '1, 3',
                      '2, 0', '2, 1', '2, 2', '2, 3', '3, 0', '3, 1', '3, 2', '3, 3']
sample_grid_33 = {'0, 0': True, '0, 1': True, '0, 2': True, '0, 3': True, '0, 4': False, 
                  '1, 0': True, '1, 1': True, '1, 2': True, '1, 3': True, '1, 4': False,
                  '2, 0': True, '2, 1': True, '2, 2': True, '2, 3': True, '2, 4': False, 
                  '3, 0': True, '3, 1': True, '3, 2': True, '3, 3': True, '3, 4': False, 
                  '4, 0': False, '4, 1': False, '4, 2': False, '4, 3': False, '4, 4': False}
lights_on_sample = ['0, 0', '0, 1', '0, 2', '0, 3', '1, 0', '1, 1', '1, 2', '1, 3', '2, 0', '2, 1', 
                    '2, 2', '2, 3', '3, 0', '3, 1', '3, 2', '3, 3']
lights_off_sample = ['0, 4', '1, 4', '2, 4', '3, 4', '4, 0', '4, 1', '4, 2', '4, 3', '4, 4']

#sample results for file1.txt
sample_grid_updated = {'0, 0': False, '0, 1': False, '0, 2': False, '0, 3': False, '0, 4': True, 
                       '1, 0': False, '1, 1': False, '1, 2': False, '1, 3': False, '1, 4': True,
                       '2, 0': False, '2, 1': False, '2, 2': False, '2, 3': False, '2, 4': True, 
                       '3, 0': False, '3, 1': False, '3, 2': False, '3, 3': False, '3, 4': True, 
                       '4, 0': True, '4, 1': True, '4, 2': True, '4, 3': True, '4, 4': True}
sample_num_lights_on = 9
sample_file2 = "input_assign3.txt"
sample_num_2 = 400410

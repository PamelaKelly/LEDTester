import urllib.request, os.path, argparse
from led import LED
from parser import Parser

def main():
    """ Top level function which runs the program. """
    #parse command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    file = args.input
    # parse file
    commands, grid_size = Parser.parse_file(file)    
    # create led board
    led = LED(grid_size)
    # run commands
    for command in commands:
        led.update_grid(command)
        print(led.get_grid())
        

main()
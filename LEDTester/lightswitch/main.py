import urllib.request, os.path, argparse

def main():
    """ Top level function which runs the program. """
    #parse command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    file = args.input
    
    # TODO: parse file
    
    # TODO: Create LED Board
    
    # TODO: Run series of commands from file



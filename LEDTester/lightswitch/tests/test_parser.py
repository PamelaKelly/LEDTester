import unittest
from lightswitch.parser import Parser

class TestParser(unittest.TestCase):
    """ Test class for testing the Parser class. """
    
    def setUp(self):
        self.__test_commands = [
            ["turn on", [0,0], [4,4]],
            ["turn off", [0,0], [4,4]],
            ["turn on", [0,0], [2,2]],
            ["switch", [0,0], [4,4]],
            ["turn off", [2,2], [15,15]],
            ["turn on", [0,0], [4,4]],
            ["turn off", [-10,-10], [3,3]]
            ]
              
    def test_parse_url(self):
        """
        Assert that parse_url function returns correct output 
        
        Verification:
        1. Verify that parse_url returns the correct list of commands from the given test source.
        2. Verify that parse_url returns the correct grid size form the given test source.
        """
        self.assertEqual(Parser.parse_url("res/file1.txt"), [self.__test_commands, 5])
    
    def test_parse_file(self):
        """
        Assert that parse_file returns correct output
        
        Verification:
        1. Verify that parse_file returns the correct list of commands from the given test source.
        2. Verify that parse_file returns the correct grid size from the given test source.
        """
        self.assertEqual(Parser.parse_file("res/file1.txt"), [self.__test_commands, 5])
        
        
        
        
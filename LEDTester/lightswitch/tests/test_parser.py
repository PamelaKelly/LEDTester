import unittest
from lightswitch.parser import Parser
from astropy.time.tests.test_precision import test_leap_seconds_rounded_correctly

class TestParser(unittest.TestCase):
    """ Test class for testing the Parser class. """
    
    def setUp(self):
        self.__parser = Parser()
        self.__test_commands = ['turn on 0,0 through 4,4', 'turn off 0,0 through 4,4', 'turn on 0,0 through 2,2', 
                        'switch 0,0 through 4,4', 'turn off 2,2 through 15,15', 'turn on 0,0 through 4,4',
                        'turn off -10,-10 through 3,3']
        
    def test_parse_url(self):
        """
        Assert that parse_url function returns correct output 
        
        Verification:
        1. Verify that parse_url returns the correct list of commands from the given test source.
        2. Verify that parse_url returns the correct grid size form the given test source.
        """
        self.assertEqual(self.__parser.parse_url("#"), [self.__test_commands, 5])
    
    def test_parse_file(self):
        """
        Assert that parse_file returns correct output
        
        Verification:
        1. Verify that parse_file returns the correct list of commands from the given test source.
        2. Verify that parse_file returns the correct grid size from the given test source.
        """
        self.assertEqual(self.__parser.parse_file("#"), [self.__test_commands, 5])
        
        
    def test_parse_command(self):
        """
        Assert that parse_command returns the correct instructions for the LED board. 
        
        Verification: 
        1. Verify that parse_command parses "turn on" commands correctly.
        2. Verify that parse_command parse "turn on" commands correctly. 
        3. Verify that parse_command parses "switch" commands correctly. 
        4. Verify that parse_command ignores lines it should. 
        """
        self.assertEqual(self.__parser.parse_command("turn on 0,0 through 4,4"), ["turn on"], [(0,0), (4,4)])
        self.assertEqual(self.__parser.parse_command("turn off 0,0 through 4,4"), ["turn off"], [(0,0), (4,4)])
        self.assertEqual(self.__parser.parse_command("switch 0,0 through 4,4"), ["switch"], [(0,0), (4,4)])
        
        
        
        
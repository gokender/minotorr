import unittest

from minotor import ram
from tests import data_testing

class TestRam(unittest.TestCase):
    """Tests for `ram` package."""

    def setUp(self):
        """Set up test fixtures"""
        self.ram = ram.RAM(data_testing.CPU_DATA)

    def test_001_ram_data(self):
        """Test if it's the right hardware component"""
        self.assertEqual(self.ram.parsed_data['ImageURL'], 'images_icon/ram.png')

    def test_002_loads_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.ram.loads, {})

    def test_003_data_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.ram.data, {})

    def test_004_loads_structure(self):
        """Test the loads structure"""
        #print(type(self.cpu.clocks))
        self.assertIn('memory', self.ram.loads)
        self.assertIn('virtual_memory', self.ram.loads)

    def test_005_data_structure(self):
        """Test the data structure"""
        #print(type(self.cpu.clocks))
        self.assertIn('memory_used', self.ram.data)
        self.assertIn('memory_available', self.ram.data)
        self.assertIn('virtual_memory_used', self.ram.data)
        self.assertIn('virtual_memory_available', self.ram.data)

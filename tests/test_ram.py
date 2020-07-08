import unittest

from minotorr import ram
from tests import data_testing

class TestRam(unittest.TestCase):
    """Tests for `ram` package."""

    def setUp(self):
        """Set up test fixtures"""
        self.ram = ram.RAM(data_testing.CPU_DATA)

    def test_ram_data(self):
        """Test if it's the right hardware component"""
        self.assertEqual(self.ram.parsed_data['ImageURL'], 'images_icon/ram.png')

    def test_load_memory(self):
        """Test the load memory"""
        self.assertEqual(self.ram.load.memory, 82.9)
    
    def test_load_virtual_memory(self):
        """Test the load virtual_memory"""
        self.assertEqual(self.ram.load.virtual_memory, 85.7)

    def test_load_dict(self):
        """Test the load dict structure"""
        self.assertEqual(self.ram.load.to_dict()['memory'], self.ram.load.memory)

    def test_data_memory_used(self):
        """Test the data memory_used"""
        self.assertEqual(self.ram.data.memory_used, 6.5)
    
    def test_data_memory_available(self):
        """Test the data memory_available"""
        self.assertEqual(self.ram.data.memory_available, 1.3)
    
    def test_data_virtual_memory_used(self):
        """Test the data virtual_memory_used"""
        self.assertEqual(self.ram.data.virtual_memory_used, 13.2)
    
    def test_data_virtual_memory_available(self):
        """Test the data virtual_memory_available"""
        self.assertEqual(self.ram.data.virtual_memory_available, 2.2)
    
    def test_data_dict(self):
        """Test the data dict structure"""
        self.assertEqual(self.ram.data.to_dict()['memory_used'], self.ram.data.memory_used)
import unittest

from minotorr import cpu
from tests import data_testing

class TestCPU(unittest.TestCase):
    """Tests for `cpu` package."""

    def setUp(self):
        
        """Set up test fixtures"""
        self.cpu = cpu.CPU(data_testing.CPU_DATA)

    def test_001_cpu_name(self):
        """Test the name of the CPU"""
        self.assertEqual(self.cpu.name, 'Intel Core i5-4590')

    def test_002_cpu_data(self):
        """Test if it's the right hardware component"""
        self.assertEqual(self.cpu.parsed_data['ImageURL'], 'images_icon/cpu.png')

    def test_003_cpu_cores(self):
        """Test the number of cores"""
        self.assertEqual(self.cpu.cores, 4)

    def test_004_clocks_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu.clocks, {})

    def test_005_temperatures_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu.temperatures, {})

    def test_006_loads_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu.loads, {})

    def test_007_powers_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu.powers, {})

    def test_008_clocks_structure(self):
        """Test the clocks structure"""
        #print(type(self.cpu.clocks))
        self.assertIn('bus_speed', self.cpu.clocks)
        self.assertIn('1', self.cpu.clocks)

    def test_009_temperatures_structure(self):
        """Test the temperatures structure"""
        #print(type(self.cpu.clocks))
        self.assertIn('cpu_package', self.cpu.temperatures)
        self.assertIn('1', self.cpu.temperatures)

    def test_010_loads_structure(self):
        """Test the loads structure"""
        #print(type(self.cpu.clocks))
        self.assertIn('cpu_total', self.cpu.loads)
        self.assertIn('1', self.cpu.loads)

    def test_011_powers_structure(self):
        """Test the powers structure"""
        #print(type(self.cpu.clocks))
        self.assertIn('cpu_package', self.cpu.powers)
        self.assertIn('cpu_cores', self.cpu.powers)
        self.assertIn('cpu_graphics', self.cpu.powers)
        self.assertIn('cpu_memory', self.cpu.powers)

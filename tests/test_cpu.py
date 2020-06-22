import unittest

from minotor import cpu
from tests import data_testing

class TestCPU(unittest.TestCase):
    """Tests for `cpu` package."""

    def setUp(self):
        
        """Set up test fixtures"""
        self.cpu_obj = cpu.CPU(data_testing.CPU_DATA, 1592483676)

    def test_001_cpu_name(self):
        """Test the name of the CPU"""
        self.assertEqual(self.cpu_obj.name, 'Intel Core i5-4590')

    def test_002_cpu_data(self):
        """Test if it's the right hardware component"""
        self.assertEqual(self.cpu_obj.parsed_data['ImageURL'], 'images_icon/cpu.png')

    def test_003_cpu_cores(self):
        """Test the number of cores"""
        self.assertEqual(self.cpu_obj.cores, 4)

    def test_004_clocks_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu_obj.clocks, {})

    def test_005_temperatures_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu_obj.temperatures, {})

    def test_006_loads_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu_obj.loads, {})

    def test_007_powers_parsed(self):
        """Test if not empty""" #TODO : change doc
        self.assertNotEqual(self.cpu_obj.powers, {})

    def test_008_clocks_structure(self):
        """Test the clocks structure"""
        #print(type(self.cpu_obj.clocks))
        self.assertIn('bus_speed', self.cpu_obj.clocks)
        self.assertIn('1', self.cpu_obj.clocks)

    def test_009_temperatures_structure(self):
        """Test the temperatures structure"""
        #print(type(self.cpu_obj.clocks))
        self.assertIn('cpu_package', self.cpu_obj.temperatures)
        self.assertIn('1', self.cpu_obj.temperatures)

    def test_010_loads_structure(self):
        """Test the loads structure"""
        #print(type(self.cpu_obj.clocks))
        self.assertIn('cpu_total', self.cpu_obj.loads)
        self.assertIn('1', self.cpu_obj.loads)

    def test_011_powers_structure(self):
        """Test the powers structure"""
        #print(type(self.cpu_obj.clocks))
        self.assertIn('cpu_package', self.cpu_obj.powers)
        self.assertIn('cpu_cores', self.cpu_obj.powers)
        self.assertIn('cpu_graphics', self.cpu_obj.powers)
        self.assertIn('cpu_dram', self.cpu_obj.powers)

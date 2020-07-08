import unittest

from minotorr import cpu
from tests import data_testing

class TestCPU(unittest.TestCase):
    """Tests for `cpu` package."""
    def setUp(self):
        
        """Set up test fixtures"""
        self.cpu = cpu.CPU(data_testing.CPU_DATA)

    def test_cpu_name(self):
        """Test the name of the CPU"""
        self.assertEqual(self.cpu.name, 'Intel Core i5-4590')

    def test_cpu_data(self):
        """Test if it's the right hardware component"""
        self.assertEqual(self.cpu.parsed_data['ImageURL'], 'images_icon/cpu.png')

    def test_cpu_cores(self):
        """Test the number of cores"""
        self.assertEqual(self.cpu.cores, 4)

    def test_clock_speed(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.clock.speed, 100.0)
    
    def test_clock_cores(self):
        """Test the first core speed"""
        self.assertEqual(self.cpu.clock.cores[0], 3500.0)
    
    def test_clock_dict(self):
        """Test the clock dict structure"""
        self.assertEqual(self.cpu.clock.to_dict()['0'], self.cpu.clock.cores[0])

    def test_temperature_package(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.temperature.package, 47.0)
    
    def test_temperature_max(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.temperature.max, 47.0)
    
    def test_temperature_average(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.temperature.average, 46.3)
    
    def test_temperature_cores(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.temperature.cores[0], 46.0)
    
    def test_temperature_dict(self):
        """Test the clock dict structure"""
        self.assertEqual(self.cpu.temperature.to_dict()['0'], self.cpu.temperature.cores[0])

    def test_load_total(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.load.total, 42.2)
    
    def test_load_cores(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.load.cores[0], 39.1)
    
    def test_load_dict(self):
        """Test the clock dict structure"""
        self.assertEqual(self.cpu.load.to_dict()['0'], self.cpu.load.cores[0])

    def test_power_package(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.power.package, 28.5)
    
    def test_power_cores(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.power.cores, 18.3)
    
    def test_power_graphics(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.power.graphics, 0.0)
    
    def test_power_memory(self):
        """Test the bus speed"""
        self.assertEqual(self.cpu.power.memory, 2.6)
    
    def test_power_dict(self):
        """Test the clock dict structure"""
        self.assertEqual(self.cpu.power.to_dict()['cpu_package'], self.cpu.power.package)
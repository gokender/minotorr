import unittest

from minotorr import gpu
from tests import data_testing

class TestCPU(unittest.TestCase):
    """Tests for `gpu` package."""
    def setUp(self):
        
        """Set up test fixtures"""
        self.gpu = gpu.GPU(data_testing.CPU_DATA)

    def test_gpu_name(self):
        """Test the name of the CPU"""
        self.assertEqual(self.gpu.name, 'NVIDIA GeForce GTX 950')

    def test_gpu_data(self):
        """Test if it's the right hardware component"""
        self.assertEqual(self.gpu.parsed_data['ImageURL'], 'images_icon/nvidia.png')

    def test_clock_core(self):
        """Test the clock core"""
        self.assertEqual(self.gpu.clock.core, 721.4)
    
    def test_clock_memory(self):
        """Test the clock memory"""
        self.assertEqual(self.gpu.clock.memory, 810.0)
    
    def test_clock_shader(self):
        """Test the first clock shader"""
        self.assertEqual(self.gpu.clock.shader, 1442.8)
    
    def test_clock_dict(self):
        """Test the clock dict structure"""
        self.assertEqual(self.gpu.clock.to_dict()['core'], self.gpu.clock.core)

    def test_temperature_core(self):
        """Test the temperature core"""
        self.assertEqual(self.gpu.temperature.core, 44.0)
    
    def test_temperature_dict(self):
        """Test the temperature dict structure"""
        self.assertEqual(self.gpu.temperature.to_dict()['core'], self.gpu.temperature.core)

    def test_load_core(self):
        """Test the load core"""
        self.assertEqual(self.gpu.load.core, 14.0)
    
    def test_load_memory_controller(self):
        """Test the load memory controller"""
        self.assertEqual(self.gpu.load.memory_controller, 20.0)
    
    def test_load_video_engine(self):
        """Test the load video engine"""
        self.assertEqual(self.gpu.load.video_engine, 26.0)
    
    def test_load_memory(self):
        """Test the load memory"""
        self.assertEqual(self.gpu.load.memory, 43.0)
    
    def test_load_bus(self):
        """Test the load bus"""
        self.assertEqual(self.gpu.load.bus, 0.0)
    
    def test_load_dict(self):
        """Test the load dict structure"""
        self.assertEqual(self.gpu.load.to_dict()['core'], self.gpu.load.core)

    def test_power_package(self):
        """Test the power package"""
        self.assertEqual(self.gpu.power.package, 13.9)
    
    def test_power_dict(self):
        """Test the power dict structure"""
        self.assertEqual(self.gpu.power.to_dict()['package'], self.gpu.power.package)
    
    def test_data_memory_free(self):
        """Test the data memory free"""
        self.assertEqual(self.gpu.data.memory_free, 1167.3)
    
    def test_data_memory_used(self):
        """Test the data memory used"""
        self.assertEqual(self.gpu.data.memory_used, 880.7)

    def test_data_memory_total(self):
        """Test the data memory total"""
        self.assertEqual(self.gpu.data.memory_total, 2048.0)
    
    def test_data_dict(self):
        """Test the data dict structure"""
        self.assertEqual(self.gpu.data.to_dict()['memory_free'], self.gpu.data.memory_free)
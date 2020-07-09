"""GPU component module"""

class _Clock:
    """Private class for creating a Clock object.

    Provides GPU Clock informations from Libre Hardware Monitor webserver.

    :param memory (float):
    :param core (float):
    :param shader (float):
    :param unit (str):
    """

    def __init__(self, memory=0.0, core=0.0, shader=0.0, unit='MHz'):
        self.core = core
        self.memory = memory
        self.shader = shader
        self.unit = unit

    def parse(self, data):
        """Get GPU/Clock subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' MHz').replace(',', '.'))

            if core['Text'] == 'GPU Core':
                self.core = value
            elif core['Text'] == 'GPU Memory':
                self.memory = value
            elif core['Text'] == 'GPU Shader':
                self.shader = value

    def to_dict(self):
        """Transform the _Clock object to dict
        :rtype: dict
        """
        data = {}

        data['core'] = self.core
        data['memory'] = self.memory
        data['shader'] = self.shader

        data['unit'] = self.unit
   
        return data


class _Temperature:
    """Private class for creating a Temperature object.

    Provides GPU Temperature informations from Libre Hardware Monitor webserver.

    :param core (float):
    :param unit (str):
    """

    def __init__(self, core=0.0, unit='°C'):
        self.core = core
        self.unit = unit

    def parse(self, data):
        """Get GPU/Temperature subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' °C').replace(',', '.'))

            if core['Text'] == 'GPU Core':
                self.core = value

    def to_dict(self):
        """Transform the _Temperature object to dict
        :rtype: dict
        """
        data = {}

        data['core'] = self.core
        data['unit'] = self.unit
   
        return data

class _Load:
    """Private class for creating a Load object.

    Provides GPU Load informations from Libre Hardware Monitor webserver.

    :param core (float):
    :param memory_controller (float):
    :param video_engine (float):
    :param memory (float):
    :param bus (float):
    :param unit (str):
    """
    def __init__(self, core=0.0, memory_controller=0.0, video_engine=0.0, memory=0.0, bus=0.0, unit='%'):

        self.core = core
        self.memory_controller = memory_controller
        self.video_engine = video_engine
        self.memory = memory
        self.bus = bus

        self.unit = unit

    def parse(self, data):
        """Get GPU/Load subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' %').replace(',', '.'))
            if core['Text'] == 'GPU Core':
                self.core = value
            elif core['Text'] == 'GPU Memory Controller':
                self.memory_controller = value
            elif core['Text'] == 'GPU Video Engine':
                self.video_engine = value
            elif core['Text'] == 'GPU Memory':
                self.memory = value
            elif core['Text'] == 'GPU Bus':
                self.bus = value

    def to_dict(self):
        """Transform the _Load object to dict
        :rtype: dict
        """
        data = {}

        data['core'] = self.core
        data['memory_controller'] = self.memory_controller
        data['video_engine'] = self.video_engine
        data['memory'] = self.memory
        data['bus'] = self.bus

        data['unit'] = self.unit
   
        return data

class _Power:
    """Private class for creating a Power object.

    Provides GPU Power informations from Libre Hardware Monitor webserver.

    :param package (float):
    :param unit (str):
    """

    def __init__(self, package=0.0, unit='W'):

        self.package = package
        self.unit = unit

    def parse(self, data):
        """Get GPU/Power subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' W').replace(',', '.'))

            if core['Text'] == 'GPU Package':
                self.package = value

    def to_dict(self):
        """Transform the _Power object to dict
        :rtype: dict
        """
        data = {}

        data['package'] = self.package
        data['unit'] = self.unit
   
        return data

class _Data:
    """Private class for creating a Data object.

    Provides GPU Data informations from Libre Hardware Monitor webserver.

    :param memory_free (float):
    :param memory_used (float):
    :param memory_total (float):
    :param unit (str):
    """
    def __init__(self, memory_free=0.0, memory_used=0.0, memory_total=0.0, unit='MB'):

        self.memory_free = memory_free
        self.memory_used = memory_used
        self.memory_total = memory_total
        self.unit = unit

    def parse(self, data):
        """Get RAM/Data subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' MB').replace(',', '.'))
            if core['Text'] == 'GPU Memory Free':
                self.memory_free = value
            elif core['Text'] == 'GPU Memory Used':
                self.memory_used = value
            elif core['Text'] == 'GPU Memory Total':
                self.memory_total = value

    def to_dict(self):
        """Transform the _Data object to dict
        :rtype: dict
        """
        data = {}

        data['memory_free'] = self.memory_free
        data['memory_used'] = self.memory_used
        data['memory_total'] = self.memory_total
        
        data['unit'] = self.unit
   
        return data

class GPU:
    """Class for creating a GPU object.

    Provides GPU informations from Libre Hardware Monitor webserver.

    Basic Usage::

      >>> from minotorr import gpu
      >>> gpu_ob = gpu.GPU(data) # data is the response from HTTP requests
      >>> gpu_ob.name
      NVIDIA GeForce GTX 950
      >>> gpu_obj.clock
      <minotorr.gpu._Clock>
      >>> gpu_obj.load
      <minotorr.gpu._Load>
      >>> gpu_obj.power
      <minotorr.gpu._Power>
      >>> gpu_obj.temperature
      <minotorr.gpu._Temperature>
      >>> gpu_obj.data
      <minotorr.gpu._Data>
    """
    def __init__(self, data):

        self.parsed_data = {}

        self.name = ''

        self.clock = _Clock()
        self.load = _Load()
        self.power = _Power()
        self.temperature = _Temperature()
        self.data = _Data()

        self.update(data)

    def parse(self):
        """Get GPU subtree from data dictionnary"""
        for component in self.raw_data['Children'][0]['Children']:
            if component['ImageURL'] == 'images_icon/nvidia.png':
                self.parsed_data = component

    def parse_name(self):
        """Get GPU name"""
        self.name = self.parsed_data['Text']

    def parse_clock(self):
        """Get clocks informations from GPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Clocks':
                self.clock.parse(category['Children'])

    def parse_temperature(self):
        """Get temperature informations from GPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Temperatures':
                self.temperature.parse(category['Children'])

    def parse_load(self):
        """Get load informations from GPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Load':
                self.load.parse(category['Children'])

    def parse_power(self):
        """Get power informations from GPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Powers':
                self.power.parse(category['Children'])
    
    def parse_data(self):
        """Get data informations from GPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Data':
                self.data.parse(category['Children'])
            
    def to_dict(self):
        """Transform the GPU object to dict
        :rtype: dict
        """
        gpu = {}
        gpu['name'] = self.name
        gpu['clock'] = self.clock.to_dict()
        gpu['temperature'] = self.temperature.to_dict()
        gpu['load'] = self.load.to_dict()
        gpu['power'] = self.power.to_dict()
        gpu['data'] = self.data.to_dict()

        return gpu

    def update(self, data):
        """Update GPU Object with new data
        :param data: Response in JSON from HTTP webserver
        """

        self.raw_data = data

        self.parse()
        self.parse_name()
        self.parse_clock()
        self.parse_temperature()
        self.parse_load()
        self.parse_power()
        self.parse_data()
        
"""Ram component module"""

class _Load:
    """Private class for creating a Load object.

    Provides RAM Load informations from Libre Hardware Monitor webserver.

    :param memory (float):
    :param virtual_memory (float):
    :param unit (str):
    """
    def __init__(self, memory=0.0, virtual_memory=0.0, unit='%'):

        self.memory = memory
        self.virtual_memory = virtual_memory
        self.unit = unit

    def parse(self, data):
        """Get RAM/Load subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' %').replace(',', '.'))
            if core['Text'] == 'Memory':
                self.memory = value
            elif core['Text'] == 'Virtual Memory':
                self.virtual_memory = value

    def to_dict(self):
        """Transform the _Load object to dict
        :rtype: dict
        """
        data = {}

        data['memory'] = self.memory
        data['virtual_memory'] = self.virtual_memory
        
        data['unit'] = self.unit
   
        return data

class _Data:
    """Private class for creating a Data object.

    Provides RAM Data informations from Libre Hardware Monitor webserver.

    :param memory_used (float):
    :param virtual_memory (float):
    :param virtual_memory_used (float):
    :param virtual_memory_available (float):
    :param unit (str):
    """
    def __init__(self, memory_used=0.0, 
                       memory_available=0.0,
                       virtual_memory_used=0.0,
                       virtual_memory_available=0.0,
                       unit='GB'):

        self.memory_used = memory_used
        self.memory_available = memory_available
        self.virtual_memory_used = virtual_memory_used
        self.virtual_memory_available = virtual_memory_available
        self.unit = unit

    def parse(self, data):
        """Get RAM/Data subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' GB').replace(',', '.'))
            if core['Text'] == 'Memory Used':
                self.memory_used = value
            elif core['Text'] == 'Memory Available':
                self.memory_available = value
            elif core['Text'] == 'Virtual Memory Used':
                self.virtual_memory_used = value
            elif core['Text'] == 'Virtual Memory Available':
                self.virtual_memory_available = value

    def to_dict(self):
        """Transform the _Data object to dict
        :rtype: dict
        """
        data = {}

        data['memory_used'] = self.memory_used
        data['memory_available'] = self.memory_available
        data['virtual_memory_used'] = self.virtual_memory_used
        data['virtual_memory_available'] = self.virtual_memory_available
        
        data['unit'] = self.unit
   
        return data

class RAM:
    """Class for creating a RAM object.

    Provides RAM informations from Libre Hardware Monitor webserver.

    Basic Usage::

      >>> from minotorr import ram
      >>> ram_ob = ram.RAM(data) # data is the response from HTTP requests
      >>> ram_ob.load
      <minotorr.ram._Load>
      >>> ram_ob.data
      <minotorr.ram._Data>
    """

    def __init__(self, data):

        self.parsed_data = {}
        
        self.data = _Data()
        self.load = _Load()

        self.update(data)

    def parse(self):
        """Get RAM subtree from data dictionnary"""
        for component in self.raw_data['Children'][0]['Children']:
            if component['ImageURL'] == 'images_icon/ram.png':
                self.parsed_data = component

    def parse_load(self):
        """Get load informations from RAM"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Load':
                self.load.parse(category['Children'])

    def parse_data(self):
        """Get data informations from RAM"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Data':
                self.data.parse(category['Children'])

    def to_dict(self):
        """Transform the RAM object to dict
        :rtype: dict
        """
        ram = {}
        ram['load'] = self.load.to_dict()
        ram['data'] = self.data.to_dict()

        return ram

    def update(self, data):
        """Update RAM Object with new data
        :param data: Response in JSON from HTTP webserver
        """
        self.raw_data = data
        self.parse()
        self.parse_load()
        self.parse_data()
        
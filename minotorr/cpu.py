"""CPU component module"""

class _Clock:
    """Private class for creating a Clock object.

    Provides CPU Clock informations from Libre Hardware Monitor webserver.

    :param speed (float):
    :param cores (list->float):
    :param unit (str):
    """

    def __init__(self, speed=0.0, cores=[], unit='MHz'):
        self.cores = cores
        self.speed = speed
        self.unit = unit

    def parse(self, data):
        """Get CPU/Clock subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' MHz').replace(',', '.'))

            if core['Text'] == 'Bus Speed':
                self.speed = value
            else:
                self.cores.append(value)

    def to_dict(self):
        """Transform the _Clock object to dict
        :rtype: dict
        """
        data = {}

        data['bus_speed'] = self.speed

        cpt = 0
        for core in self.cores:
            data[str(cpt)] = core
            cpt += 1

        data['unit'] = self.unit
   
        return data


class _Temperature:
    """Private class for creating a Temperature object.

    Provides CPU Temperature informations from Libre Hardware Monitor webserver.

    :param package (float):
    :param cores (list->float):
    :param max (float):
    :param average (float):
    :param unit (str):
    """

    def __init__(self, package=0.0, cores=[], cmax=0.0, average=0.0, unit='°C'):
        self.cores = cores
        self.package = package
        self.max = cmax
        self.average = average
        self.unit = unit

    def parse(self, data):
        """Get CPU/Temperature subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' °C').replace(',', '.'))

            if core['Text'] == 'CPU Package':
                self.package = value
            elif core['Text'] == 'Core Max':
                self.max = value
            elif core['Text'] == 'Core Average':
                self.average = value
            else:
                if 'Distance' not in core['Text']:
                    self.cores.append(value)

    def to_dict(self):
        """Transform the _Temperature object to dict
        :rtype: dict
        """
        data = {}

        data['cpu_package'] = self.package
        data['cpu_max'] = self.max
        data['cpu_average'] = self.average

        cpt = 0
        for core in self.cores:
            data[str(cpt)] = core
            cpt += 1

        data['unit'] = self.unit
   
        return data

class _Load:
    """Private class for creating a Load object.

    Provides CPU Load informations from Libre Hardware Monitor webserver.

    :param total (float):
    :param cores (list->float):
    :param unit (str):
    """

    def __init__(self, total=0.0, cores=[], unit='%'):

        self.total = total
        self.cores = cores
        self.unit = unit

    def parse(self, data):
        """Get CPU/Load subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' %').replace(',', '.'))
            if core['Text'] == 'CPU Total':
                self.total = value
            else:
                self.cores.append(value)

    def to_dict(self):
        """Transform the _Load object to dict
        :rtype: dict
        """
        data = {}

        data['cpu_total'] = self.total

        cpt = 0
        for core in self.cores:
            data[str(cpt)] = core
            cpt += 1

        data['unit'] = self.unit
   
        return data

class _Power:
    """Private class for creating a Power object.

    Provides CPU Power informations from Libre Hardware Monitor webserver.

    :param package (float):
    :param cores (float):
    :param graphics (float):
    :param memory (float):
    :param unit (str):
    """

    def __init__(self, package=0.0, cores=0.0, graphics=0.0, memory=0.0, unit='W'):

        self.package = package
        self.cores = cores
        self.graphics = graphics
        self.memory = memory
        self.unit = unit

    def parse(self, data):
        """Get CPU/Power subtree from data dictionnary"""
        for core in data:
            value = float(core['Value'].rstrip(' W').replace(',', '.'))

            if core['Text'] == 'CPU Package':
                self.package = value
            elif core['Text'] == 'CPU Cores':
                self.cores = value
            elif core['Text'] == 'CPU Graphics':
                self.graphics = value
            elif core['Text'] == 'CPU Memory':
                self.memory = value

    def to_dict(self):
        """Transform the _Power object to dict
        :rtype: dict
        """
        data = {}

        data['cpu_package'] = self.package
        data['cpu_cores'] = self.cores
        data['cpu_graphics'] = self.graphics
        data['cpu_memory'] = self.memory

        data['unit'] = self.unit
   
        return data

class CPU:
    """Class for creating a CPU object.

    Provides CPU informations from Libre Hardware Monitor webserver.

    Basic Usage::

      >>> from minotorr import cpu
      >>> cpu_ob = cpu.CPU(data) # data is the response from HTTP requests
      >>> cpu_ob.name
      Intel Core i5-4590
      >>> cpu_ob.cores
      4
      >>> cpu_obj.clock
      <minotorr.cpu._Clock>
      >>> cpu_obj.load
      <minotorr.cpu._Load>
      >>> cpu_obj.power
      <minotorr.cpu._Power>
      >>> cpu_obj.temperature
      <minotorr.cpu._Temperature>
    """
    def __init__(self, data):

        self.parsed_data = {}

        self.name = ''
        self.cores = 0

        self.clock = _Clock()
        self.load = _Load()
        self.power = _Power()
        self.temperature = _Temperature()

        self.update(data)

    def parse(self):
        """Get CPU subtree from data dictionnary"""
        for component in self.raw_data['Children'][0]['Children']:
            if component['ImageURL'] == 'images_icon/cpu.png':
                self.parsed_data = component

    def parse_name(self):
        """Get CPU name"""
        self.name = self.parsed_data['Text']

    def parse_cores(self):
        """Get the number of cores from CPU"""
        self.cores = len(self.parsed_data['Children'][0]['Children']) - 1

    def parse_clock(self):
        """Get clocks informations from CPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Clocks':
                self.clock.parse(category['Children'])

    def parse_temperature(self):
        """Get temperature informations from CPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Temperatures':
                self.temperature.parse(category['Children'])

    def parse_load(self):
        """Get load informations from CPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Load':
                self.load.parse(category['Children'])

    def parse_power(self):
        """Get power informations from CPU"""
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Powers':
                self.power.parse(category['Children'])
            
    def to_dict(self):
        """Transform the CPU object to dict
        :rtype: dict
        """
        cpu = {}
        cpu['name'] = self.name
        cpu['cores'] = self.cores
        cpu['clock'] = self.clock.to_dict()
        cpu['temperature'] = self.temperature.to_dict()
        cpu['load'] = self.load.to_dict()
        cpu['power'] = self.power.to_dict()

        return cpu

    def update(self, data):
        """Update CPU Object with new data
        :param data: Response in JSON from HTTP webserver
        """

        self.raw_data = data

        self.parse()
        self.parse_name()
        self.parse_cores()
        self.parse_clock()
        self.parse_temperature()
        self.parse_load()
        self.parse_power()
        
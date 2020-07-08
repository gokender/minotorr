"""CPU component module"""

class _Clock:
    """"""

    def __init__(self, speed=0.0, cores=[], unit='MHz'):
        self.cores = cores
        self.speed = speed
        self.unit = unit

    def parse(self, data):
        for core in data:
            value = float(core['Value'].rstrip(' MHz').replace(',', '.'))

            if core['Text'] == 'Bus Speed':
                self.speed = value
            else:
                self.cores.append(value)

    def to_dict(self):
        data = {}

        data['bus_speed'] = self.speed

        cpt = 0
        for core in self.cores:
            data[str(cpt)] = core
            cpt += 1

        data['unit'] = self.unit
   
        return data


class _Temperature:
    """"""

    def __init__(self, package=0.0, cores=[], cmax=0.0, average=0.0, unit='°C'):
        self.cores = cores
        self.package = package
        self.max = cmax
        self.average = average
        self.unit = unit

    def parse(self, data):
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
    """"""

    def __init__(self, total=0.0, cores=[], unit='%'):

        self.total = total
        self.cores = cores
        self.unit = unit

    def parse(self, data):
        for core in data:
            value = float(core['Value'].rstrip(' %').replace(',', '.'))
            if core['Text'] == 'CPU Total':
                self.total = value
            else:
                self.cores.append(value)

    def to_dict(self):
        data = {}

        data['cpu_total'] = self.total

        cpt = 0
        for core in self.cores:
            data[str(cpt)] = core
            cpt += 1

        data['unit'] = self.unit
   
        return data

class _Power:
    """"""

    def __init__(self, package=0.0, cores=0.0, graphics=0.0, memory=0.0, unit='W'):

        self.package = package
        self.cores = cores
        self.graphics = graphics
        self.memory = memory
        self.unit = unit

    def parse(self, data):
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
        data = {}

        data['cpu_package'] = self.package
        data['cpu_cores'] = self.cores
        data['cpu_graphics'] = self.graphics
        data['cpu_memory'] = self.memory

        data['unit'] = self.unit
   
        return data

class CPU:
    """"CPU Object"""

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
        for component in self.raw_data['Children'][0]['Children']:
            if component['ImageURL'] == 'images_icon/cpu.png':
                self.parsed_data = component

    def parse_name(self):
        self.name = self.parsed_data['Text']

    def parse_cores(self):
        self.cores = len(self.parsed_data['Children'][0]['Children']) - 1

    def parse_clocks(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Clocks':
                self.clock.parse(category['Children'])

    def parse_temperatures(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Temperatures':
                self.temperature.parse(category['Children'])

    def parse_loads(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Load':
                self.load.parse(category['Children'])

    def parse_powers(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Powers':
                self.power.parse(category['Children'])
            
    def to_dict(self):
        cpu = {}
        cpu['name'] = self.name
        cpu['cores'] = self.cores
        cpu['clock'] = self.clock.to_dict()
        cpu['temperature'] = self.temperature.to_dict()
        cpu['load'] = self.load.to_dict()
        cpu['power'] = self.power.to_dict()

        return cpu

    def update(self, data):

        self.raw_data = data

        self.parse()
        self.parse_name()
        self.parse_cores()
        self.parse_clocks()
        self.parse_temperatures()
        self.parse_loads()
        self.parse_powers()
        
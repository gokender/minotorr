"""Hardware component module"""

class CPU:
    """"CPU Object"""

    def __init__(self, data):

        self.parsed_data = {}

        self.name = ''
        self.cores = 0
        self.clocks = {}
        self.temperatures = {}
        self.loads = {}
        self.powers = {}

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
        #clocks = {}
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Clocks':
                for core in category['Children']:
                    values_temp = {
                        'min': float(core['Min'].rstrip(' MHz').replace(',', '.')),
                        'value': float(core['Value'].rstrip(' MHz').replace(',', '.')),
                        'max': float(core['Max'].rstrip(' MHz').replace(',', '.')),
                        'unit':'MHz'
                    }
                    if core['Text'] == 'Bus Speed':
                        self.clocks['bus_speed'] = values_temp
                    else:
                        self.clocks[core['Text'].split('#')[1]] = values_temp

    def parse_temperatures(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Temperatures':
                for core in category['Children']:
                    values_temp = {
                        'min': float(core['Min'].rstrip(' °C').replace(',', '.')),
                        'value': float(core['Value'].rstrip(' °C').replace(',', '.')),
                        'max': float(core['Max'].rstrip(' °C').replace(',', '.')),
                        'unit':'°C'
                    }
                    if core['Text'] == 'CPU Package':
                        self.temperatures['cpu_package'] = values_temp

                    elif core['Text'] == 'Core Max':
                        self.temperatures['cpu_max'] = values_temp
                    elif core['Text'] == 'Core Average':
                        self.temperatures['cpu_average'] = values_temp
                    else:
                        if 'Distance' not in core['Text']:
                            self.temperatures[core['Text'].split('#')[1]] = values_temp

    def parse_loads(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Load':
                for core in category['Children']:
                    values_temp = {
                        'min': float(core['Min'].rstrip(' %').replace(',', '.')),
                        'value': float(core['Value'].rstrip(' %').replace(',', '.')),
                        'max': float(core['Max'].rstrip(' %').replace(',', '.')),
                        'unit':'%'
                    }
                    if core['Text'] == 'CPU Total':
                        self.loads['cpu_total'] = values_temp
                    else:
                        self.loads[core['Text'].split('#')[1]] = values_temp

    def parse_powers(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Powers':
                for core in category['Children']:
                    values_temp = {
                        'min': float(core['Min'].rstrip(' W').replace(',', '.')),
                        'value': float(core['Value'].rstrip(' W').replace(',', '.')),
                        'max': float(core['Max'].rstrip(' W').replace(',', '.')),
                        'unit':'W'
                    }

                    if core['Text'] == 'CPU Package':
                        self.powers['cpu_package'] = values_temp
                    elif core['Text'] == 'CPU Cores':
                        self.powers['cpu_cores'] = values_temp
                    elif core['Text'] == 'CPU Graphics':
                        self.powers['cpu_graphics'] = values_temp
                    elif core['Text'] == 'CPU Memory':
                        self.powers['cpu_memory'] = values_temp

    def to_dict(self):
        cpu = {}
        cpu['name'] = self.name
        cpu['cores'] = self.cores
        cpu['clocks'] = self.clocks
        cpu['temperatures'] = self.temperatures
        cpu['loads'] = self.loads
        cpu['powers'] = self.powers

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
        
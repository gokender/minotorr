"""Hardware component module"""

class RAM:
    """"RAM Object"""

    def __init__(self, data):

        self.parsed_data = {}

        self.loads = {}
        self.data = {}

        self.update(data)

    def parse(self):
        for component in self.raw_data['Children'][0]['Children']:
            if component['ImageURL'] == 'images_icon/ram.png':
                self.parsed_data = component

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
                    if core['Text'] == 'Memory':
                        self.loads['memory'] = values_temp
                    elif core['Text'] == 'Virtual Memory':
                        self.loads['virtual_memory'] = values_temp

    def parse_data(self):
        for category in self.parsed_data['Children']:
            if category['Text'] == 'Data':
                for core in category['Children']:
                    values_temp = {
                        'min': float(core['Min'].rstrip(' GB').replace(',', '.')),
                        'value': float(core['Value'].rstrip(' GB').replace(',', '.')),
                        'max': float(core['Max'].rstrip(' GB').replace(',', '.')),
                        'unit':'GB'
                    }

                    if core['Text'] == 'Memory Used':
                        self.data['memory_used'] = values_temp
                    elif core['Text'] == 'Memory Available':
                        self.data['memory_available'] = values_temp
                    elif core['Text'] == 'Virtual Memory Used':
                        self.data['virtual_memory_used'] = values_temp
                    elif core['Text'] == 'Virtual Memory Available':
                        self.data['virtual_memory_available'] = values_temp

    def to_dict(self):
        ram = {}
        ram['loads'] = self.loads
        ram['data'] = self.data

        return ram

    def update(self, data):

        self.raw_data = data
        self.parse()
        self.parse_loads()
        self.parse_data()
        
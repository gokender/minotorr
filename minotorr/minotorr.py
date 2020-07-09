"""Minotor module."""

from datetime import datetime

import requests

from minotorr import cpu, ram, gpu

class Minotorr:

    def __init__(self, port=8085):

        self.port = port

        self.data, self.timestamp = self.download_data()
        self.cpu = cpu.CPU(self.data)
        self.ram = ram.RAM(self.data)
        self.gpu = gpu.GPU(self.data)

    def download_data(self):

        url = 'http://192.168.0.27:{}/data.json'.format(self.port)
        date_measure = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        
        try:
            response = requests.get(url)
            response.raise_for_status()

            return (response.json(), date_measure)

        except requests.exceptions.HTTPError as err:
            print(err)
            return (None, date_measure)

    def update(self):
        self.data, self.timestamp = self.download_data()
        self.cpu = self.cpu.update(self.data)
        self.ram = self.ram.update(self.data)
        self.cpu = self.gpu.update(self.data)
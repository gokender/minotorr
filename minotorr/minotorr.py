"""Minotor module."""

from datetime import datetime

import requests

from minotorr import cpu, ram

class Minotorr:

    def __init__(self, port=8085):

        self.port = port

        self.data, self.timestamp = self.download_data()
        self.cpu = cpu.CPU(self.data)
        self.ram = ram.RAM(self.data)

    def download_data(self):

        url = 'http://192.168.0.27:{}/data.json'.format(self.port)
        try:
            date_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            response = requests.get(url)
            response.raise_for_status()

            return (response.json(), date_time)

        except requests.exceptions.HTTPError as err:
            print(err)
            return (None, date_time)

    def update(self):

        self.data, self.timestamp = self.download_data()
        self.cpu = self.cpu.update(self.data, self.timestamp)
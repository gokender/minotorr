"""Main module."""
from datetime import datetime

import requests

from minotor import cpu

class Minotor:

    def __init__(self, port=8085):


        self.port = port
        self.data, self.timestamp = self.download_data(port)
        self.cpu = cpu.CPU(self.data, self.timestamp)

    
    def download_data(self, port):
        
        url = 'http://192.168.0.27:{}/data.json'.format(port)
        try:
            timestamp = int(datetime.timestamp(datetime.now()))
            
            response = requests.get(url)
            response.raise_for_status()
            
            return (response.json(), timestamp)
            
        except requests.exceptions.HTTPError as err:
            print(err)
            return (None, timestamp)
    
    def update(self):

        self.data, self.timestamp = self.download_data(self.port)
        self.cpu = self.cpu.update(self.data, self.timestamp)
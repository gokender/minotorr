"""Computer module."""
from datetime import datetime

import requests

from minotor import cpu

class HardwareMonitor:

    def __init__(self, port=8085):

        #self.port = port
        self.data, self.timestamp = self.download_data(port)
        self.cpu = cpu.CPU(self.data)

    def download_data(self, port):
        
        url = 'http://192.168.0.27:{}/data.json'.format(port)
        try:
            date_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            response = requests.get(url)
            response.raise_for_status()
            
            return (response.json(), date_time)
            
        except requests.exceptions.HTTPError as err:
            print(err)
            return (None, date_time)
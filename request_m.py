import urllib.request
import json


class Request:
    def __init__(self, date, currency,
                 url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={0}&date={1}&json"):
        self.date = date
        self.currency = currency
        self.url = url
        self.value = None
        self.name = None

    def get_info(self):
        with urllib.request.urlopen(self.url.format(self.currency, self.date)) as url:
            data = json.loads(url.read().decode())
            self.value = data[0]["rate"]
            self.name = data[0]["txt"]
            return self.value, self.name

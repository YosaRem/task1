from requests import get
from json import loads


class Finder:
    url = "http://free.ipwhois.io/json/"

    def __init__(self, ip):
        self.ip = ip
        self.data = self.get_data()

    def get_data(self):
        res = get(self.url + self.ip)
        if res.status_code == 200:
            return loads(res.content)
        return {"country": "None", "asn": "None", "isp": "None"}

    def get_as(self, ip):
        return str(self.data.get("asn"))

    def get_country(self, ip):
        return str(self.data.get("country"))

    def get_provider(self, ip):
        return str(self.data.get("isp"))

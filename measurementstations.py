from requests import get
from abstractclasses import API



class MeasurementStations(API):
    def __init__(self):
        self.url = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
        self.IDStations = []
        self.CityStations = []
        self.AdressStations = []
        self.URL = []
        self.measurementstations = {}

    def ConnectionAPI(self, url: str = None):
        self.req = get(self.url)

    def DataPreparation(self):
        self.data = self.req.json()
        return self.data

    def CreatingUrl(self, Id: list[int]):
        # url = 'http://api.gios.gov.pl/pjp-api/rest/station/sensors/'
        url = 'http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/'
        # print(len(url))
        for id in Id:
            URL = url + str(id)
            # print(URL)
            self.URL.append(URL)
        return self.URL
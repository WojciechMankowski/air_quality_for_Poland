from datadownload import ConnectionAPI
from measurementstations import MeasurementStations
from DataBase import DataBase

class MeasurementStationsContextManager(MeasurementStations):
    def __init__(self):
        super(MeasurementStationsContextManager, self).__init__()
    def __enter__(self):
        self.ConnectionAPI()
        self.DataPreparation()
    def __exit__(self, exc_type, exc_val, exc_tb):
        db = DataBase()
        db.Close()


def ContextManager(city):
    api = MeasurementStationsContextManager()
    db = DataBase()
    ID = db.DatabaseQueries(city=city)
    number = 0
    with api:
        url = api.CreatingUrl(Id=ID)
    for item in url:
        ConnectionAPI(item, number)
        number += 1
    

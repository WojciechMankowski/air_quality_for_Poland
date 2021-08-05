from ContextManager import MeasurementStationsContextManager
from DataBase import DataBase
from datadownload import APIDowladDate
def runexpley():
    api = MeasurementStationsContextManager()
    db = DataBase()
    isfile = db.is_db()
    if isfile == False:
        db.CreatTabels()
    print("Gdańsk")
    ID = db.DatabaseQueries("Gdańsk")
    data = APIDowladDate()
    # print("Warszawa")
    # ID = db.DatabaseQueries("Warszawa")
    with api:
        url = api.CreatingUrl(Id=ID)
    for item in url:
        data.ConnectionAPI(item)
    data_json = data.DataPreparation()
    print(data_json)
    data.ExtractionOfInformation()


if __name__ == '__main__':
    runexpley()


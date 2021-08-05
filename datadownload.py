from requests import get
from json import dump, load
class APIDowladDate():
    def ConnectionAPI(self, l, url: str=None) -> None:
        self.req = get(url)
        self.Number = 0
        self.numbestation = url[53:]
        print(self.numbestation)
        self.listNumbestation = []
        self.listNumbestation.append(self.numbestation)

        self.len = l
        self.air_quality_dictionary = {}
    def DataPreparation(self) -> None:
        self.data = self.req.json()
        return self.data
    def __iter__(self):
        return self
    def __next__(self):
        self.Number += 1
        self.ExtractionOfInformation(self.Number)
        if self.len == self.Number:
            raise StopIteration()
        return self.Number
    def ExtractionOfInformation(self, number):
        air_quality_dictionary = {}
        overall_air_quality = self.data['stIndexLevel'] #ogólna jakość powietrza
        overall_air_quality_index = overall_air_quality['indexLevelName'] #ogólna jakość powietrza
        air_quality_dictionary['Ogólna jakość powietrza'] = overall_air_quality_index

        SO2_level = self.data['so2IndexLevel']
        if SO2_level != None:
            SO2_level_index = SO2_level['indexLevelName']
            air_quality_dictionary["SO2"] = SO2_level_index
        else:
            SO2_level_index = None
            air_quality_dictionary["SO2"] = SO2_level_index
        NO2_level = self.data['no2IndexLevel']
        if NO2_level != None:
            NO2_level_index = NO2_level['indexLevelName']
            air_quality_dictionary["NO2"] = NO2_level_index
        else:
            NO2_level_index = None
            air_quality_dictionary["NO2"] = NO2_level_index


        pm10_level = self.data['pm10IndexLevel']
        if pm10_level != None:
            pm10_level_index = pm10_level['indexLevelName']
            air_quality_dictionary['pm10'] = pm10_level_index
        else:
            pm10_level_index = None
            air_quality_dictionary['pm10'] = pm10_level_index

        O3_level = self.data['o3IndexLevel']
        if O3_level != None:
            O3_level_index = O3_level['indexLevelName']
            air_quality_dictionary['O3'] = O3_level_index
        else:
            O3_level_index = None
            air_quality_dictionary['O3'] = O3_level_index
        self.air_quality_dictionary[number] = air_quality_dictionary
    def GetInformation(self) -> dict[int, dict[str, str]]:
        return self.air_quality_dictionary
lista = []
my_dict = {}

def ConnectionAPI(url,n) -> None:
    res = get(url)
    dataJSON = res.json()
    numbestation = url[53:]
    data = ExtractionOfInformation(dataJSON, numbestation)
    getmy_dict(data, n)
    saveToJSON(my_dict)

def getmy_dict(data, number):
    my_dict[f"{number}"] = data

def saveToJSON(data):
    with open('test.json', 'w') as file:
        dump(data, file, indent=4)
        file.close()

def readJSON():
    with open("test.json", "r") as fil:
        data = load(fil)
    return data

def ExtractionOfInformation(data, id):
    air_quality_dictionary = {}
    Air_quality_dictionary = {}
    print(data)
    overall_air_quality = data['stIndexLevel'] #ogólna jakość powietrza
    if overall_air_quality != None:
        overall_air_quality_index = overall_air_quality['indexLevelName'] #ogólna jakość powietrza
        air_quality_dictionary['Ogólna jakość powietrza'] = overall_air_quality_index
    else:
        overall_air_quality_index = None  # ogólna jakość powietrza
        air_quality_dictionary['Ogólna jakość powietrza'] = overall_air_quality_index

    SO2_level = data['so2IndexLevel']
    if SO2_level != None:
        SO2_level_index = SO2_level['indexLevelName']
        air_quality_dictionary["SO2"] = SO2_level_index
    else:
        SO2_level_index = None
        air_quality_dictionary["SO2"] = SO2_level_index
    NO2_level = data['no2IndexLevel']
    if NO2_level != None:
        NO2_level_index = NO2_level['indexLevelName']
        air_quality_dictionary["NO2"] = NO2_level_index
    else:
        NO2_level_index = None
        air_quality_dictionary["NO2"] = NO2_level_index


    pm10_level = data['pm10IndexLevel']
    if pm10_level != None:
        pm10_level_index = pm10_level['indexLevelName']
        air_quality_dictionary['pm10'] = pm10_level_index
    else:
        pm10_level_index = None
        air_quality_dictionary['pm10'] = pm10_level_index

    O3_level = data['o3IndexLevel']
    if O3_level != None:
        O3_level_index = O3_level['indexLevelName']
        air_quality_dictionary['O3'] = O3_level_index
    else:
        O3_level_index = None
        air_quality_dictionary['O3'] = O3_level_index
    Air_quality_dictionary[id] = air_quality_dictionary
    return Air_quality_dictionary
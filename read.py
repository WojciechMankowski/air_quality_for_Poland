from datadownload import readJSON
from DataBase import DataBase

def CreatAPI():



    data = readJSON()
    # print(data)
    listaDF = []
    api = {}
    db = DataBase()
    for key in data.keys():
        data_dict = data[key]
        for key, item in data_dict.items():
            address = db.DatabaseQueriesCity(key)
            api[address] = item
    return api

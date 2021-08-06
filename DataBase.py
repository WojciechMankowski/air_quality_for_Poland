import sqlite3
from os import listdir
# from dotenv import load_dotenv
import os
import psycopg2

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('air.db')
        self.coursor = self.conn.cursor()
    def CreatTabels(self):
        self.conn = sqlite3.connect('air.db')
        self.coursor = self.conn.cursor()
        create_query = '''
        CREATE TABLE IF NOT EXISTS stations (
        id integer PRIMARY KEY, 
        addressStreet text, 
        city_commune_communeName text,
        city_commune_districtName text,
        city_commune_provinceName text,
        city_id integer,
        city_name text,
        gegrLat real,
        gegrLon real,
        stationName text)
        '''
        self.coursor.execute(create_query)

    def is_db(self):
        lista_file = list(listdir())
        for item in lista_file:
            if item == 'air.db':
                return True
        return False

    def SaveInTabel(self, stations: list[dict[str, str]]):
        for station in stations:
            city = station["city"]
            commune = city['commune']
            listaSave = [
                station["id"],
                station["addressStreet"],
                commune['communeName'],
                commune["districtName"],
                commune["provinceName"],
                city["id"],
                city["name"],
                station["gegrLat"],
                station["gegrLon"],
                station["stationName"]
            ]
            self.coursor.execute("INSERT OR REPLACE INTO stations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", listaSave)
            self.conn.commit()
    def DatabaseQueries(self, city: str):
        ID = []
        query = f"SELECT id FROM  stations  WHERE city_commune_communeName = '{city}'"
        result = self.coursor.execute(query)
        for id in result:
            ID.append(id[0])
        return ID
    def DatabaseQueriesCity(self, id: int):
        print(id)
        ID = []
        query = f"SELECT city_commune_communeName, addressStreet FROM  stations  WHERE id = '{id}'"
        result = self.coursor.execute(query)
        rows = self.coursor.fetchall()[0]
        return f"{rows[1]} {rows[0]}"

    def Close(self):
        self.conn.close()

class DataBasePostgreSQL:
    def __init__(self):
        # load_dotenv()
        DATABASE_URL = os.getenv('DATABASE_URL')
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.coursor = self.conn.cursor()
    def SaveInTabel(self, stations: list[dict[str, str]]):
        for station in stations:
            city = station["city"]
            commune = city['commune']
            listaSave = [
                station["id"],
                station["addressStreet"],
                commune['communeName'],
                commune["districtName"],
                commune["provinceName"],
                city["id"],
                city["name"],
                station["gegrLat"],
                station["gegrLon"],
                station["stationName"]
            ]
            savetupla = tuple(listaSave)
            listaSave.clear()
            queue = f"INSERT INTO stations VALUES {savetupla}"
            cur.execute(queue)
        self.conn.commit()
        self.coursor.close()
    def DatabaseQueries(self, city: str):
        ID = []
        query = f"SELECT id FROM  stations  WHERE city_commune_communeName = '{city}'"
        self.coursor.execute(query)
        row = self.coursor.fetchone()
        while row is not None:
            print(row[0])
            ID.append(row[0])
            row = self.coursor.fetchone()
        return ID
    def DatabaseQueriesCity(self, id: int):
        print(id)
        ID = []
        query = f"SELECT city_commune_communeName, addressStreet FROM  stations  WHERE id = '{id}'"
        self.coursor.execute(query)
        row = self.coursor.fetchone()
        print(row[1])
        print(row[0])
        return f"{row[1]} {row[0]}"

    def Close(self):
        self.conn.close()

if __name__ == '__main__':
    db = DataBase()
    isfile = db.is_db()
    if isfile == False:
        db.CreatTabels()
    print("Gdańsk")
    db.DatabaseQueries("Gdańsk")
    print("Warszawa")
    db.DatabaseQueries("Warszawa")

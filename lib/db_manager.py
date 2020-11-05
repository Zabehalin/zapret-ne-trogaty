import psycopg2 
import requests
# if __name__ == "__main__":
#     db_manager


class db_manager():
    # ================ підключення до бази =================
    def __init__(self, host, user, passwd, url, token):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.__URL = url
        self.__db = psycopg2.connect(
            host=self.host,
            database="covid_19",
            user=self.user,
            password=self.passwd)
        self.__cursor = self.__db.cursor()
    # ================ Відключення від бази =================

    def __del__(self):
        self.__db.close()
        #print("test")
    # ================ Присвоєння URL =================

    def get_all_data(self):
        response = requests.get(self.__URL)
        return response.json()
    # ================ Створення бази =================

    def save_all_data(self, data):
        # print("save_all_data => ", data)
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS covid_19;")
        self.__cursor.execute("USE covid_19;")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS covid19_covid19 (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255),CountryCode VARCHAR(255), Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10),NewDeaths INT(10),TotalDeaths INT(10),NewRecovered INT(10),TotalRecovered INT(10))")
    # ================ Заповнення бази =================

    def add_corona(self, Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered,test):
        print("add_corona")
        sql = "INSERT INTO covid19_covid19 (id, country, countrycode, slug, newconfirmed, totalconfirmed, newdeaths, totaldeaths, newrecovered, totalrecovered) VALUES ('" + str(test) +"', '" + str(Country) + "', '" + str(CountryCode) + "', '" + str(Slug) + "', '" + str(NewConfirmed) + "', '" + str(TotalConfirmed) + "', '" + str(NewDeaths) + "', '" + str(TotalDeaths) + "', '" + str(NewRecovered) + "', '" + str(TotalRecovered) + "')"
        #val = (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed,NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)
        self.__cursor.execute(sql)
        self.__db.commit()
    # ================ Очистка бази =================

    def dell_corona(self):
        print("dell_corona")
        sql = "DELETE FROM covid19_covid19 "
        self.__cursor.execute(sql)
        self.__db.commit()
    # ================ Вивід з бази =================

    def vyvid_corona(self):
        print("vyvid_corona")
        sql = "SELECT * FROM covid19_covid19 "
        self.__cursor.execute(sql)
        retu = self.__cursor.fetchall()
        return retu
        # for item in self.__cursor.fetchall():
        #     print(item)
    # ================ Вивід з бази по назві країни =================

    def show_country(self, countr):
        sql = ("SELECT * FROM covid19_covid19 WHERE Country = '" + countr + "'")
        self.__cursor.execute(sql)
        coun = self.__cursor.fetchall()
        print(coun)
        return coun
    # ================ Вивід з бази по індексу країни =================

    def show_country_CountryCode(self, countr):
        sql = ("SELECT * FROM covid19_covid19 WHERE CountryCode = '" + countr + "'")
        self.__cursor.execute(sql)
        coun = self.__cursor.fetchall()
        print(coun)
        return coun

import pymysql


class Banco:
    db = pymysql.connect(host='localhost', user='root', password='Lk-08$14$22-!', database='projeto_integrado')
    cursor = db.cursor()

    def close_db(self):
        self.db.close()

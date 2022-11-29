import pymysql

db = pymysql.connect(host='localhost', user='root', password='Lk-08$14$22-!', database='projeto_integrado')

cursor = db.cursor()


class Banco:

    def inserir_ingrediente(self, nome, preco, total_gramas):
        g1 = (preco * 1) / total_gramas

        sql = f"""INSERT INTO Ingrediente(nome_ingrediente, preco_ingrediente, total_gramas, preco_grama_unidade) 
                VALUES('{nome}', {preco}, {total_gramas}, {g1})"""
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

        #db.close()

    def inserir_doce(self, nome, quantidade):

        sql = f"""INSERT INTO Doce(nome_doce, quantidade_doce) 
                        VALUES('{nome}', {quantidade})"""
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

        #db.close()

    def inserir_receita(self, list_ingr, list_qntd):
        doce_id_query = "SELECT ID_doce FROM doce ORDER BY 1 DESC LIMIT 1"
        try:
            cursor.execute(doce_id_query)
            doce_id = int(cursor.fetchone()[0])
            for i, q in zip(list_ingr, list_qntd):
                print(i)
                sql = f"""INSERT INTO Receita(ID_doce, ID_ingrediente, quantidade_ingrd) 
                                       VALUES('{doce_id}', {int(i)}, {q})"""
                cursor.execute(sql)
                db.commit()
        except Exception as e:
            print("NONONonO")
            print(e)
            db.rollback()

        #db.close()

    def select_ingredientes(self):
        try:
            cursor.execute("SELECT * FROM Ingrediente")
            select = cursor.fetchall()
            return select
        except Exception as e:
            print(e)

    def deletar_ingrediente(self, id):
        try:
            cursor.execute(f"DELETE FROM Ingrediente WHERE ID_ingrediente = {int(id)}")
            db.commit()
        except Exception as e:
            print(f"id --> {id}")
            print(e)


        # db.close()


teste = Banco()
#print(teste.select_ingredientes()[0])
#teste.inserir_ingrediente('Leite condensado semideslatado', 2.68, 395)
#teste.inserir_ingrediente('Leite condensado semideslatado', 2.68, 395)
#teste.inserir_ingrediente('Manteiga com sal itambé', 24.50, 500)
#teste.inserir_ingrediente('Alpino Achocolatado em pó', 19.99, 1000)
#teste.inserir_ingrediente('Confeito miçanga 8 cores', 5.15, 100)
#teste.inserir_ingrediente('Forminha papel laminadas', 19.40, 200)


#teste.inserir_doce('Aleluia', 13, 5)








'''
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lk-08$14$22-!',
    port='3306',
    database='ativ_proj_pratic')

cursor = mydb.cursor()
'''
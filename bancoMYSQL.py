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
                sql = f"""INSERT INTO Receita(ID_doce, ID_ingrediente, quantidade_ingrd) 
                                       VALUES('{doce_id}', {int(i)}, {q})"""
                cursor.execute(sql)
                db.commit()
        except Exception as e:
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

    def select_doces(self):
        try:
            cursor.execute("SELECT * FROM doce")
            select = cursor.fetchall()
            return select
        except Exception as e:
            print(e)

    def select_receita(self):
        sql = '''
            SELECT d.nome_doce, i.nome_ingrediente, i.preco_ingrediente, i.total_gramas, r.quantidade_ingrd, d.preco_total FROM receita r
            inner join doce d on r.ID_doce = d.ID_doce
            inner join ingrediente i on r.ID_ingrediente = i.ID_ingrediente
              '''
        try:
            cursor.execute(sql)
            select = cursor.fetchall()
            return select
        except Exception as e:
            print(e)

    def deletar_ingrediente(self, id):
        try:
            cursor.execute(f"DELETE FROM Ingrediente WHERE ID_ingrediente = {int(id)}")
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        # db.close()

    def deletar_doce(self, id):
        try:
            cursor.execute(f"DELETE FROM doce WHERE ID_doce = {int(id)}")
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        # db.close()

    def update_calculo(self, qntd):
        doce_id_query = "SELECT ID_doce FROM doce ORDER BY 1 DESC LIMIT 1"
        try:
            cursor.execute(doce_id_query)
            doce_id = int(cursor.fetchone()[0])

            sql = f'''
                    SELECT d.nome_doce, i.nome_ingrediente, r.quantidade_ingrd, i.preco_grama_unidade FROM doce as d inner join
                    receita as r on r.ID_doce = d.ID_doce inner join
                    ingrediente as i on i.ID_ingrediente = r.ID_ingrediente
                    WHERE d.ID_doce = {doce_id};
                    '''

            cursor.execute(sql)
            select = cursor.fetchall()

            calc = 0
            for i in range(len(select)):
                calc += select[i][2]*select[i][3]

            sql_update = f"UPDATE doce SET preco_total = {calc}, preco_unidade = {calc/float(qntd)} WHERE ID_doce = {doce_id}"
            cursor.execute(sql_update)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()


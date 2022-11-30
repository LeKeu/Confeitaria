from bancoMYSQL import Banco


class Receita(Banco):

    def inserir_receita(self, list_ingrd, list_qntd):
        doce_id_query = "SELECT ID_doce FROM doce ORDER BY 1 DESC LIMIT 1"
        try:
            Banco.cursor.execute(doce_id_query)
            doce_id = int(Banco.cursor.fetchone()[0])
            for i, q in zip(list_ingrd, list_qntd):
                sql = f"""INSERT INTO Receita(ID_doce, ID_ingrediente, quantidade_ingrd) 
                                       VALUES('{doce_id}', {int(i)}, {q})"""
                Banco.cursor.execute(sql)
                Banco.db.commit()
        except Exception as e:
            print(e)
            Banco.db.rollback()

        # db.close()

    def select_receita(self):
        sql = '''
            SELECT d.nome_doce, i.nome_ingrediente, i.preco_ingrediente, i.total_gramas, 
            r.quantidade_ingrd, d.preco_total FROM receita r
            inner join doce d on r.ID_doce = d.ID_doce
            inner join ingrediente i on r.ID_ingrediente = i.ID_ingrediente
              '''
        try:
            Banco.cursor.execute(sql)
            select = Banco.cursor.fetchall()
            return select
        except Exception as e:
            print(e)

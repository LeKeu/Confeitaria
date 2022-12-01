from bancoMYSQL import Banco


class Doce(Banco):

    def inserir_doce(self, nome, quantidade):

        sql = f"""INSERT INTO Doce(nome_doce, quantidade_doce) 
                        VALUES('{nome}', {quantidade})"""
        try:
            Banco.cursor.execute(sql)
            Banco.db.commit()
        except Exception as e:
            print(e)
            Banco.db.rollback()

        # db.close()

    def select_doces(self):
        try:
            Banco.cursor.execute("SELECT * FROM doce")
            select = Banco.cursor.fetchall()
            return select
        except Exception as e:
            print(e)

    def deletar_doce(self, id_doce):
        try:
            Banco.cursor.execute(f"DELETE FROM doce WHERE ID_doce = {int(id_doce)}")
            Banco.db.commit()
        except Exception as e:
            print(e)
            Banco.db.rollback()
        # db.close()

    def update_calculo(self, qntd):
        doce_id_query = "SELECT ID_doce FROM doce ORDER BY 1 DESC LIMIT 1"
        try:
            Banco.cursor.execute(doce_id_query)
            doce_id = int(Banco.cursor.fetchone()[0])

            sql = f'''
                    SELECT d.nome_doce, i.nome_ingrediente, r.quantidade_ingrd, i.preco_grama_unidade 
                    FROM doce as d inner join
                    receita as r on r.ID_doce = d.ID_doce inner join
                    ingrediente as i on i.ID_ingrediente = r.ID_ingrediente
                    WHERE d.ID_doce = {doce_id};
                    '''

            Banco.cursor.execute(sql)
            select = Banco.cursor.fetchall()

            '''
            (CA + CF) / 1 - ML
            CF -> gasto com gasolina e embalagem
            CA -> calc
            ML -> em %, quanto ele deseja ganhar. pegar do q a gente mandou do girotto ou perguntar p pessoa
            '''

            calc = 0
            for i in range(len(select)):
                calc += select[i][2]*select[i][3]

            sql_update = f'''UPDATE doce SET preco_total = {calc}, preco_unidade = {calc/float(qntd)} 
            WHERE ID_doce = {doce_id}'''
            Banco.cursor.execute(sql_update)
            Banco.db.commit()
        except Exception as e:
            print(e)
            Banco.db.rollback()

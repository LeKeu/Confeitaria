from bancoMYSQL import Banco


class Ingrediente(Banco):

    def inserir_ingrediente(self, nome, preco, total_gramas):
        g1 = (preco * 1) / total_gramas

        sql = f"""INSERT INTO Ingrediente(nome_ingrediente, preco_ingrediente, total_gramas, preco_grama_unidade) 
                VALUES('{nome}', {preco}, {total_gramas}, {g1})"""
        try:
            Banco.cursor.execute(sql)
            Banco.db.commit()
        except Exception as e:
            print(e)
            Banco.db.rollback()

    def select_ingredientes(self):
        try:
            Banco.cursor.execute("SELECT * FROM Ingrediente")
            select = Banco.cursor.fetchall()
            return select
        except Exception as e:
            print(e)

    def deletar_ingrediente(self, id_ingrd):
        try:
            Banco.cursor.execute(f"DELETE FROM Ingrediente WHERE ID_ingrediente = {int(id_ingrd)}")
            Banco.db.commit()
        except Exception as e:
            print(e)
            Banco.db.rollback()

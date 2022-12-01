from flask import Flask, render_template, request, redirect, url_for, flash

import bancoMYSQL as Banco
import Doce as Doce
import Ingrediente as Ingrd
import Receita as Receita


BANCO = Banco.Banco()
DOCE = Doce.Doce()
INGREDIENTE = Ingrd.Ingrediente()
RECEITA = Receita.Receita()

app = Flask(__name__)
app.secret_key = 'filoGoretti'


@app.route('/')
def inicio():
    #BANCO.close_db()
    return render_template('indexInicio.html')

# ================================================================================
#       INGREDIENTES


@app.route('/ingredientes')
def ingredientes():
    list_ingrd = INGREDIENTE.select_ingredientes()
    return render_template('indexIngrediente.html', list_ingrd=list_ingrd)


@app.route('/add_ingrediente', methods=['POST'])
def add_ingrediente():
    if request.method == 'POST':
        nome = request.form['fname']
        preco = request.form['preco']
        tot_grama = request.form['totGrama']

        if ',' in preco:
            preco.replace(',', '.')

        if (nome and preco and tot_grama) != '':
            INGREDIENTE.inserir_ingrediente(nome, float(preco), float(tot_grama))
            flash("Ingrediente Adicionado!", "info")
        else:
            flash("Preencha todos os campos!", "error")
        return redirect(url_for('ingredientes'))


@app.route('/delete_ingrd/<string:id_ingrd>', methods=['POST', 'GET'])
def deletar_ingrediente(id_ingrd):
    INGREDIENTE.deletar_ingrediente(id_ingrd)
    flash("Ingrediente Deletado!", "info")
    return redirect(url_for('ingredientes'))
# ================================================================================
# ================================================================================

#       ADICIONAR DOCE


@app.route('/add_doce', methods=['GET', 'POST'])
def add_doce():
    if request.method == 'POST':
        ingrds = request.form.getlist("ingrd_checkbox")
        nome = request.form['Dnome']
        qntd = request.form['Dqntd']

        if (nome and qntd) != '' and len(ingrds) > 0:
            list_qntd = []
            for i in ingrds:
                list_qntd.append(int(request.form[i]))

            DOCE.inserir_doce(nome, qntd)
            RECEITA.inserir_receita(ingrds, list_qntd)
            DOCE.update_calculo(qntd)
            flash("Doce Adicionado!", "info")
        else:
            print(ingrds)
            print(nome)
            print(qntd)
            flash("Preencha todos os campos!", "error")

    list_ingrd = INGREDIENTE.select_ingredientes()
    list_doce = DOCE.select_doces()
    return render_template('indexDoce.html', list_ingrd=list_ingrd, list_doce=list_doce)


@app.route('/delete_doce/<string:id_doce>', methods=['POST', 'GET'])
def deletar_doce(id_doce):
    DOCE.deletar_doce(id_doce)
    flash("Doce Deletado!", "info")
    return redirect(url_for('add_doce'))

# ================================================================================


@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    return render_template('indexCalc.html')


@app.route('/receitas')
def receitas():
    list_receita = RECEITA.select_receita()
    return render_template('indexReceita.html', list_receita=list_receita)


if __name__ == "__main__":
    app.run(debug=True)

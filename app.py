from flask import Flask, render_template, request, redirect, url_for, flash

import bancoMYSQL as x

BANCO = x.Banco()

app = Flask(__name__)
app.secret_key = 'filoGoretti'

@app.route('/')
def inicio():
    return render_template('indexInicio.html')

#================================================================================
#================================================================================
#       INGREDIENTES
@app.route('/ingredientes')
def ingredientes():
    list_users = BANCO.select_ingredientes()
    return render_template('indexIngrediente.html', list_users=list_users)


@app.route('/add_ingrediente', methods=['POST'])
def add_ingrediente():
    if request.method == 'POST':
        nome = request.form['fname']
        preco = request.form['preco']
        totGrama = request.form['totGrama']

        if ',' in preco:
            preco.replace(',', '.')

        if (nome and preco and totGrama) != '':
            BANCO.inserir_ingrediente(nome, float(preco), float(totGrama))
            flash("Ingrediente Adicionado!", "info")
        else:
            flash("Preencha todos os campos!", "error")
            print("ohohohohohoho")
        return redirect(url_for('ingredientes'))


@app.route('/delete_ingrd/<string:id>', methods=['POST', 'GET'])
def deletar_ingrediente(id):
    BANCO.deletar_ingrediente(id)
    flash("Ingrediente Deletado!", "info")
    return redirect(url_for('ingredientes'))
#================================================================================
#================================================================================

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

            BANCO.inserir_doce(nome, qntd)
            BANCO.inserir_receita(ingrds, list_qntd)
            BANCO.update_calculo(qntd)
            flash("Doce Adicionado!", "info")
        else:
            flash("Preencha todos os campos!", "error")
            print("HOHOHOH")

    list_ingrd = BANCO.select_ingredientes()
    list_doce = BANCO.select_doces()
    return render_template('indexDoce.html', list_ingrd=list_ingrd, list_doce=list_doce)


@app.route('/delete_doce/<string:id>', methods=['POST', 'GET'])
def deletar_doce(id):
    BANCO.deletar_doce(id)
    flash("Doce Deletado!", "info")
    return redirect(url_for('add_doce'))
#================================================================================


@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    return render_template('indexCalc.html')


@app.route('/receitas')
def receitas():
    list_receita = BANCO.select_receita()
    return render_template('indexReceita.html', list_receita=list_receita)




if __name__ == "__main__":
    app.run(debug=True)
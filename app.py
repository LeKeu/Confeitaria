from flask import Flask, render_template, request, redirect, url_for

import bancoMYSQL as x

BANCO = x.Banco()

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('indexInicio.html')

#================================================================================
#       ADICIONAR INGREDIENTES
@app.route('/ingredientes')
def ingredientes():
    list_users = BANCO.select_ingredientes()
    return render_template('indexIngrediente.html', list_users=list_users)


@app.route('/add_ingrediente', methods=['POST'])
def add_ingrediente():
    if request.method == 'POST':
        nome = request.form['fname']
        preco = float(request.form['preco'])
        totGrama = float(request.form['totGrama'])
        BANCO.inserir_ingrediente(nome, preco, totGrama)
        return redirect(url_for('ingredientes'))


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def deletar_ingrediente(id):
    BANCO.deletar_ingrediente(id)
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
        list_qntd = []
        for i in ingrds:
            list_qntd.append(int(request.form[i]))

        calc = 0
        for i in range(len(ingrds)):
            calc += BANCO.retornar_precoUni_ingrediente()*BANCO.retornar_gramaTot_ingrediente()
        calc_tot = calc * qntd

        BANCO.inserir_doce(nome, qntd)
        BANCO.inserir_receita(ingrds, list_qntd)


    list_ingrd = BANCO.select_ingredientes()
    return render_template('indexDoce.html', list_ingrd=list_ingrd)

#================================================================================


if __name__ == "__main__":
    app.run(debug=True)
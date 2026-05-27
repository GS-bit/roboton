from random import choice, randint

from flask import Flask, render_template, request, jsonify

from batalha import Batalha
from dialogos import dialogar
from golpes import GOLPES
from heroi import Heroi
from vilao import Vilao

app = Flask(__name__)

personagens = []

@app.route('/')
def index():
    global personagens
    personagens = [
        Heroi('Benignoton', 100, 100, 100), 
        Vilao('Malignoton', 100, 100, 100)
    ]
    
    offensives = []
    specials = []
    dialog = dialogar()

    for i in GOLPES.keys():
        if GOLPES[i]['tipo'] == 'Ofensivo':
            offensives.append({"nome": i, "desc": GOLPES[i]['desc'], "poder": GOLPES[i]['poder']})
        else:
            specials.append({"nome": i, "desc": GOLPES[i]['desc'], "poder": GOLPES[i]['poder']})

    return render_template('index.html', 
                           benignoton=personagens[0],
                           malignoton=personagens[1],
                           offensives=offensives, 
                           specials=specials,
                           dialog=dialog,)

@app.route('/move', methods=['POST'])
def move():
    dados = request.get_json()

    escolha_do_heroi = dados.get('move')

    batalha = Batalha(personagens[0], personagens[1])

    log = ""

    batalha.next_turno(escolha_do_heroi)
    
    return jsonify({
        'dialog': batalha.dialogo,
        'log': batalha.log,
        'benignotonVidaPercentual': 100 * batalha.heroi.vida_atual / batalha.heroi.vida_max,
        'malignotonVidaPercentual': 100 * batalha.vilao.vida_atual / batalha.vilao.vida_max,
        'benignotonCondicao': batalha.heroi.condicao,
        'malignotonCondicao': batalha.vilao.condicao
    })

if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

# instanciando recurso flask para criar servidor e armazenar em variável 'app'
app = Flask(__name__, template_folder='templates')

# uri - faça a conexão com banco de dados MongoDB utilizando variáveis de ambiente do sistema operacional
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

# atribuindo recursos mongo python em variável
mongo = PyMongo(app)
db = mongo.db

# Rota Inicial renderizando template
@app.route("/")
def hello_world():
    return render_template('index.html')

# Rota para persistir dados em MongoDB 
@app.route("/new/piratas")
def add_pirates():
    db.piratas.insert_many([
        {'_id': 1, 'nome': "Henrique", 'sobrenome':"Souza", 'email':"annibalhsouza@gmail.com", 'idade': "29", 'cargo': "fundador/CTO",  'genero': "masculino", 'github': "ahsouza", 'url': "https://ahsouza.github.io/", 'linkedin': "anibalhenriquesouza", 'skills': "rust - go - js - ts - html - css - java - c/c++ - c# - py - shell - linux/windows/darwin" },
        {'_id': 2, 'nome': "William", 'sobrenome':"Agostini", 'email':"willsantos96@gmail.com", 'idade': "27", 'cargo': "Sócio Desenvolvedor", 'genero': "masculino", 'github': "willsantos96", 'url': "https://williamagostini.github.io/", 'linkedin': "william-agostini", 'skills': "js - html - css - py - shell - docker - linux/windows"},
        ])
    return jsonify(message="Pirata adicionado", status="success"), 201

# rota para obter lista de todos piratas
@app.route('/piratas')
def piratas():
    # atribuir informações da query em variável '_piratas'
    _piratas = db.piratas.find()

    # variável tipo interface
    item = {}
    data = []
    # percorrer elementos para cada pirata e exibir dados básico sobre ele em formato JSON
    for pirata in _piratas:
        item = {
            'id': str(pirata['_id']),
            'nome': pirata['nome'],
            'sobrenome': pirata['sobrenome'],
            'email': pirata['email'],
            'idade': pirata['idade'],
            'github': pirata['github'],
            'linkedin': pirata['linkedin'],
            'url': pirata['url'],
        }
        # adicionar elemento
        data.append(item)
        
    # retornar piratas
    return jsonify(
        status=True,
        data=data
    )

# rota para obter pirata específico através de 'id'
@app.route("/pirata/<int:pirataId>")
def pirata(pirataId):
    pirata = db.piratas.find_one({"_id": pirataId})
    return pirata

# rota para obter pirata específico através do github
@app.route("/pirata/<string:github>")
def pirata_github(github):
    pirata = db.piratas.find_one({"github": github})
    return pirata

# rota para solicitar cotação do projeto desejado
@app.route("/send/cotacao", methods=['POST'])
def enviar_cotacao():
    try:
        # criar cotação
        try:
            body = request.json
            db.cotacoes.insert_one({ '_id': request.json.get('_id', None), 'nome': request.json.get('nome', None), 'empresa': request.json.get('empresa', None), 'email': request.json.get('email', None), 'sinopse_do_projeto': request.json.get('sinopse_do_projeto', None), 'valor_total_estimado': request.json.get('valor_estimado', None)})
            
            return body
        except:
            # solicitação incorreta, pois o corpo da solicitação não está disponível
            # adiciona mensagem para fins de depuração
            return "", 400
        # Prepare the response
        if isinstance(data, list):
            # retorna a lista de Id do item recém-criado
            return jsonify([str(v) for v in data]), 201
        else:
            # retorna o Id do item recém-criado
            return jsonify(str(data)), 201
    except:
        # Erro ao tentar criar o recurso
        return "", 500

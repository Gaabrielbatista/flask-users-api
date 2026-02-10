from os import system
system('clear')


from flask import Flask, make_response, jsonify, request, render_template
from bd import Carros

app = Flask(__name__)

# Parar de ordenar
app.json.sort_keys = False

@app.route('/')
def homepage():
    return render_template('index.html')

# Endpoint para listar e cadastrar carros
@app.route('/carros', methods=['GET'])
def get_carro():
    return make_response(jsonify(Mensagem="Lista de Carros:", Dados=Carros))

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)

    return make_response(jsonify(Mensagem=f"Carro cadastrado com sucesso no ID: {carro['id']}.", Dados=carro))

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request, render_template
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
    return jsonify(Mensagem="Lista de Carros:", Dados=Carros)

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)

    return jsonify(Mensagem=f"Carro cadastrado com sucesso no ID: {carro['id']}.", Dados=carro)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from bd import Carros
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(
        user='flask_user',
        password='flask_pass123',
        host='localhost',
        database='gaabrieldb',
        port='3307',
    )

app = Flask(__name__)
# Parar de ordenar
app.json.sort_keys = False

# Endpoint para listar e cadastrar carros
@app.route('/carros', methods=['GET'])
def get_carro():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM carros;')
    carros = cursor.fetchall()
    result = list()

    for carro in carros:
        result.append(
            {
                "id":  carro[0],
                "marca": carro[1],
                "modelo": carro[2],
                "ano": carro[3]
            }
        )
    cursor.close()

    return jsonify(menssagem='Carros.', dados=result)

# Arrumar
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)

    return jsonify(Mensagem=f"Carro cadastrado com sucesso no ID: {carro['id']}.", Dados=carro)

if __name__ == '__main__':
    app.run(debug=True)

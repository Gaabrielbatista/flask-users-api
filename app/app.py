from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

cnx = mysql.connector.connect(
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        host=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'),
        port=3307
    )

app = Flask(__name__)
cors = CORS(app)
# Parar de ordenar
app.json.sort_keys = False

# Endpoints
@app.route('/carros', methods=['GET'])
def get_carro():
    cursor = cnx.cursor()

    query = 'SELECT * FROM carros'
    cursor.execute(query)
    
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

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    cursor = cnx.cursor()

    query = 'INSERT INTO carros (marca, modelo, ano) VALUES (%s, %s, %s)'
    cursor.execute(query, (carro["marca"], carro["modelo"], carro["ano"]))
    
    cnx.commit()
    cursor.close()

    return jsonify(mensagem=f"Carro cadastrado com sucesso!", dados=carro)  

@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    cursor = cnx.cursor()

    query = 'DELETE FROM carros WHERE id = %s'
    cursor.execute(query, (id,))

    cnx.commit()    
    cursor.close()

    return jsonify(Mensagem="Sucesso!", Dados=id)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT'), load_dotenv=True)

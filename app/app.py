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
@app.route('/users', methods=['GET'])
def get_users():
    cursor = cnx.cursor()

    query = 'SELECT * FROM users'
    cursor.execute(query)

    users = cursor.fetchall()

    result = list()

    for user in users:
        result.append(
            {
                "id":  user[0],
                "nome": user[1],
                "email": user[2],
                "idade": user[3]
            }
        )
    cursor.close()

    return jsonify(menssagem="Users:", dados=result)

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    cursor = cnx.cursor()
    print(user)
    query = 'INSERT INTO users (nome, email, idade) VALUES (%s, %s, %s)'
    cursor.execute(query, (user["nome"], user["email"], user["idade"]))
    
    cnx.commit()
    cursor.close()

    
    return jsonify(mensagem="Sucesso!", dados=user)  

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = request.json
    cursor = cnx.cursor()

    query = 'UPDATE users SET nome = %s, email = %s, idade = %s WHERE id = %s'
    cursor.execute(query, (user["nome"], user["email"], user["idade"], id))

    cnx.commit()
    cursor.close()

    return jsonify(mensagem="Sucesso!", dados=user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = cnx.cursor()

    query = 'DELETE FROM users WHERE id = %s'
    cursor.execute(query, (id,))

    cnx.commit()    
    cursor.close()

    return jsonify(mensagem="Sucesso!", id=id)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT'), load_dotenv=True)

from app import app
from flask import jsonify, request
from database.connection import get_db_connection
from serializers.user_serializer import map_user

# Endpoints relacionados aos usuários
@app.route('/users', methods=['GET'])
def get_users():
    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = 'SELECT * FROM users'
    cursor.execute(query)

    users = cursor.fetchall()

    result = [map_user(user) for user in users]

    cursor.close()
    cnx.close()
    return jsonify(menssagem="Users", dados=result)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = 'SELECT * FROM users WHERE id = %s'
    cursor.execute(query, (id,))

    db_result = cursor.fetchall()
    row = db_result[0]

    user = map_user(row)

    cursor.close()
    cnx.close()
    return jsonify(mensagem="User", dados=user)

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json

    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = 'INSERT INTO users (nome, email, idade) VALUES (%s, %s, %s)'
    cursor.execute(query, (user["nome"], user["email"], user["idade"]))
    
    cnx.commit()

    cursor.close()
    cnx.close()
    return jsonify(mensagem="Sucesso!", dados=user)  

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = request.json

    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = 'UPDATE users SET nome = %s, email = %s, idade = %s WHERE id = %s'
    cursor.execute(query, (user["nome"], user["email"], user["idade"], id))

    cnx.commit()

    cursor.close()
    cnx.close()
    return jsonify(mensagem="Sucesso!", dados=user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = 'DELETE FROM users WHERE id = %s'
    cursor.execute(query, (id,))

    cnx.commit()

    cursor.close()
    cnx.close()
    return jsonify(mensagem="Sucesso!", id=id)

from app import app
from flask import jsonify, request
from database.connection import get_db_connection
from serializers.user_serializer import map_user
from math import ceil

# Endpoints relacionados aos usuários
@app.route('/users', methods=['GET'])
def get_users():
    page = max(int(request.args.get("page", 1)), 1) # Pega o número da página, ou 1 se não for fornecido, max() garante que page não seja menor que 1
    limit = min(int(request.args.get("limit", 10)), 100) # Pega o número de itens por página, ou 10 se não for fornecido, min limita para 100
    offset = (page - 1) * limit # offset = quantidade de registros antes da página atual = (página anterior) × limit


    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = 'SELECT id, nome, email, idade FROM users LIMIT %s OFFSET %s;'
    cursor.execute(query, (limit, offset))
    users = cursor.fetchall()

    users_dados = [map_user(user) for user in users]

    # Consulta para contar o total de usuários
    query_count = 'SELECT COUNT(*) FROM users;'
    cursor.execute(query_count)
    contagem_total = cursor.fetchone()
    
    contagem_total = contagem_total[0]

    # page = str(page)
    # limit = str(limit)
    # offset = str(offset)

    cursor.close()
    cnx.close()

    paginas_total = ceil(contagem_total/limit)

    print("page=", page)
    print("limit=", limit)
    print("offset=", offset)

    return jsonify(data=users_dados, pagination={"page":page, "limit":limit, "total":contagem_total, "total_pages":paginas_total})

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

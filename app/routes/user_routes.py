from app import app
from flask import jsonify, request
from database.connection import connection_manager
from serializers.user_serializer import map_user
from math import ceil


# Endpoints
@app.route('/users', methods=['GET'])
def get_users():
    page = max(int(request.args.get("page", 1)),
               1)

    limit_max = max(int(request.args.get("limit", 10)), 1)
    limit = min(limit_max, 100)

    offset = (page - 1) * limit

    with connection_manager() as cursor:
        query = 'SELECT id, nome, email, idade FROM users LIMIT %s OFFSET %s;'
        cursor.execute(query, (limit, offset))

        users = cursor.fetchall()
        print(users)
        users_data = [map_user(user) for user in users]

        # Consulta para contar o total de usuários
        query_count = 'SELECT COUNT(*) FROM users;'
        cursor.execute(query_count)

        total_count = cursor.fetchone()[0]

    total_pages = ceil(total_count / limit)

    # page = str(page)
    # limit = str(limit)
    # offset = str(offset)

    print("page =", page)
    print("limit=", limit)
    print("offset =", offset)

    return jsonify(data=users_data,
                   pagination={"page": page, "limit": limit, "total": total_count, "total_pages": total_pages}), 200


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    with connection_manager() as cursor:
        query = 'SELECT id, nome, email, idade FROM users WHERE id = %s'
        cursor.execute(query, (id,))

        db_result = cursor.fetchone()

        if not db_result:
            return jsonify(error="User not found"), 404

        user_data = map_user(db_result)

    return jsonify(data=user_data), 200


@app.route('/users', methods=['POST']) # Arrumar
def create_user():
    user_data = request.json

    if not user_data:
        return jsonify(error= "Nenhum dado JSON fornecido."), 400

    name = user_data.get("nome")
    email = user_data.get("email")
    age = user_data.get("idade", None)

    # name
    if not name or name.isspace():
        return jsonify(error="Campo 'nome' é obrigatório e não pode estar vazio."), 400

    if not isinstance(name, str):
        return jsonify(error="Campo 'nome' deve ser String."), 400

    # email
    if not email or email.isspace():
        return jsonify(error="Campo 'email' é obrigatório e não pode estar vazio."), 400

    if not isinstance(email, str):
        return jsonify(error="Campo 'email' deve ser String."), 400

    if "." not in email or "@" not in email:
        return jsonify(error="Campo 'email' deve conter '@' e '.' (ponto)."), 400

    # age
    if not age:
        if not isinstance(age, int):
            return jsonify(error="Campo 'idade' deve ser Integer."), 400

    if age < 1 or age > 120:
            return jsonify(error="Campo 'idade' deve estar entre 1 e 120."), 400

    with connection_manager() as cursor:
        if age:
            query = 'INSERT INTO users (nome, email, idade) VALUES (%s, %s, %s)'
            cursor.execute(query, (name, email, age))
        else:
            query = 'INSERT INTO users (nome, email) VALUES (%s, %s)' # arrumar
            cursor.execute(query, (name, email))


    return jsonify(data=user_data), 201


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_data = request.json

    with connection_manager() as cursor:
        query = 'UPDATE users SET nome = %s, email = %s, idade = %s WHERE id = %s'
        cursor.execute(query, (user_data["nome"], user_data["email"], user_data["idade"], id))

    return jsonify(data=user_data), 200


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    with connection_manager() as cursor:
        query = 'DELETE FROM users WHERE id = %s'
        cursor.execute(query, (id,))

    return jsonify(data=id), 204

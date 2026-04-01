from app import app
from flask import jsonify, request
from database.connection import connection_manager
from serializers.user_serializer import map_user
from math import ceil


# Endpoints relacionados aos usuários
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
        users_datas = [map_user(user) for user in users]

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

    return jsonify(data=users_datas,
                   pagination={"page": page, "limit": limit, "total": total_count, "total_pages": total_pages}), 200


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    with connection_manager() as cursor:
        query = 'SELECT id, nome, email, idade FROM users WHERE id = %s'
        cursor.execute(query, (id,))

        db_result = cursor.fetchone()

        if not db_result:
            return jsonify(error="User not found"), 404

        user_datas = map_user(db_result)

    return jsonify(data=user_datas), 200


@app.route('/users', methods=['POST'])
def create_user():
    user_datas = request.json

    with connection_manager() as cursor:
        query = 'INSERT INTO users (nome, email, idade) VALUES (%s, %s, %s)'
        cursor.execute(query, (user_datas["nome"], user_datas["email"], user_datas["idade"]))

    return jsonify(data=user_datas), 201


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_datas = request.json

    with connection_manager() as cursor:
        query = 'UPDATE users SET nome = %s, email = %s, idade = %s WHERE id = %s'
        cursor.execute(query, (user_datas["nome"], user_datas["email"], user_datas["idade"], id))

    return jsonify(data=user_datas), 200


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    with connection_manager() as cursor:
        query = 'DELETE FROM users WHERE id = %s'
        cursor.execute(query, (id,))

    return jsonify(data=id), 204

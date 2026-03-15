# Define a função de mapeamento para o usuário
def map_user(row):
    return {
        "id": row[0],
        "nome": row[1],
        "email": row[2],
        "idade": row[3]
    }

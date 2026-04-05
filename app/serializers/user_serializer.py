# Define a função de mapeamento para o usuário
def map_user(data):
    return {
        "id": data[0],
        "nome": data[1],
        "email": data[2],
        "idade": data[3]
    }

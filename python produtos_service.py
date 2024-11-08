from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados simulado para produtos
produtos_db = {}

# 1. Adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    data = request.get_json()
    nome = data['nome']
    preco = data['preco']

    if nome in produtos_db:
        return jsonify({"erro": "Produto já existe"}), 400

    produtos_db[nome] = {'preco': preco}
    return jsonify({"mensagem": "Produto adicionado com sucesso"}), 201

# 2. Listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos_db), 200

# 3. Buscar um produto pelo nome
@app.route('/produtos/<nome>', methods=['GET'])
def buscar_produto(nome):
    produto = produtos_db.get(nome)
    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404
    return jsonify({nome: produto}), 200

if __name__ == '__main__':
    app.run(port=5001)

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Banco de dados simulado para o estoque
estoque_db = {}

# URL do Microserviço de Produtos (para comunicação)
URL_PRODUTOS = 'http://localhost:5001/produtos'

# 1. Atualizar a quantidade de um produto
@app.route('/estoque', methods=['PUT'])
def atualizar_quantidade():
    data = request.get_json()
    nome = data['nome']
    nova_quantidade = data['quantidade']

    # Verificar se o produto existe no Microserviço de Produtos
    response = requests.get(f'{URL_PRODUTOS}/{nome}')
    if response.status_code == 404:
        return jsonify({"erro": "Produto não encontrado"}), 404

    # Atualizar a quantidade no estoque
    estoque_db[nome] = nova_quantidade
    return jsonify({"mensagem": "Quantidade atualizada com sucesso"}), 200

# 2. Remover um produto do estoque
@app.route('/estoque/<nome>', methods=['DELETE'])
def remover_produto(nome):
    # Verificar se o produto existe no Microserviço de Produtos
    response = requests.get(f'{URL_PRODUTOS}/{nome}')
    if response.status_code == 404:
        return jsonify({"erro": "Produto não encontrado"}), 404

    # Remover o produto do estoque
    if nome in estoque_db:
        del estoque_db[nome]
        return jsonify({"mensagem": "Produto removido do estoque"}), 200
    else:
        return jsonify({"erro": "Produto não está no estoque"}), 404

if __name__ == '__main__':
    app.run(port=5002)

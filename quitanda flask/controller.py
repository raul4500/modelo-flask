from flask import*
from model import*
import json

# Definição do Blueprint
produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/')
def mostrar_produtos():
    carrinho = request.cookies.get('carrinho')
    if carrinho:
        carrinho = json.loads(carrinho)
    else:
        carrinho = []

    return render_template('index.html', produtos=produtos, carrinho=carrinho)

@produto_bp.route('/adicionar/<int:produto_id>')
def adicionar_ao_carrinho(produto_id):
    carrinho = request.cookies.get('carrinho')
    if carrinho:
        carrinho = json.loads(carrinho)
    else:
        carrinho = []

    produto = obter_produto_por_id(produto_id)
    if produto and produto_id not in [item['id'] for item in carrinho]:
        carrinho.append({'id': produto.id, 'nome': produto.nome, 'preco': produto.preco})

    resp = make_response(redirect('/'))
    resp.set_cookie('carrinho', json.dumps(carrinho))

    return resp

@produto_bp.route('/remover/<int:produto_id>')
def remover_do_carrinho(produto_id):
    carrinho = request.cookies.get('carrinho')
    if carrinho:
        carrinho = json.loads(carrinho)
        carrinho = [item for item in carrinho if item['id'] != produto_id]

    resp = make_response(redirect('/'))
    resp.set_cookie('carrinho', json.dumps(carrinho))

    return resp

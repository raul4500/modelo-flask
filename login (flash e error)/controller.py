from flask import*      
from model import*
import time

app_controller = Blueprint('controller', __name__)

@app_controller.route('/')
def index():
    if 'nome' in session:
        return render_template('home.html', resposta=f'Bem-vindo {session["nome"]}', id=0)
    return render_template('index.html', resposta='Você não está logado', id=1)

@app_controller.route('/login', methods=['GET', 'POST'])
def login():
    if 'nome' in session: 
            return redirect(url_for('controller.index'))
    
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        session['senha'] = request.form['senha']
        if verificarUsuario(session['nome'],session['senha']) == True:
            flash('Formulario enviado com sucesso!', 'success')
            render_template('menssagem.html')
            time.sleep(3)
            return redirect(url_for('controller.index'))
        else:
            session.pop('nome', None)
    return render_template('login.html')

@app_controller.route('/logout')
def logout():
    session.pop('nome', None)
    return redirect(url_for('controller.index'))
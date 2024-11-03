from flask import*      
from model import*

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
        session.permanent = True
        session['nome'] = request.form['nome']
        senha = request.form['senha']
        if verificarUsuario(session['nome'],senha) == True:
            flash('Formulario enviado com sucesso!', 'success')
            return redirect(url_for('controller.index'))
        else:
            session.pop('nome', None)
    return render_template('login.html')

@app_controller.route('/logout')
def logout():
    flash(f'usuario {session['nome']} deslogado com sucesso!')
    session.pop('nome', None)
    return redirect(url_for('controller.index'))

@app_controller.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

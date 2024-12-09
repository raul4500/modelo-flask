from flask import*
from database import init_db
from repository import*
from datetime import*

app_controller = Blueprint('controller', __name__)

livroRepository = LivroRepository()
autorRepsotory = AutorRepository()
categoriaRepository = CategoriaRepository()

@app_controller.route('/')
def redirecionar():
    return redirect(url_for('controller.index'))

@app_controller.route('/livros', methods=['GET'])
def index():
    livros = livroRepository.getAllLivros()
    return render_template('index.html', livros=livros)

@app_controller.route('/add_livro', methods=['GET','POST'])
def adicionarLivro():
        if request.method == 'POST':
            titulo = request.form['titulo']
            isbn = request.form['isbn']
            data = request.form['data']
            data = datetime.strptime(data, '%Y-%m-%d').date()
            paginas = request.form['paginas']
            autor = request.form['autor']
            categoria = request.form['categoria']
            livroRepository.createLivro(titulo, isbn, data, paginas, autor, categoria)
        autores = autorRepsotory.getAllAutores()
        categorias = categoriaRepository.getAllCategorias()
        return render_template('add_livro.html', url='/add_livro', autores=autores, categorias=categorias)

@app_controller.route('/deletar/livro/<id>')
def deletarLivro(id):
        livroRepository.deleteLivro(id)
        return redirect(url_for('controller.index'))
    
@app_controller.route('/deletar/autor/<id>')
def deletarAutor(id):
        autorRepsotory.deleteAutor(id)
        return redirect(url_for('controller.adicionarAutor'))

@app_controller.route('/editar/livro/<id>', methods=['GET', 'POST'])
def editarLivro(id):
        if request.method == 'POST':
            titulo = request.form['titulo']
            isbn = request.form['isbn']
            data = request.form['data']
            paginas = request.form['paginas']
            livroRepository.updateLivro(id,titulo, isbn, data, paginas)
            return redirect(url_for('controller.index'))
        autores = autorRepsotory.getAllAutores()
        categorias = categoriaRepository.getAllCategorias()
        return render_template('add_livro.html', url=f'/editar/livro/{id}', autores=autores, categorias=categorias)
    
@app_controller.route('/editar/autor/<id>', methods=['GET', 'POST'])
def editarAutor(id):
        if request.method == 'POST':
            nome = request.form['nome']
            data = request.form['data_nascimento']
            nacionalidade = request.form['nacionalidade']
            data = datetime.strptime(data, '%Y-%m-%d').date()
            autorRepsotory.updateAutor(id, nome, data, nacionalidade)
            return redirect(url_for('controller.adicionarAutor'))
        autores = autorRepsotory.getAllAutores()
        return render_template('add_autor.html', url=f'/editar/autor/{id}', autores=autores, editar=True)
    
@app_controller.route('/add_autor', methods=['GET','POST'])
def adicionarAutor():
        if request.method == 'POST':
            nome = request.form['nome']
            nacionalidade = request.form['nacionalidade']
            data_nascimento = request.form['data_nascimento']
            data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            categoria = request.form['categoria']
            categoriaRepository.createCategoria(categoria)
            autorRepsotory.createAutor(nome, data_nascimento, nacionalidade)
        autores = autorRepsotory.getAllAutores()
        return render_template('add_autor.html', url='/add_autor', autores=autores)


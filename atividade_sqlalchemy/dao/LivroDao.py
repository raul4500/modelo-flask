from models import *

# classe dos livros com suas próprias funções (CRUD)

class LivroDao:
    @staticmethod
    def getLivro(id):
        return Livros.query.get(id)

    @staticmethod
    def getAllLivros():
        return Livros.query.all()

    @staticmethod
    def addLivro(titulo, isbn, datap, paginas, autor_id, categoria_id):
        livro = Livros(titulo=titulo, isbn=isbn, datap=datap, paginas=paginas, autor_id=autor_id, categoria_id=categoria_id)
        print(livro)
        db.session.add(livro)
        db.session.commit()
        return livro.toJson()

    @staticmethod
    def attLivro(id, titulo, isbn, datap, paginas):
        livro = LivroDao.getLivro(id)
        if livro:
            livro.titulo = titulo
            livro.isbn = isbn
            livro.datap = datap
            livro.paginas = paginas
            db.session.commit()
        return livro

    @staticmethod
    def delLivro(id):
        livro = LivroDao.getLivro(id)   
        if livro:
            db.session.delete(livro)
            db.session.commit()
        return livro

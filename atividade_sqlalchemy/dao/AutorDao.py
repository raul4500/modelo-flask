from models.Autor import *

# classe dos autores com suas próprias funções (CRUD)

class AutorDao:
    @staticmethod
    def getAutor(id):
        return Autor.query.get(id)

    @staticmethod
    def getAllAutores():
        return Autor.query.all()

    @staticmethod
    def addAutor(nome_autor, data_nascimento, nacionalidade):
        autor = Autor(nome_autor=nome_autor, data_nascimento=data_nascimento, nacionalidade=nacionalidade)
        db.session.add(autor)
        db.session.commit()
        return autor

    @staticmethod
    def attAutor(id, nome_autor, data_nascimento, nacionalidade):
        autor = AutorDao.getAutor(id)
        if autor:
            autor.nome_autor = nome_autor
            autor.data_nascimento = data_nascimento
            autor.nacionalidade = nacionalidade
            db.session.commit()
        return autor

    @staticmethod
    def delAutor(id):
        autor = AutorDao.getAutor(id)
        if autor:
            db.session.delete(autor)
            db.session.commit()
        return autor
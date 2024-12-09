from models import *

# classe das categorias com suas próprias funções (CRUD)

class CategoriaDao:
    @staticmethod
    def getCategoria(id):
        return Categoria.query.get(id)

    @staticmethod
    def getAllCategorias():
        return Categoria.query.all()

    @staticmethod
    def addCategoria(nome_categoria):
        categoria = Categoria(categoria=nome_categoria)
        db.session.add(categoria)
        db.session.commit()
        return categoria

    @staticmethod
    def attCategoria(id, nome_categoria):
        categoria = CategoriaDao.getCategoria(id)
        if categoria:
            categoria.nome_categoria = nome_categoria
            db.session.commit()
        return categoria

    @staticmethod
    def delAutor(id):
        categoria = CategoriaDao.getCategoria(id)
        if categoria:
            db.session.delete(categoria)
            db.session.commit()
        return categoria
from dao.CategoriaDao import *

class CategoriaRepository:
    def __init__(self) -> None:
        self.categoriaDao = CategoriaDao()

    def getAllCategorias(self):
        return self.categoriaDao.getAllCategorias()

    def getCategoria(self, id):
        return self.categoriaDao.getCategoria(id)

    def createCategoria(self, categoria):
        return self.categoriaDao.addCategoria(categoria)

    def updateCategoria(self, id , categoria):
        return self.categoriaDao.attCategoria(id, categoria)

    def deleteCategoria(self, id):
        return self.categoriaDao.delCategoria(id)

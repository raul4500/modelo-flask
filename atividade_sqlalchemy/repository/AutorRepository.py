from dao.AutorDao import *

class AutorRepository:
    def __init__(self) -> None:
        self.autorDao = AutorDao()

    def getAllAutores(self):
        return self.autorDao.getAllAutores()

    def getAutor(self, id):
        return self.userDao.getAutor(id)

    def createAutor(self, nome, data, nacionalidade):
        return self.autorDao.addAutor(nome, data, nacionalidade)

    def updateAutor(self, id, nome, data, nacionalidade):
        return self.autorDao.attAutor(id,nome, data, nacionalidade)

    def deleteAutor(self, id):
        return self.autorDao.delAutor(id)

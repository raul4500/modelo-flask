from dao.LivroDao import *

class LivroRepository:
    def __init__(self) -> None:
        self.livroDao = LivroDao()

    def getAllLivros(self):
        return self.livroDao.getAllLivros()

    def getLivro(self, id):
        return self.livroDao.getLivro(id)

    def createLivro(self,titulo, isbn, datap, paginas, autor_id, categoria_id):
        return self.livroDao.addLivro(titulo, isbn, datap, paginas,autor_id, categoria_id)

    def updateLivro(self, id, titulo, isbn, datap, paginas):
        return self.livroDao.attLivro(id, titulo, isbn, datap, paginas)

    def deleteLivro(self, id):
        return self.livroDao.delLivro(id)

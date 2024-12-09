from database import db
from sqlalchemy import*
from sqlalchemy.orm import*

class Livros(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    isbn = db.Column(db.String(80), unique=True, nullable=False)
    datap = db.Column(db.String(80), nullable=False)
    paginas = db.Column(db.String(80), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
 
    autor = db.relationship("Autor", back_populates="livro")
    categoria = db.relationship("Categoria", back_populates="livro")
    
    def __repr__(self):
        return f'{self.titulo} - {self.isbn} - {self.datap} - {self.paginas} - {self.autor} - {self.categoria}'

    def toJson(self):
        return {"id": self.id, "titulo": self.titulo, "isbn": self.isbn, "datap": self.datap, "paginas": self.paginas, 'autor': self.autor, 'categoria': self.categoria}
    
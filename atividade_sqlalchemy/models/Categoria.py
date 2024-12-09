from database import db
from sqlalchemy import*
from sqlalchemy.orm import*

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(80), nullable=False)
    livro = relationship("Livros", back_populates="categoria")

    def __repr__(self):
        return f'{self.categoria}'

    def toJson(self):
        return {"id": self.id, "categoria": self.categoria}

from database import db
from sqlalchemy import*
from sqlalchemy.orm import*

class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True)
    nome_autor = db.Column(db.String(80), nullable=False)
    data_nascimento = db.Column(db.String(80), nullable=False)
    nacionalidade = db.Column(db.String(80), nullable=False)
    
    livro = relationship("Livros", back_populates="autor")

    def __repr__(self):
        return f'{self.nome_autor} / {self.data_nascimento} / {self.nacionalidade}'

    def toJson(self):
        return {"id": self.id, "nome_autor": self.nome_autor, "data_nascimento": self.data_nascimento, "nacionalidade": self.nacionalidade}
    

    # Relacionamento: Um autor pode ter muitos livros
    


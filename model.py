from flask import*

class Modelo:
    def __init__(self, id, nome, altura, time, camisa):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.time = time
        self.camisa = camisa

mensagem = "hello world"
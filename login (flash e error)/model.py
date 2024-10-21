from flask import*

class Pessoa:
    def __init__(self,nome, senha):
        self.nome = nome
        self.senha = senha

def verificarUsuario(nome, senha):
    with open('/home/estudante1/flaskSP3114511/atividade login (sessao)/senha.dat','r') as arquivo:
        for linha in arquivo:
            dado = linha.split(',')
            if dado[0]==nome and dado[1]==senha:
                return True
        return False
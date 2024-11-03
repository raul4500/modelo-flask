from flask import*

class Pessoa:
    def __init__(self,nome, senha):
        self.nome = nome
        self.senha = senha

def verificarUsuario(nome, senha): 
    with open('senha.dat', 'r') as arquivo:
        for linha in arquivo:
            dado = linha.strip().split(',')
            if dado[0] == nome and dado[1] == senha:
                return True
        return False
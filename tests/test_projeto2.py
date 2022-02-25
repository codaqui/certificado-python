from submission.projeto2 import main

def test_texto():
  assert main.texto == 'texto'
  
def test_numero():
  assert main.numero == 2
  
def test_boolean():
  assert main.boleano == False
  
def test_conta_desafio_1():
  assert 90 < main.desafio1 < 100
  
def test_syntax_desafio():
  valido = False
  with open("submission/projeto2/main.py", "r") as file:
    temp = file.readlines()
    for line in temp:
      if 'desafio1' in line:
        line_array = list(line)
        if '+' in line_array or '-' in line_array or '*' in line_array or '/' in line_array:
          valido = True
  assert valido
  
def test_dinheiro():
  assert main.dinheiro == 7.5

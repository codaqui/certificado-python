from submission.projeto2 import main

def test_texto():
  assert main.texto == 'texto'
  
def test_numero():
  assert main.numero == 2
  
def test_boolean():
  assert main.boleano == False
  
def test_conta_desafio_1():
  assert 90 > main.desafio1 > 100
  
 

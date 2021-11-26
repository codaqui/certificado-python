from submission.projeto2 import main

def test_texto():
  assert main.texto == 'texto'
  
def test_numero():
  assert main.numero == 2
  
def test_boolean():
  assert main.boleano == False
  
def test_conta_desafio_1():
  assert 90 > main.desafio1 > 100
  
def test_syntax_desafio():
  # Abrir o arquivo submission.projeto2
  # with open(.....) as file
  # Achar a linha desafio1 = **^$#^%#
  # file.read(), achar a linha `desafio1 =`
  # split = -> validar o indice 1 do array
  # Verifica se nessa linha tem o valor 55, e possui uma operação valida. (+, -, , *, ^)
  assert True
  
 

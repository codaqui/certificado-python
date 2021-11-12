from submissão.projeto2 import main

def test_texto():
  assert main.texto == 'texto'
  
def test_numero():
  assert main.numero == 2

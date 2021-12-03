import os
from submission.projeto3 import main

def test_se_copiou_tarefa1():
  assert main.lista_de_compras == ['Banana', 'Arroz', 'Laranja']
  
def test_se_if_existe_tarefa1():
  with open('submission/projeto3/main.py', 'r') as file:
    tmp_file = file.read()
  verifica = False
  if "'Uva' in lista_de_compras" in tmp_file:
    verifica = True
  elif '"Uva" in lista_de_compras' in tmp_file:
    verifica = True    
  assert verifica

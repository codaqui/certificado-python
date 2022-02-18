import os
import dis
from submission.projeto3 import main

def test_se_copiou_tarefa1():
  assert main.lista_de_compras == ['Banana', 'Arroz', 'Laranja']
  
def test_se_if_existe_tarefa1():
  with open('submission/projeto3/main.py', 'rb') as file:
    temp = file.read()
    bytecode = compile(temp, 'submission/projeto3/main.py', 'exec')
    validate_1 = [0, False]
    validate_2 = [0, False]
    validate_3 = [0, False]
    validate_4 = [0, False]
    validate_5 = [0, False]
    for index, line in enumerate(dis.Bytecode(bytecode)):
      if line.opname == 'LOAD_CONST' and line.argval == 'Uva':
        validate_1[0] = index
        validate_1[1] = True
      if line.opname == 'LOAD_NAME' and line.argval == 'lista_de_compras' and index > validate_1[0] and validate_1[1]:
        validate_2[0] = index
        validate_2[1] = True
      if line.opname == 'COMPARE_OP' and line.argval == 'in' and index > validate_2[0] and validate_2[1]:
        validate_3[0] = index
        validate_3[1] = True
      if line.opname == 'POP_JUMP_IF_FALSE' and index > validate_3[0] and validate_3[1]:
        validate_4[0] = index
        validate_4[1] = True
      if line.opname == 'LOAD_NAME' and line.argval == 'print' and index > validate_4[0] and validate_4[1]:
        validate_5[0] = index
        validate_5[1] = True
  assert validate_1[1] and validate_2[1] and validate_3[1] and validate_4[1] and validate_5[1]
      

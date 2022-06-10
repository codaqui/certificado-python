# Certificação Trilha de Conhecimento Python

Esse repositório serve de exercicio para você concluir os seus estudos em Python seguindo a [trilha de estudos](https://github.com/codaqui/institucional-trilhas-estudos/blob/main/guias/programador-python.md) da Codaqui.

## Já estudou?! Se sente preparado?! Vamos lá!

**Observações**:

- Realize todos os projetos abaixo. Não precisa ser em ordem, mas deverá realizar todos para concluir o curso e adquirir o certificado.
- A correção automática não é garantia de que está tudo correto, fique atento na aba **Pull Requests** um mentor irá acompanhar o seu desenvolvimento.
- Qualquer dúvida, entre no nosso Discord e procure um mentor para ajudar.

## Projetos

<details>
<summary>Projeto 1 - Iniciando os trabalhos!</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto1.py`.
2. O seu arquivo `projeto1.py` deverá exibir um `Hello World!` quando executado.

</details>

---

<details>
<summary>Projeto 2 - Variáveis e Tipos de Variáveis</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto2.py`.
2. O seu arquivo deverá em ordem:

```text
- Definir uma variável chamada 'texto' com o valor de 'texto'.
- Definir uma variável chamada 'numero' com o valor de 2.
- Definir uma variável chamada 'boleano' com o valor de False.
- Crie uma conta que realize uma operação (soma, subtração, multiplicação ou divisão) com o numero 55 e o resultado deverá ser maior que 90 e menor que 100. Você deverá salvar isso em uma variável chamada 'desafio1'.
- Definir uma variável chamada `dinheiro` que represente o valor de R$7,50 e que possamos utilizar essa variável em uma equação.
```

</details>

---

<details>
    <summary>Projeto 3 - Estruturas Lógicas e Condicionais</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto3.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

<details>
<summary>Exercicio 1</summary>

- Copie o codigo abaixo e cole no arquivo.

```python
lista_de_compras = ['Banana', 'Arroz', 'Laranja']
```
 
</details>

<details>
<summary>Exercicio 2</summary>

- Crie um código que verifica o objeto `Uva` existe na `lista_de_compras`, caso existe utilize print para algum texto. Faça a verificação logo após definir a lista.

</details>

<details>
<summary>Exercicio 3</summary>

- Copie o codigo abaixo e cole no mesmo arquivo, logo após a ultima resposta..

```python
lista_de_numeros = [50, 60, 834241542, 5433302]
```

</details>

<details>
<summary>Exercicio 4</summary>

- Verifique se a soma dos números em `lista_de_numeros` é maior do que `86422542`, caso seja `print('soma é maior')`.

</details>

<details>
<summary>Exercicio 5</summary>

- Dado a seguinte lista

```python
lista_de_numeros = range(100)
```

Exiba uma sub lista chamada `lista_par` dos números da `lista_de_numeros` que são pares, e outra sub lista chamada `lista_impar` com os impares.

</details>

<details>
<summary>Exercicio 6</summary>

- Tempo e Data (Origem: https://pense-python.caravela.club/05-condicionais-e-recursividade/14-exercicios.html)

O módulo time fornece uma função, também chamada time, que devolve a Hora Média de Greenwich na “época”, que é um momento arbitrário usado como ponto de referência. Em sistemas UNIX, a época é primeiro de janeiro de 1970.

```bash
>>> import time
>>> time.time()
1437746094.5735958
```
Escreva um script que leia a hora atual e a converta em um tempo em horas, minutos e segundos, mais o número de dias desde a época.

</details>


</details>

---

<details>
<summary>Projeto 4 - Estrutura de Repetição</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto4.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Dada a seguinte lista abaixo.
2. Crie um código que seja capaz de imprimir(_print_) todos os valores contidos na lista. 

 ```python
nomes = ["Enderson", "Luiz Fernando", "Pedro", "Isis", "Kamily", "Bianca", "Mell Steissy", "Caio"]
 ```


</details>

---
<details>
<summary>Projeto 5 - Coleções em Python</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto5.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Copie e cole a lista a seguir dentro do seu código.
2. Com a lista declarada, remova o primeiro e segundo index da `lista_de_numeros`.
 
 ```python
lista_de_numeros = [12, 23, 34, 45]
 ```
 
 
1. Defina a tupla a seguir.
2. Crie um código capaz de verificar qual time não possui Mundial.
3. Crie uma lista com os times que restarem da verificação.  
 
 ```python
times_com_mundial = ('Corinthians', 'Santos', 'Palmeiras', 'Flamengo')
 ```
 
1. Dado o seguinte conjunto, uma lista de dicionários.
2. Crie um código que seja capaz de printar o curso que Milena está realizando. 
 
 ```python
dados_do_aluno_1 = {
    'Nome': 'Milena',
    'Curso': 'Programação',
    'Turno': 'tarde',
    'Telefone': '9999999'
}
dados_do_aluno_2 = {
    'Nome': 'Vitor',
    'Curso': 'Design de Aplicativos',
    'Turno': 'tarde',
    'Telefone': '9999999'
}
lista_de_alunos = [dados_do_aluno_1, dados_do_aluno_2]
 ```

</details>

---
<details>
<summary>Projeto 6 - Funções</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto6.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Dado o conhecimento de Movimento Retilinio Uniforme, e lembrando da equação `S = S0 + v.t` escreva um programa que responda todos os casos da tabela abaixo.

| Espaço Final | Espaço Inicial | Velocidade | Tempo |
| ------------ | -------------- | ---------- | ----- |
| ? | 100 metros | 10 metros | 10 metros/segundo | 10 segundos |
| ? | 75 metros | 5 metros | 12 metros/segundo | 5 segundos |
| ? | 150 metros | 25 metros | 15 metros/segundo | 25 segundos |

Dica: Crie uma função, e execute essa mesma função várias vezes com parametros diferentes.

2. Crie uma função que dado uma palavra, a sua função irá sempre retorna a mesma palavra, porém todas as letras em minusculo.

| Parametro | Retorno |
| --------- | ------- |
| HORA | hora |
| HoRa | hora |
| DeSCulpA | desculpa |

</details>

---
<details>
<summary>Projeto 7 - Comprehensions em Python</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto6.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Crie utilizando apenas uma linha, uma lista chamada `numeros`, e essa lista vai conter todos os numeros de 1 a 10 multiplicado por 2.


```python
# Dica
numeros = [para cada numero de range(1,10) multiplique esse numero por 2]
```

2. Crie utilizando apenas uma linha, uma lista chamada `numeros_pares`, que contenha todos numeros pares de 0 a 100.

```python
# Dica
numeros = [ quero numero dentro de uma lista de 0,100 que % 2 seja 0 ]
```

3. Crie utilizando apenas uma linha, uma lista chamada `possui_a`, que verifique os valores da lista_de_compras, retornando `True` quando a palavra possui a letra `a` e `False` quando não.

```
lista_de_compras = ['Banana', 'Abacate', 'Uva', 'Melão', 'Colher', 'Ovo', 'Queijo']
# Dica
possui_a = [ verdadeiro quando a palavra tem a e falso quando não tem para todas as palavras da lista]
```


</details>

---
<details>
<summary>Projeto 8 - Expressões Lambdas e Funções Integradas</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto7.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Crie uma função lambda que some dois numeros.
2. Dada a lista abaixo, utilize `map` e uma função `lambda` para multiplicar todos os valores por 2.

```python
lista_de_numeros = [2, 4, 6, 8]
```


</details>

---
<details>
<summary>Projeto 9 - Debugando e Tratando Erros</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto9.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Crie uma função que some dois valores, quando o usuário digitar um valor que não seja `float` ou `int` você irá dar `print` em uma mensagem de erro e não deixando o interpretador retornar erro.
2. Crie um programa que a pessoa possa consultar alunos, dado o dicionário abaixo, se a pessoa digitar um nome que não existe, retorne uma mensagem de erro sem deixar o interpreador retornar o erro.

```python

dict_alunos = {
  'joao' : { 'nome': 'joao', 'idade': 14 },
  'maria' : { 'nome': 'maria', 'idade': 14 },
}
```


</details>

---

<details>
<summary>Projeto 10 - Trabalhando com Modulos</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto10.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Crie um modulo chamado `calculadora`, dentro desse modulo crie dois submodulos: `somar` e `dividir`, cujo possuam as funções `somar_dois_numeros` e `dividir_dois_numeros`, fazendo com que o código abaixo passe a funcionar.

```python
from calculadora.somar import somar_dois_numeros
from calculadora.dividir import dividir_dois_numeros

somar_dois_numeros(2,2)
dividir_dois_numeros(4,2)
```

</details>

---
<details>
<summary>Projeto 11 - Leitura e Escrita em Arquivos</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto11.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Crie um arquivo `texto.txt` e insira uma contagem de números de 0 a 10.
2. Crie uma lista de dicionários simulando um cadastro de usuário, contendo `usuario, senha` e salve em um json nomeado: `top_secret.json`.
3. Crie um CSV com as colunas Materia | Nota | Bimestre, faça esse csv ser capaz de salvar dados de notas escolares.

</details>

---
<details>
<summary>Projeto 12 - Iteradores e Geradores</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto12.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:
    
**Exercicios**:
1. Crie utilizando um iterador/gerador um código capaz de exibir 15 números da sequencia de Fibonacci.
2. Crie utilizando um iterador/gerador um código capaz de verificar números divisíveis por 10 sem conter resto.


</details>

---
<details>
<summary>Projeto 13 - Decoradores</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto13.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:

1. Crie um decorador que possa fazer com que as funções abaixo, sempre que executadas exibam um print('Nome da função'), chame seu decorador de `meu_decorador_log`.

```python
def somar_dois_numeros(a,b):
  return a + b
  
def dividir_dois_numeros(a,b):
  return a / b
```

</details>
---
<details>
<summary>Projeto 14 - Orientação da Objetos</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto12.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:



</details>
---
<details>
<summary>Projeto 15 - Herança e Polimorfismo</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto12.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:



</details>
---
<details>
<summary>Projeto 16 - Teste</summary>

1. Dentro da pasta `projetos` crie o arquivo `projeto12.py`.
2. O seu arquivo deverá em ordem executar os exercicios abaixo:

**Exercicios**:



</details>

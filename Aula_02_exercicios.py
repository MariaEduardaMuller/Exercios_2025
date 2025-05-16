#1- Peça ao usuário para digitar 5 números e mostre a soma deles ao final.
numero1 = int (input(”digite o primeiro número:”))
numero2 = int (input(”digite o primeiro número:”))
numero3 = int (input(”digite o primeiro número:”))
numero4 = int (input(”digite o primeiro número:”))
numero5 = int (input(”digite o primeiro número:”))

soma = numero1+ numero2 + numero3 + numero4 + numero5 

Print (f”A soma dos 5 numeros é: {soma} ”)

#2- Peça ao usuário para digitar 4 números e mostre qual é o maior e qual é o menor.

numero1 = int (input(”digite o primeiro número:”))
numero2 = int (input(”digite o primeiro número:”))
numero3 = int (input(”digite o primeiro número:”))
numero4 = int (input(”digite o primeiro número:”))
numero5 = int (input(”digite o primeiro número:”))

listaDeNumeros = [numero1, numero2, numero3, numero4]

ListaDeNumeros.sort(reverse = false)
print (f”O menor numero é: {listadenumeros[0]/n O maior numero é: [lista de 

#3-Peça ao usuário uma palavra e mostre quantas vogais ela tem.

palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
quantidade = 0

for letra in palavra: 
    if letra in vogais:
        quantidade += 1

print(f"A palavra '{palavra}' tem {quantidade} vogais.")

#outro jeito:

palavra = input("Digite uma palavra: ")
vogais = [‘‘a’’, ‘‘e’’, ‘‘i’’, ‘‘o’’, ‘‘u’’]
contador = 0
           for letra in palavra:’
               for vogal in vogais: 
                  if(letra == vogal):
                     contador = contador + 1

print (f ‘’a quantidade de vogais na palavra {palavra} é de: {contador}’’)

#4- Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))
numero6 = int(input("Digite o sexto número: "))

numeros = [numero1, numero2, numero3, numero4, numero5, numero6]

for numero in numeros:
    if numero % 2 == 0:
        print(f"Número par: {numero}")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))
numero6 = int(input("Digite o sexto número: "))

listaDePares = []

listadeNumeros = [numero1, numero2, numero3, numero4, numero5, numero6]

for numero in listaDeNumeros:
  if numero% 2 == 0:
     listaDePares.append(numero)

if len (listaDePares) !=0:

print(f’’Os numeros pares digitados foram: {listaDePares}’’)
else:
print(‘’A lista não tem nenhum número par!’’)

#5- Solicite as notas de 4 provas e mostre a média.
nota1 = float (input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))
nota3 = float (input("Digite a terceira nota: "))
nota4 = float (input('Digite a quarta nota:'))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f ‘’A media das notas {nota1}, {nota2}, {nota3}, {nota4} é: {média}’)


#6- Peça ao usuário um número e mostre a tabuada desse número de 1 a 10.

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

outro jeito:
numero = int(input("Digite um número para visualizar a tabuada desse numero: "))
for numero in range(1, 11): 
  print(f”{numeroDigitado} x {numero} = {numeroDigitado * numero}”)

#7- Peça um número N ao usuário e mostre todos os números de 1 até N.

n = int(input("Digite um número: "))

for i in range(1, n+1):
    print(i)

#8- Peça ao usuário uma palavra e mostre ela ao contrário.

palavra = input("Digite uma palavra: ")

print(f"A palavra ao contrário é: {palavra[::-1]}")

#9- Peça um número ao usuário e diga se ele é múltiplo de 3.

numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print(f"{numero} é múltiplo de 3.")
else:
    print(f"{numero} não é múltiplo de 3.")

#10- Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética.

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")

listaDeNomes = [nome1, nome2, nome3]
listaDeNomes.sort()

print("Nomes em ordem alfabética:")
for nome in listaDeNomes:
    print(nome)

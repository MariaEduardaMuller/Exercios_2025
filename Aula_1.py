idade = int (input('Qual a sua idade?'))
 
if idade <12:
    print ('criança')
elif idade >=12 and idade <=17:
    print ('adolescente')
if idade > 18:
    print('adulto')





#2.Maior de dois números
solicite dois números ao usuário e exiba o maior deles. Caso sejam iguais, informe isso

# Solicita ao usuário dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os dois números
if numero1 > numero2:
    print(f"O maior número é {numero1}")
elif numero2 > numero1:
    print(f"O maior número é {numero2}")
else:
    print("Os dois números são iguais.")



#3.Verificação de vogal ou consoante
peça ao usuário para digitar uma letra e informe se é uma vogal (a, e, i, o, u) ou consoante 

# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ").lower()

# Verifica se a entrada é uma letra
if letra.isalpha() and len(letra) == 1:
    # Verifica se a letra é uma vogal
    if letra in 'aeiou':
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")
else:
    print("Por favor, digite apenas uma letra válida.")



#4.Comparação de senhas 
solicite ao usuários que defina uma senha e, em seguida, peça para confirmá-la 
caso as senhas sejam iguais, exiba “acesso permitido”, senão, exiba “senhas não coincidem

# Solicita ao usuário para definir uma senha
senha = input("Defina uma senha: ")

# Solicita a confirmação da senha
confirmacao_senha = input("Confirme a senha: ")

# Compara as senhas
if senha == confirmacao_senha:
    print("Acesso permitido")
else:
    print("Senhas não coincidem")

#6.Escreva um programa que leia 3 números inteiros e imprima na tela os valores em ordem decrescente
# Leitura dos 3 números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Coloca os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Imprime os números em ordem decrescente
print("Os números em ordem decrescente são:", numeros)


#7. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12km por litro. Para obter o cálculo, o usuário deve formatar o tempo gasto na viagem e a velocidade média. Desta forma, será possível obter a distância percorrida com a fórmula DISTÂNCIA = TEMPO + VELOCIDADE. Tendo o valor da distancia, basta calcular quantidade de litros de combustível utilizado na viagem com a fórmula: LITROS_USADOS = DISTÂNCIA / 12. o programa deve apresentar os valores da velocidade média. tempo gasto, a distância percorrida e a quantidade de litros utilizando na viagem. Dica: trabalhe com valores reais

# Entrada de dados
tempo_gasto = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))

# Cálculo da distância percorrida (DISTÂNCIA = TEMPO * VELOCIDADE)
distancia_percorrida = tempo_gasto * velocidade_media

# Cálculo da quantidade de litros de combustível usados (LITROS_USADOS = DISTÂNCIA / 12)
litros_usados = distancia_percorrida / 12

# Exibição dos resultados
print(f"\nVelocidade média: {velocidade_media} km/h")
print(f"Tempo gasto: {tempo_gasto} horas")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Quantidade de litros de combustível utilizados: {litros_usados:.2f} litros")1.classificação de idade 
peça a idade do usuário e classifique-o de acordo com a tebela: 
menor de 12 anos - criança 
entre 12 e 17 anos - adolescente 
18 anos ou mais - adulto

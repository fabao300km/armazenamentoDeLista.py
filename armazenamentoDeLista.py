import random

# Como não especificado os número foi Gerando uma lista com 50 números aleatórios entre 1 e 100
numeros = [random.randint(1, 100) for _ in range(50)]

# Imprimindo a lista gerada (para visualização) aqui o usuário tem a visão dos numeros que estão na lista
print("Lista de 50 números gerados:")
print(numeros)

# Verificando se há números repetidos e em quais posições 
repetidos = {}

# Percorrendo a lista para identificar repetições e suas posições
for i, num in enumerate(numeros):
    if num not in repetidos:
        repetidos[num] = [i]  # Armazena a posição onde o número aparece pela primeira vez
    else:
        repetidos[num].append(i)  # Adiciona outras posições onde o número aparece

# Mostrando os números que se repetem e suas posições
print("\nNúmeros repetidos e suas posições na lista:")
for num, posicoes in repetidos.items():
    if len(posicoes) > 1:  # Se o número se repetiu mais de uma vez
        print(f"Número {num} repetido nas posições: {posicoes}")
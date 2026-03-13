# revisão do exercício de aula #1
print("Bom dia")

# revisão do exercício de aula #2
#%%
# SOMA 1 + 1
print("1 + 1 =", 1 + 1)

#%%
# SUBTRAÇÃO (10 - 5)
print("10 - 5 = ", 10-5)

#%%
# MULTIPLICAÇÃO (10 e 5)
print("10 * 5 =", 10*5)

#%%
# DIVISÃO (10 e 3)
print("10 / 3 =", 10/3)

#%%
# DIVISÃO COM INTEIRA PARTE (10 e 3)
print("10 // 3 =", 10//3)

#%%
# RESTO DA DIVISÃO (10 e 4)
print("10 % 4 =", 10%4)

#%%
# POTÊNCIA (3 e 4)
print("3 ** 4 =", 3**4)

# Faça um programa que de bom dia, pergunta o nome da pessoa e responde que é um prazer conhecer ela,
# citando o nome da pessoa.
#%%
nome = input("Bom dia! Qual é o seu nome?")
print("Muito prazer em te conhecer,", nome)

# Faça um programa que receba um número inteiro e 
# calcule sua raiz quadrada e exiba o resultado.
#%%
numero = input("Por favor, escolha um número inteiro e digite a seguir:")
numero = int(numero)
print("A raiz quadrada do", numero, "é", numero ** (1/2))

# Faça um programa que exiba o dobro de um número inserido pelo usuário.
#%%
numero = input("Escolha um número para apresentarmos o seu dobro:")
numero = int(numero)
dobro = numero * 2
print("O dobro de", numero,"é", dobro, ".")

#%%
# Faça um programa que receba 4 alturas usando um laço 
# de repetição e realize a soma dessas alturas.

soma = 0
entrada = 0

while entrada <= 3:
    altura = input("Qual é a sua altura em metros?")
    soma += float(altura)
    entrada += 1

print("O total de alturas é:", soma)
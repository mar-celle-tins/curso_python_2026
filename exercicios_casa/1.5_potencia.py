#Faça um programa que receba dois valores A e B. Faça a potência desses dois valores e retorne o resultado:
# a ^ b = z

#%%
valor_a = input("Olá! Por favor, escolha um número:")
valor_a = int(valor_a)

valor_b = input("Agora escolha outro número, por favor:")
valor_b = int(valor_b)

potencia = valor_a ^ valor_b
print("A potência dos dois valores escolhidos por você é:", potencia)
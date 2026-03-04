#Faça um programa que receba o raio de uma circunferência em centímetros. Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.
# Área:  x.xx
# Perímetro:  y.yy

#%%
raio = input("Insira o raio da circunferência em centímetros, por favor:")
raio = int(raio)
area = 3,14 * (raio**2)
perimetro = 2 * 3,14 * raio

print("Com base na medida do seu raio, a área do seu círculo é de", area, "cm2 e o perímetro é de", perimetro, "cm.")

# DÚVIDA: ao testar meu código, a área retornou um número desse tipo ("3,1400")
# e o perímetro retornou um número desse tipo ("6,140"). Como eu posso determinar 
# o número de casas decimais que eu quero? E por que os números aparecem entre parênteses?
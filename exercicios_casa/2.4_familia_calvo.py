# Faça um programa que verifique se a pessoa pertence à família “calvo”.

#Resolução
#1. Perguntar se algum sobrenome da pessoa começa com a letra C.
#2. Caso não, informar que ela não pertence à família Calvo.
#3. Caso sim, pedir que a pessoa digite o sobrenome.
#4. Comparar o sobrenome digitado com o sobrenome Calvo. 
#5. Se for diferente, apresentar mensagem que informe que a pessoa não pertence à famiília.
#6. Se for igual, informar que a pessoa pertence à família. 

#%%
letra = input("""
      Olá! Você possui algum sobrenome cuja letra incial é "C"?
      (1) Sim
      (2) Não
      """)

letra = int(letra)
if letra == 2:
    print("Poxa, você não faz parte da família Calvo.")
elif letra == 1:
    sobrenome = input("Por favor, digite o seu sobrenome cuja letra inicial é C:")
    if sobrenome == "Calvo":
        print("Que legal! Você faz parte da família Calvo.")
    else:
        print("Poxa, você não faz parte da família Calvo.")
else:
    print("Inválido. Por favor, escolha uma opção válida.") 
          
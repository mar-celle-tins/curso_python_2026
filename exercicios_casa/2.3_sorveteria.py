#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago

#%%
tipo = input("""
             Olá! Por favor, digite a opção do tipo de sorvete que deseja: 
             (1) casquinha - R$1,00
             (2) cascão - R$2,50
             (3) cestinha - R$4,00
             """)
tipo = int(tipo)

valor_tipo = 0
if tipo == 1:
    valor_tipo = 1.0
elif tipo == 2:
    valor_tipo = 2.5
elif tipo == 3:
    valor_tipo = 4.0
else:
    print("Escolha uma das opções para prosseguir com o seu pedido")

sabor = input("""
              Agora, por favor escolha o sabor do seu sorvete:
              (1) morango
              (2) creme
              (3) chocolate
              """)
sabor = int(sabor)

cobertura = input("""
                  Por fim, escolha se deseja cobertura e de qual tipo:
                  (0) sem cobertura - R$0,00
                  (1) caramelo - R$1,50 
                  (2) morango - R$1,50
                  (3) chocolate - R$1,50
                  """)
cobertura = int(cobertura)

valor_cobertura = 0
if cobertura == 0:
    valor_cobertura = 0
elif cobertura == 1 or 2 or 3:
    valor_cobertura = 1.5
else:
    print("Escolha uma das opções para prosseguir com o seu pedido")

valor_total = valor_tipo + valor_cobertura

print("Muito bem! O valor total do seu pedido é R$", valor_total)
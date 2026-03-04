#%%
# Otimização de código
# Operações lógicas consomem poder de processamento (tempo) do PC.
# O "else" ajuda a otimizar o processamento da comparação lógica.

idade = 16

if idade >= 18:
    print("Você pode beber cerveja!")
    print("Beba com moderação.")
    #Esses quatro espaços no começo são chamados de identação.

else: #está conectado com o "if". Só será executado se o "if" for falso.
    print("Você ainda não pode beber!") 
    print("Vá para casa beber leite!")

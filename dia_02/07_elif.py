#%%

#Quando o sistema encontrar a primeira resposta verdadeira, 
# ele vai ignorar todo o restante da estrututra do if.

idade = 17

if idade >= 70:
    print("Cuidado com a bebida!")
    print("Converse com o seu geriatra.")

elif idade >= 18: #"elif" está vinculado a um "if".
    print("Você pode beber cerveja!")
    print("Beba com moderação.")
        #Esses quatro espaços no começo são chamados de identação.

elif idade <= 17:
    print("Você ainda não pode beber cerveja. Fique no Refri!")

else: #está conectado com o "if". Só será executado se o "if" for falso.
    print("Você ainda não pode beber!") 
    print("Vá para casa beber leite!")


#Isso se chama código espagueti. Não é a melhor prática.
  # else:
  # if idade >= 18:
  #         print("Você pode beber cerveja!")
  #         print("Beba com moderação.")
            #Esses quatro espaços no começo são chamados de identação.

  #     else: #está conectado com o "if". Só será executado se o "if" for falso.
  #         print("Você ainda não pode beber!") 
  #         print("Vá para casa beber leite!")
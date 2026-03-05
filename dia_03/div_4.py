# número divisível por 4: %4 = 0 (o resto da divisão é 0)

#Quais números são divisíveis por 4
# no intervalo [4-100]?

#%%
count = 4
while count <= 100:
    resto = count % 4
    if resto == 0: #comparando o resto
        print(count)

    
    count += 1 #significa count = count + 1


#%%
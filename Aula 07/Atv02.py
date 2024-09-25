#Dicionario
Lista = [1,6,9] #Cochetes
Tupla = (3,7,8) #Parenteses
Dicionario = {
    "Professor":"Gustavo",
    "Diciplina":"Versionamento",
    "Aluno":"Richard",
    "Ano":2024
    } #Chaves
#print(Lista[2])
#print(Tupla[2])
#print(Dicionario.keys())
#print(Dicionario.values())
#print(type(Dicionario))
#for x in Dicionario.keys():
    #print("{:>10}{:>16}".format("Chaves:", x))
#for x in Dicionario.values():
    #print("{:>10}{:>16}".format("Valores:", x))
Chave = [x for x in Dicionario.keys()]
Valor = [x for x in Dicionario.values()]
x = 0
while(x<len(Lista)):
    print("{:<12}{:<10}".format(Chave[x],Valor[x]))
    x += 1
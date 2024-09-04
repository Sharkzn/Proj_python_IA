#Criar as variaveis: Idade e tem_convite
idade = int(input("Digite sua Idade: "))
tem_convite = True #bolofofo

if idade >= 18:
    if tem_convite:
        print("Pode entrar no baile da DZ7")
    else:
        print("Precisa de um Convite pra entrar no baile.")
else:
    print("Não pode entar. É menor de idade.")
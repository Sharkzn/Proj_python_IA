Produto ={
    "ID:":2024001,
    "Produto:":"Maça",
    "Preço:":"R$5.50",
    "Validade:":"25/09/2024"
}
Chave = [x for x in Produto.keys()]
Valor = [x for x in Produto.values()]
x = 0
while(x<len(Chave)):
    print("{:<10}{:<10}".format(Chave[x],Valor[x]))
    x += 1
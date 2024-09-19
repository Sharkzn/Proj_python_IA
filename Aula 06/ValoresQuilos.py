Peso = [20,30,55,60,80,90,120,130,170,1000]
Terra = [round(x * 9.81, 2) for x in Peso]
Lua = [round(x * 1.62, 2) for x in Peso]
Marte = [round(x * 3.71, 2) for x in Peso]
Mercúrio = [round(x * 3.7, 2) for x in Peso]
print("{:<4}{:<8} {:<8} {:<8}".format("N°", "Terra", "Lua", "Marte", "Mercúrio"))
print("__|_________|________|__________|")
for x in range(len(Terra)):
    print("{:<4} {:<8} {:<8} {:<8}".format(x + 1, Terra[x], Lua[x], Marte[x], Mercúrio[x]))
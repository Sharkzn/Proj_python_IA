Metros = [4, 7, 12, 14, 16, 17, 24, 44, 88, 100]
Polegadas = [round(x * 39.37) for x in Metros]
Pés = [round(x * 3.281) for x in Metros]
Jardas = [round(x * 1.094) for x in Metros]
Milhas = [round(x / 1852) for x in Metros]
print("{:<4}{:<6}  {:<12}{:<8}{:<8}{:<8}".format("N°", "Metros", "Polegadas", "Pés", "Jardas", "Milhas"))
print("__|_______|__________|_______|________|_______|")
for x in range(0,len(Metros)):
    print("{:<4} {:<6} {:<12} {:<8} {:<8} {:<8}".format(x + 1, Metros[x], Polegadas[x], Pés[x], Jardas[x], Milhas[x]))

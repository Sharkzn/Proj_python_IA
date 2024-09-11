class Conversao:
    def Velocidade():
        Kmh = [75.4,30.6,120,32.8,20.8]
        Mph = [round(x/1.61,2) for x in Kmh]
        x = 0
        while(x<5):
            print(Kmh[x], "Anos em meses são", Mph [x] )
            x += 1
    
    def Temperatura():
        Celsius = [45,30,12.5,32.6,50]
        Fahrenheit = [round((x*1.8)+32,2) for x in Celsius]
        x = 0
        while(x<5):
            print(Celsius[x], "Celsius em fahrenheir são", Fahrenheit [x] )
            x += 1
    
    def Altura ():
        Pés = [32,46,51,67,78,81,89,91,95,100]
        Metros = [round((x*1)*0.3048,2 ) for x in Pés]
        x = 0
        while(x<5):
            print(Pés[x], "Pés em Metros são:", Metros [x] )
            x += 1
    
    def Idade():
        Anos = [12,29,45,2,5,18]
        Mês = [round(x*12,2) for x in Anos]
        x = 0
        while(x<5):
            print(Anos[x], "Anos em meses são", Mês [x] )
            x += 1
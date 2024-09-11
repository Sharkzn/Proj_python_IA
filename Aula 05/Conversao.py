class Conversao:
    Kmh = [75.4,30.6,120,32.9,20.8]
    Mph = []

    def Velocidade():
        Kmh = [75.4,30.6,120,32.8,20.8]
        Mph = []
        for x in Kmh:
            Mph.append(round(x/1.61,2))
        return Mph
    
    def Temperatura():
        Celsius = [45,30,12.5,32.6,50]
        Fahrenheit = []
        for x in Celsius:
            Fahrenheit.append(round((x*1.8)+32,2))
        return Fahrenheit
    
    def altura ():

        Pés = [32,46,51,67,78,81,89,91,95,100]
        Metros = []
        for x in Pés:
            Metros.append(round((x*1)*0.3048,2))
        return Metros
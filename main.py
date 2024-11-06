import math
ladoA=float(input("ingrese el lado A del triangulo: "))

ladoA=((math.sqrt(3))/4*math.pow(ladoA, 2))
if ladoA<1000:
    decimal=str(input("quieres el resultado con decimales o enteros?: "))
    if decimal.lower()=="decimales": 
        print(f"el area es: {ladoA}")
    elif decimal.lower()=="enteros":
        area=round(ladoA)
        print(f"el area es: {area}")
    else:
        print("palabra mal escrita")
else:
    print("DATOS NO VALIDOS")
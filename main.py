suma=0
for i in range(1,4):
    voltajes=float(input(f"enter the diferent voltage {i} : "))
    suma+=voltajes
promedio=suma/3
print(promedio)
if promedio>220:
    print("PELIGRO")
elif promedio>115 and promedio<220:
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")
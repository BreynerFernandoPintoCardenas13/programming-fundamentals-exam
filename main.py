suma=0
for i in range(1,6):
    voltajes=float(input(f"enter the voltage {i} : "))
    suma+=voltajes
promedio=suma/5
print(promedio)
if promedio>220:
    print("ALTO VOLAJE")
else:
    print("VOLTAJE CORRECTO")
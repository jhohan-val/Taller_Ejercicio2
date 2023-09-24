import os

Salpicones = []

os.system("cls")
print("*****************************************************")
n = int(input("\nDigita la cantidad de frutas que llevara el salpicon: "))

os.system("cls")
for i in range (n):
    salpicon = {}
    salpicon["id"] = i + 1
    salpicon["nombre"] = input("Ingresa el nombre de la fruta: ")
    salpicon["precioUnitario"] = float(input(f"Ingresa el precio unitario: "))
    salpicon["cantidad"] = int(input(f"Ingresa la cantidad de que desea: "))
    Salpicones.append(salpicon)
    print("\n")
    os.system("cls")
costoTotal = 0
os.system("cls")
for fruta in Salpicones:
    costoTotal += fruta["precioUnitario"] * fruta["cantidad"]
print("*****************************************************")
print("\nCosto total del salpicón:", costoTotal,"\n")

ordenarFrutas = sorted(Salpicones, key=lambda x: x["precioUnitario"], reverse=True)
for fruta in ordenarFrutas:
    print(f"{fruta['nombre']}: ${fruta['precioUnitario']:.2f} por unidad")

def ordenarFrutas (frutas):
    frutasOrdenadas = sorted(frutas, key=lambda x: x["precioUnitario"])
    frutaMasBarata = frutasOrdenadas[0]
    frutaMasCara = frutasOrdenadas[-1]
    return frutaMasBarata, frutaMasCara

frutaBarata, frutaCara = ordenarFrutas(Salpicones)
print("\nFruta más barata:", frutaBarata["nombre"])
print("Fruta más cara:", frutaCara["nombre"],"\n")
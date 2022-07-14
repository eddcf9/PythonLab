
n = int(input("Cantidad de paises a agregar\n"))
paises = []

for i in range(n):
    pais = raw_input("Da el nombre de un pais: ")
    paises.append(pais)

paises = sorted(set(paises))


print(paises)



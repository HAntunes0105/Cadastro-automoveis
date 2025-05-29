Frota = {}

for Linha in open("Frota.csv", "r"):
  Corte = Linha.rstrip().split(";")
  Placa = Corte[0]
  Marca = Corte[1]
  Modelo = Corte[2]
  Tipo = Corte[3]
  Km = Corte[4]
  Data = Corte[5]
  Dict = {"Marca": Marca, "Modelo": Modelo, "Tipo": Tipo, "Km": Km, "Data": Data}
  Frota[Placa] = Dict

print("\n{:^55}\n".format(
    "FROTA DE AUTOMOVEIS DA EMPRESA"))
print("{:10}{:<12}{:<12}{:<10}{:<15}{:<10}".format(
    "PLACA", "MARCA", "MODELO", "TIPO", "KILOMETRAGEM", "DATA")
  )
for Chave, Dados in Frota.items():
  print("{:10}{:<12}{:<12}{:<10}{:<15}{:<10}".format(
      Chave, Dados["Marca"], Dados["Modelo"], Dados["Tipo"], Dados["Km"], Dados["Data"])

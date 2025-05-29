Frota = {}

while True:
  Placa = input("Numero da placa: ")
  MPlaca = Placa.upper()
  if MPlaca == "FIM":
    break
  elif len(MPlaca) != 7:
    print("\nA Placa deve conter 7 caracteres")
  elif MPlaca[0:3].isalpha() == False:
    print("\nOs 3 primeiros caracteres precisam ser letras")
  elif MPlaca[4].isalpha() == False:
    print("\nO quinto caractere precisa ser uma letra")
  elif MPlaca[3].isnumeric() == False:
    print("\nO caracter 3 precisa ser um algarismo")
  elif MPlaca[6:7].isnumeric() == False:
    print("\nO caracter 6 e 7 precisa ser um algarismo")
  elif MPlaca in Frota:
    Escolha = input(f"\nA placa {MPlaca} ja esta registrada na frota de veiculos, deseja fazer alguma alteração?(s/n)  ").lower()
    if Escolha == "n":
      continue
    elif Escolha == "s":
      print(f"\nDADOS DA PLACA {MPlaca}:\n")
      print("{:15}{:<10}{:<10}{:<15}{:<10}".format(
          "MARCA", "MODELO", "TIPO", "KILOMETRAGEM", "DATA")
      )
      print("{:15}{:<10}{:<10}{:<15}{:<10}\n".format(
          Frota[MPlaca]["Marca"], Frota[MPlaca]["Modelo"], Frota[MPlaca]["Tipo"], Frota[MPlaca]["Km"], Frota[MPlaca]["Data"])
      )

      Marca = input("Marca: ")
      if Marca == "":
        Frota.setdefault(MPlaca)
      else:
        Frota[MPlaca]["Marca"] = Marca

      Modelo = input("Modelo: ")
      if Modelo == "":
        Frota.setdefault(MPlaca)
      else:
        Frota[MPlaca]["Modelo"] = Modelo

      Tipo = input("Tipo: ")
      if Tipo == "":
        Frota.setdefault(MPlaca)
      else:
        Frota[MPlaca]["Tipo"] = Tipo

      Km = input("Kilometragem: ")
      if Km == "":
        Frota.setdefault(MPlaca)
      else:
        Frota[MPlaca]["Km"] = Km

        Data = input("Data: ")
      if Data == "":
        Frota.setdefault(MPlaca)
      else:
        Frota[MPlaca]["Data"] = Data
      continue

  else:
    Marca = input("Marca: ")
    Modelo = input("Modelo: ")
    Tipo = input("Tipo: ")
    Km = input("Kilometragem: ")
    Data = input("Data da compra (AAAAMMDD): ")
    Dict = {"Marca": Marca, "Modelo": Modelo, "Tipo": Tipo, "Km": Km, "Data": Data}
    Frota[MPlaca] = Dict
    continue


arq_csv = open("Frota.csv", "w")
for MPlaca, Dados in Frota.items():
  Dado = ("{};{};{};{};{};{}\n".format(
      MPlaca, Dados["Marca"], Dados["Modelo"], Dados["Tipo"], Dados["Km"], Dados["Data"]
  ))
  arq_csv.write(Dado)
arq_csv.close()

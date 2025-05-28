# Registro-de-automoveis

Prrograma registra os seguintes dados de uma frota de veículos de uma empresa:
Placa
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra
O programa fica em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM
para a placa. Se for digitada uma placa com letras minúsculas o programa converte elas para
maiúsculas com o método .upper().

Sendo possivel alterar os dados da placa após digitar a placa correspondente. Para os campos em que nada for digitado é mantido
o valor já cadastrado.
Ao final do laço é gravado todos os dados em um arquivo CSV usando o caractere ";" como delimitador.

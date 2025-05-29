# Registro-de-automoveis

Programa registra os seguintes dados de uma frota de veículos de uma empresa:
- Placa
- Marca
- Modelo
- Tipo (caminhão, furgão, automóvel, motocicleta, etc)
- Kilometragem
- Data da Compra
  
O programa fica em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM
para a placa. Se for digitada uma placa com letras minúsculas o programa converte elas para
maiúsculas com o método .upper().

Se for digitado uma placa que ja tenha sido registrada, é possivel alterar o seu conteudo. Para os campos em que nada for digitado é mantido
o valor já cadastrado.
Ao final do laço é gravado todos os dados em um arquivo frota.csv de forma estruturada, que usa o caractere ";" como delimitador.

---

#Ler-arquivo-csv

Programa de leitura do arquivo "frota.csv" gerado com os dados da frota de veiculos de uma empresa, carregando em um dicionário e exibindo os dados na tela com um layout legível



nt = 'Janeiro na data de 17/01/2022, valor de R$ 11.000,00'

data = input('Data referente: ')
valor = input('Valor referente: ')
mes = int(data[3:5])
mesAnt = mes - 1
dict = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',
    6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
    11: 'Novembro', 12: 'Dezembro'
}

nt = nt.replace(dict[mesAnt],dict[mes]).replace(nt[19:29],data).replace(nt[43:52], valor)

print(nt)
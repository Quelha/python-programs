
nt = 'Dezembro na data de '
nt2 = '17/01/2022, valor de R$ 11.000,00'

data = input('Data referente: ')
valor = input('Valor referente: ')
mes = int(data[3:5])

'''RECOMEÇAR O ANO'''
if mes == 1:
    mesAnt = 12
else:
    mesAnt = mes - 1

dict = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',
    6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
    11: 'Novembro', 12: 'Dezembro'
}

'''MOSTRAR NT ANTERIOR'''
print(nt+nt2)

'''SUBSTITUINDO E JUNTANDO OS DOIS TEXTOS'''
nt = nt.replace(dict[mesAnt],dict[mes]) + nt2.replace(nt2[0:10],data).replace(nt2[25:34], valor)

print(nt)

x = input('FIM')
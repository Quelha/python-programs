
nt = """ASSUNTO:
Trata esta nota da avaliação específica da prestação de serviços de TELEMAR NORTE LESTE S/A, disponibilizados através do Contrato 08/2018, para o mês de Janeiro/2022.\n\n"""
nt2 = """FATOS:
Em 17/01/2022 foi disponibilizada a fatura de telefonia fixa código 350 4329 no valor de R$ 11.051,48 (28190344) e no dia 20/01/2022 foi disponibilizada a fatura da telefonia 0800 código 350 5110, no valor de R$ 1.123,51 (28190786), competência Janeiro 2022.
Foi inserido relatório BI com detalhes das ligações realizadas em Janeiro/2022, no processo de fiscalização mensal SEI-040161/003086/2021
 

CONCLUSÃO:
A empresa atendeu satisfatoriamente aos parâmetros técnicos relativos à prestação de serviço de telefonia fixa, demonstrando ter capacidade técnica para prestar os serviços de telefonia comum e 0800 ao Rioprevidência."""

dataComum = input('Data fatura COMUM: ')
data0800 = input('Data fatura 0800: ')
valorComum = input('Valor fatura COMUM: ')
valor0800 = input('Valor fatura 0800: ')

'''COLETANDO MES'''
mes = int(dataComum[3:5])
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
print(' ')

'''SUBSTITUINDO E JUNTANDO OS DOIS TEXTOS'''
nt = nt.replace(dict[mesAnt],dict[mes]) + nt2.replace(nt2[10:20],dataComum).replace(nt2[129:138],data0800).replace(nt2[99:109], valorComum).replace(nt2[219:227], valor0800).replace(dict[mesAnt],dict[mes])

print(nt)

x = input('FIM')
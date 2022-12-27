#-*- coding: utf-8 -*-
import csv

with open ('teste.csv',mode='r')as arq:
    leitor = csv.reader(arq,delimiter=',')
    linhas = 0
    for coluna in leitor:
        if linhas ==0:
            print('colunas',coluna)#print(f'Colunas:{" ".join(coluna)}.')
            linhas +=1
        else:
            print('numero: ',coluna[0],' nome: ',coluna[1])#print(f'\tNumero{coluna[0]} e o nome é {coluna[1]}.')    
            linhas +=1
    print('Lidas ',linhas)#print(f'lidas{linhas} lidas.')        
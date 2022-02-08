# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import statistics as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#inserção de dados de auditoria
dados_audit = pd.read_excel('Dados_audit.xlsx')


# análise de variação de tensão de alimentação, item 2.3
# a verificacao do enquadramento de 95% foi realizada por meio de distribuição gaussiana (95% dos dados estao em 2 desvios padrões)
media_AveUrms1 = dados_audit['AveUrms1'].mean()
media_AveUrms2 = dados_audit['AveUrms2'].mean()
media_AveUrms3 = dados_audit['AveUrms2'].mean()
desvio_AveUrms1 = st.stdev(dados_audit['AveUrms1'])
desvio_AveUrms2 = st.stdev(dados_audit['AveUrms2'])
desvio_AveUrms3 = st.stdev(dados_audit['AveUrms2'])
limite_superior_AveUrms1 = media_AveUrms1 + 2*desvio_AveUrms1
limite_superior_AveUrms2 = media_AveUrms2 + 2*desvio_AveUrms2
limite_superior_AveUrms3 = media_AveUrms2 + 2*desvio_AveUrms3
limite_inferior_AveUrms1 = media_AveUrms1 - 2*desvio_AveUrms1
limite_inferior_AveUrms2 = media_AveUrms2 - 2*desvio_AveUrms2
limite_inferior_AveUrms3 = media_AveUrms2 - 2*desvio_AveUrms3

#item 2.3 sobretensão e subtensão
if (limite_superior_AveUrms1 > (230*1.1)):
   print('Valor eficaz médio na fase 1 acima do limite permitido de 10% em 95% dos dados')
if (limite_superior_AveUrms2 > (230*1.1)):
   print('Valor eficaz médio na fase 2 acima do limite permitido de 10% em 95% dos dados')
if (limite_superior_AveUrms3 > (230*1.1)):
   print('Valor eficaz médio na fase 3 acima do limite permitido de 10% em 95% dos dados')
if (limite_inferior_AveUrms1 < (230*0.9)):
   print('Valor eficaz médio na fase 1 abaixo do limite permitido de 10% em 95% dos dados')
if (limite_inferior_AveUrms2 < (230*0.9)):
   print('Valor eficaz médio na fase 2 abaixo do limite permitido de 10% em 95% dos dados')
if (limite_inferior_AveUrms3 < (230*0.9)):
   print('Valor eficaz médio na fase 3 abaixo do limite permitido de 10% em 95% dos dados')
if any ( dados_audit['AveUrms1'] < (230*0.85)) or any (dados_audit['AveUrms1'] > (230*1.1)):
   print('Valor eficaz médio na fase 1 fora do limite de +10%/-15% em algum dos dados')
if any ((230*0.85) > dados_audit['AveUrms2']) or any (dados_audit['AveUrms2']  > (230*1.1)):
   print('Valor eficaz médio na fase 2 fora do limite de +10%/-15% em algum dos dados')
if any ((230*0.85) > dados_audit['AveUrms3']) or any (dados_audit['AveUrms3'] > (230*1.1)):
   print('Valor eficaz médio na fase 3 fora do limite de +10%/-15% em algum dos dados')     
else:
   print('Valor eficaz médio das 3 fases não ultrapassam os limites permitidos de +- 10% em nenhum momento')

#item 2.10 desequilíbrio   
media_MaxUunb = dados_audit['MaxUunb'].mean()     
desvio_MaxUunb = st.stdev(dados_audit['MaxUunb'])  
limite_MaxUunb  = media_MaxUunb  + 2*desvio_MaxUunb
if (limite_MaxUunb  > 1.02 ):
   print('Desequilíbrio das tensões acima do limite tolerável' )
else:
   print('Desequilíbrio das tensões dentro do limite tolerável')
   

zscore2_harmonicos = np.zeros((3,24))   
for i, j in enumerate(range(90, 162, 3)): #insercao da media de harmonicos da fase1 
    zscore2_harmonicos[0][i] = dados_audit.iloc[0:,j].mean() 
for i, j in enumerate(range(240, 312, 3)): #insercao da media de harmonicos da fase2
    zscore2_harmonicos[1][i] = dados_audit.iloc[0:,j].mean() + 2 * st.stdev(dados_audit.iloc[0:,j])
for i, j in enumerate(range(390, 462, 3)): #insercao da media de harmonicos da fase3
    zscore2_harmonicos[2][i] = dados_audit.iloc[0:,j].mean() + 2 * st.stdev(dados_audit.iloc[0:,j])   

#criacao de tabela excel zscore2_harmonicos 
linha = 'Fase1 Fase2 Fase3'.split()
coluna ='2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split()
tabela = pd.DataFrame(data = zscore2_harmonicos, index = linha, columns = coluna)
tabela.to_excel('Peso realativo de harmonicos de tensao.xls')


for i in range (3):
   if (zscore2_harmonicos[i][0] > 2):
       print('Tensão relativa no harmonico 2 da fase ',[i],'maior que 2%'  )
for i in range (3):
   if (zscore2_harmonicos[i][1] > 5):
       print('Tensão relativa no harmonico 3 da fase ',[i],'maior que 5%'  )
for i in range (3):
   if (zscore2_harmonicos[i][2] > 1):
       print('Tensão relativa no harmonico 4 da fase ',[i],'maior que 1%'  )
for i in range (3):
   if (zscore2_harmonicos[i][3] > 6):
       print('Tensão relativa no harmonico 5 da fase ',[i],'maior que 6%'  )
for i in range (3):
   for j in range (4,22,2): 
       if (zscore2_harmonicos[i][j] > 0.5):
          print('Tensão relativa no harmonico par de 6...24 da fase ',[i],'maior que 0,5%'  )       
for i in range (3):
   if (zscore2_harmonicos[i][5] > 5):
       print('Tensão relativa no harmonico 7 da fase ',[i],'maior que 5%')
for i in range (3):
   if (zscore2_harmonicos[i][7] > 1.5):
       print('Tensão relativa no harmonico 9 da fase ',[i],'maior que 1.5%')
for i in range (3):
   if (zscore2_harmonicos[i][9] > 3.5):
       print('Tensão relativa no harmonico 11 da fase ',[i],'maior que 3.5%')
for i in range (3):
   if (zscore2_harmonicos[i][11] > 3):
       print('Tensão relativa no harmonico 13 da fase ',[i],'maior que 3%')
for i in range (3):
   if (zscore2_harmonicos[i][13] > 0.5):
       print('Tensão relativa no harmonico 15 da fase ',[i],'maior que 0.5%')
for i in range (3):
   if (zscore2_harmonicos[i][15] > 2):
       print('Tensão relativa no harmonico 17 da fase ',[i],'maior que 2%') 
for i in range (3):
   if (zscore2_harmonicos[i][17] > 1.5):
       print('Tensão relativa no harmonico 19 da fase ',[i],'maior que 1.5%')
for i in range (3):
   if (zscore2_harmonicos[i][19] > 0.5):
       print('Tensão relativa no harmonico 21 da fase ',[i],'maior que 0.5%') 
for i in range (3):
   if (zscore2_harmonicos[i][21] > 1.5):
       print('Tensão relativa no harmonico 23 da fase ',[i],'maior que 1.5%')
for i in range (3):
   if (zscore2_harmonicos[i][23] > 1.5):
       print('Tensão relativa no harmonico 25 da fase ',[i],'maior que 1.5%')
else:
   print('As tensões em cada harmónica de ordem 2 a 25 nas 3 fases não excede o limite estabelecido')       
       
#análise de frequência, item 2.1 (ligação síncroona a redes interligadas)
if any (dados_audit['MaxFreq'] > 52):
   print ('Frequência máxima extrapola o limite de 52 Hz')
   print ('A maior frequência é', dados_audit['MaxFreq'].max())
if any (dados_audit['MinFreq'] < 47) :
   print ('Frequência miníma extrapola o limite de 47 Hz')
   print ('A menor frequência é', dados_audit['MinFreq'].min())
else:
   print ('Frequência dentro do limite de 47 Hz a 52 Hz')
   

#análise de THD de tensão
if any (dados_audit['MaxUthd1'] > 8) :
   print ('Em algum momento a THD na fase 1 ultrapassa 8%')
if any (dados_audit['MaxUthd2'] > 8) :
   print ('Em algum momento a THD na fase 2 ultrapassa 8%')
if any (dados_audit['MaxUthd3'] > 8) :   
   print ('Em algum momento a THD na fase 1 ultrapassa 8%') 
else:   
   print ('THD não ultrapassa 8% em nenhuma das fases')
   
#análise de THD de corrente

x = list(range(1008))

fig1, ax = plt.subplots()
ax.plot(x, dados_audit['MaxIthd1'])
ax.set_ylabel('THD máxima de corrente [%]')
fig1.savefig('THD maxima de corrente fase1.png')

fig2, bx = plt.subplots()
bx.plot(x, dados_audit['MaxIthd2'])
bx.set_ylabel('THD máxima de corrente [%]')
fig2.savefig('THD maxima de corrente fase2.png')

fig3, cx = plt.subplots()
cx.plot(x, dados_audit['MaxIthd3'])
cx.set_ylabel('THD máxima de corrente [%]')
fig3.savefig('THD maxima de corrente fase3.png')

fig4, dx = plt.subplots()
dx.plot(x, dados_audit['MaxIunb'])
dx.set_ylabel('Taxa de desequilíbrio das correntes')
fig4.savefig('Taxa de desequilíbrio das correntes.png')

from scipy import stats

print(stats.pearsonr(dados_audit['MaxIthd1'], dados_audit['MaxIunb'])) #coefieciente de pearson para fase 1
print(stats.pearsonr(dados_audit['MaxIthd2'], dados_audit['MaxIunb'])) #coefieciente de pearson para fase 2
print(stats.pearsonr(dados_audit['MaxIthd3'], dados_audit['MaxIunb'])) #coefieciente de pearson para fase 3

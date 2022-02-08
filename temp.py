# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import statistics as st
import pandas as pd


#inserção de dados de auditoria
dados_audit = pd.read_excel('Dados_audit.xlsx')

# análise de variação de tensão de alimentação, item 2.3 ()
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

if (limite_superior_AveUrms1 > (230*1.1)):
   print('Valor eficaz médio na fase 1 acima do limite permitido de 10% em 95% dos dados')
if (limite_superior_AveUrms2 > (230*1.1)):
   print('Valor eficaz médio na fase 2 acima do limite permitido de 10% em 95% dos dados')
if (limite_superior_AveUrms3 > (230*1.1)):
   print('Valor eficaz médio na fase 3 acima do limite permitido de 10% em 95% dos dados')
if (limite_inferior_AveUrms1 < (230*0.9)):
   print('Valor eficaz médio na fase 1 abaixo do limite permitido de 10% em 95% dos dados')
if (limite_inferior_AveUrms2 < (230*0.99)):
   print('Valor eficaz médio na fase 2 abaixo do limite permitido de 10% em 95% dos dados')
if (limite_inferior_AveUrms3 < (230*0.9)):
   print('Valor eficaz médio na fase 3 abaixo do limite permitido de 10% em 95% dos dados')   

#análise de frequência, item 2.1 (ligação síncroona a redes interligadas)
if any (dados_audit['MaxFreq'] > 52) :
   print ('Frequência máxima extrapola o limite de 52 Hz')
   print ('A maior frequência é', dados_audit['MaxFreq'].max())
if any (dados_audit['MinFreq'] < 47) :
   print ('Frequência miníma extrapola o limite de 47 Hz')
   print ('A menor frequência é', dados_audit['MinFreq'].min())
else:
   print ('Frequência dentro do limite de 47 Hz a 52 Hz')
   

#análise de THD
if any (dados_audit['MaxUthd1'] > 8) :
   print ('Em algum momento a THD na fase 1 ultrapassa 8%')
if any (dados_audit['MaxUthd2'] > 8) :
   print ('Em algum momento a THD na fase 2 ultrapassa 8%')
if any (dados_audit['MaxUthd3'] > 8) :   
   print ('Em algum momento a THD na fase 1 ultrapassa 8%') 
else:   
   print ('THD não ultrapassa 8% em nenhuma das fases')



# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:03:21 2021

@author: Tiago
"""

    
#item 2.4 Flicker
variacao_maxima_fase1 = dados_audit['Umax1'] / dados_audit['AveUrms1']
variacao_maxima_fase2 = dados_audit['Umax2'] / dados_audit['AveUrms2'] 
variacao_maxima_fase3 = dados_audit['Umax3'] / dados_audit['AveUrms3'] 

numero_de_linhas = len(variacao_maxima_fase1)
amostras_PST = 84
N_PLT = int(numero_de_linhas / amostras_PST)
PST1_max = list(range(12))

#percentil das variacoes maximas em pu da fase 1
for i in range(0, N_PLT+1):
    for j in variacao_maxima_fase1.index[(0+amostras_PST*i):(amostras_PST*(i+1)+1)]:
    
         variacao_maxima_fase1_p01 = np.percentile(variacao_maxima_fase1, 0.1)
         variacao_maxima_fase1_p07 = np.percentile(variacao_maxima_fase1, 0.7)
         variacao_maxima_fase1_p1 = np.percentile(variacao_maxima_fase1, 1)
         variacao_maxima_fase1_p13 = np.percentile(variacao_maxima_fase1, 1.3)
         variacao_maxima_fase1_p22 = np.percentile(variacao_maxima_fase1, 2.2)
         variacao_maxima_fase1_p3 = np.percentile(variacao_maxima_fase1, 3)
         variacao_maxima_fase1_p4 = np.percentile(variacao_maxima_fase1, 4)
         variacao_maxima_fase1_p6 = np.percentile(variacao_maxima_fase1, 6)
         variacao_maxima_fase1_p8 = np.percentile(variacao_maxima_fase1, 8)
         variacao_maxima_fase1_p10 = np.percentile(variacao_maxima_fase1, 10)
         variacao_maxima_fase1_p13 = np.percentile(variacao_maxima_fase1, 13)
         variacao_maxima_fase1_p17 = np.percentile(variacao_maxima_fase1, 17)
         variacao_maxima_fase1_p30 = np.percentile(variacao_maxima_fase1, 30)
         variacao_maxima_fase1_p50 = np.percentile(variacao_maxima_fase1, 50)
         variacao_maxima_fase1_p80 = np.percentile(variacao_maxima_fase1, 80)
         #percentis especifícos em pu das variacoes maximas da fase 1
         variacao_maxima_fase1_p1S = ((variacao_maxima_fase1_p07 + variacao_maxima_fase1_p1 + variacao_maxima_fase1_p13)/3)
         variacao_maxima_fase1_p3S = ((variacao_maxima_fase1_p22 + variacao_maxima_fase1_p3 + variacao_maxima_fase1_p4)/3)
         variacao_maxima_fase1_p10S = ((variacao_maxima_fase1_p6 + variacao_maxima_fase1_p8 + variacao_maxima_fase1_p10 + variacao_maxima_fase1_p13 + variacao_maxima_fase1_p17)/5)
         variacao_maxima_fase1_p50S = ((variacao_maxima_fase1_p30 + variacao_maxima_fase1_p50 + variacao_maxima_fase1_p80)/3)
         #cálculo short-term flicker severity (PST) e long-term flicker severity (PLT) das variacoes maximas da fase 1
         PST1_max[i] = np.sqrt(0.0314*variacao_maxima_fase1_p01 + 0.0525*variacao_maxima_fase1_p1S + 0.0657*variacao_maxima_fase1_p3S + 0.28* variacao_maxima_fase1_p10S + 0.08*variacao_maxima_fase1_p50S)

 
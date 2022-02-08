# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#inserção de dados
dataset=pd.read_excel('dados_1ciclo_G4.xlsx')
dataset=np.array(dataset)
tempo = dataset[0:4096,0]
tensao = dataset[0:4096,1]
corrente = dataset[0:4096,2]

#plotagem dos dados de corrente
fig1, ax = plt.subplots()
ax.plot(tempo, corrente)
ax.set_title('Sinal de corrente')
ax.set_xlabel('Tempo [s]')
ax.set_ylabel('Corrente [A]')
fig1.savefig('corrente.png')

#plotagem dos dados de tensão
fig2, bx = plt.subplots()
bx.plot(tempo, tensao)
bx.set_title('Sinal de tensão')
bx.set_xlabel('Tempo [s]')
bx.set_ylabel('Tensão [V]')
fig2.savefig('tensao.png')

#obtensão da análise de Fourier
from scipy.fft import fftfreq

N = len(tempo) #número de amostragens
periodo = tempo[-1] #período do sinal
sample_rate = periodo/N #tempo de amostragem
frequencia = fftfreq(N, sample_rate) #extração das frequências harmónicas

#análise de fourier para tensão
fft_calculo1 = np.fft.fft(tensao)
fft_abs1 = 2 * np.abs(fft_calculo1/N) #extração das amplitudes
plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
plt.xlim([0,550])
plt.ylim([0,350])
plt.title('Espectro de frequência do sinal de tensão')
plt.ylabel('Amplitude')
plt.xlabel('Frequência')
plt.bar(frequencia, fft_abs1, width=2)
plt.savefig('Especto de frequência do sinal de tensao.png')
plt.show()

#análise de fourier para corrente
fft_calculo2 = np.fft.fft(corrente)
fft_abs2 = 2 * np.abs(fft_calculo2/N)#extração das amplitudes
plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
plt.yticks([0, 2.5 , 5, 10, 15, 20, 25, 30, 35])
plt.xlim([0,550])
plt.ylim([0,40])
plt.title('Espectro de frequência do sinal de corrente')
plt.ylabel('Amplitude')
plt.xlabel('Frequência')
plt.bar(frequencia, fft_abs2, width=2)
plt.savefig('Especto de frequência do sinal de corrente.png')
plt.show()

#cálculo de DHT para tensão

fft_rms1=(fft_abs1/np.sqrt(2)) #tensão rms de cada frequência
tensao_rms = [11] #para tabela posterior
tensao_rms[0] = np.sqrt(sum(fft_rms1[:4095]**2)) #tensão rms do sinal como um todo
tensao_rms_frequencia_fundamental = [11] #para tabela posterior
tensao_rms_frequencia_fundamental[0] = fft_rms1[1]
tensao_rms_harmonicas = [11] #para tabela posterior
tensao_rms_harmonicas[0] = np.sqrt(sum(fft_rms1[2:4095]**2)) #tensão rms do somatório de harmónicas
DHT_tensao_porcentagem = [11] #para tabela posterior
DHT_tensao_porcentagem[0] = (tensao_rms_harmonicas / fft_rms1[1]) * 100 #DHT de harmónicas de tensão

#cálculo de DHT para corrente

fft_rms2=(fft_abs2/np.sqrt(2)) #corrente rms de cada frequêcnia
corrente_rms = [11] #para tabela posterior
corrente_rms[0] = np.sqrt(sum(fft_rms2[:4095]**2)) #corrente rms do sinal como um todo
corrente_rms_frequencia_fundamental = [11] #para tabela posterior
corrente_rms_frequencia_fundamental[0] = fft_rms2[1]
corrente_rms_harmonicas = [11] #para tabela posterior
corrente_rms_harmonicas[0] = np.sqrt(sum(fft_rms2[2:4095]**2)) #corrente rms do somatório de harmónicas
DHT_corrente_porcentagem = [11] #para tabela posterior
DHT_corrente_porcentagem[0] = (corrente_rms_harmonicas / fft_rms2[1]) * 100 #DHT de harmónicas de corrente

#criacao de tabela excel contendo dados das duas análises acima 
linha = 'Frequência Amplitude_de_tensão Tensão_rms_do_sinal[V] Tensão_rms_frequência_fundamental[V] Tensão_rms_harmónicos[V] DHT(%)_tensão Amplitude_de_corrente Corrente_rms_do_sinal[A] Corrente_rms_frequência_fundamental[A] Corrente_rms_harmónicos[A] DHT(%)_corrente'.split()
dados = [frequencia[:11], fft_abs1[:11], tensao_rms, tensao_rms_frequencia_fundamental, tensao_rms_harmonicas, DHT_tensao_porcentagem, fft_abs2[:11], corrente_rms, corrente_rms_frequencia_fundamental, corrente_rms_harmonicas, DHT_corrente_porcentagem]
tabela = pd.DataFrame(data = dados, index = linha)
tabela.to_excel('Dados espectro de frequência de tensao e corrente.xls')

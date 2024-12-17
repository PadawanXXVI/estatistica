'''
EXEMPLO 01 - TAXA DE HOMICÍDIOS
CRIAÇÃO DE BOX PLOT COM MATPLOTLIB
'''

import numpy as np
import matplotlib.pyplot as plt

populacao = {
    'Estado': ['Alabama', 'Alasca', 'Arizona', 'Arkansas', 'Califórina', 'Colorado', 'Connecticut', 'Delaware'],
    'População': [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934],
    'Taxa de homicídio': [5.7, 5.6, 4.7, 5.6, 4.4, 2.8, 2.4, 5.8]
}

# Média aritimética
media = np.mean(populacao['Taxa de homicídio']) 
print(f' A média é {media}')

# Desvio padrão
desvio_padrao = np.std(populacao['Taxa de homicídio'])
print(f'O desvio padrão é {desvio_padrao}')

# Quartis
## Mediana
q2 = np.median(populacao['Taxa de homicídio']) # segundo quartil = mediana
print(f'A mediana (ou segundo quartil) é {q2}')
## primeiro e terceiro quartis
q1 = np.percentile(populacao['Taxa de homicídio'],25) # primeiro quartil
q3 = np.percentile(populacao['Taxa de homicídio'],75) # terceiro quartil
print(f'O primeiro quartil é {q1}')
print(f'O terceiro quartil é {q3}')

# Amplitude
IQR = q3 -q1 # amplitude interquartil
print(f'A amplitude é {IQR}')

# Em python, ao usarmos as biblioteca numpy e matplotlib, as próprias bibliotecas ordenam os dados em ordem crescente

# Criação do boxplot
dados = populacao['Taxa de homicídio']
plt.boxplot(dados) # cria o boxplot

# Adição do título e do rótulo
plt.title('Taxa de homicídios')
plt.ylabel('Valores')

plt.show()
# -*- coding: utf-8 -*-
# Importar bibliotecas
import numpy as np
import pandas as pd
import random

#Carregar e remover todos os atributos não utilizados nas questões abaixo.
data = pd.read_csv("credit_v1.csv", usecols = ['Month', 'Age', 'SSN', 'Occupation', 'Annual_Income'])

print(data.to_string())

#Embaralhar a coluna Month
data['Month'] = random.sample(data['Month'].tolist(), len(data['Month']))

data

#Usar uma máscara no SSN para transformar 821-00-0265 em 821-**-****
data['SSN'] = data['SSN'].str.extract(r'^(\d{3})-(.*)$')[0] + '-' + '*'*2 + '-' + '*'*4

data

#Generalize o atributo Ocuppation {Scientist, Teacher, Engineer,Developer} -> Academic, {Lawyer, Doctor} -> Service, {Media_manager, Journalist} -> Media

mapping = {
    'Scientist': 'Academic',
    'Teacher': 'Academic',
    'Engineer': 'Academic',
    'Developer': 'Academic',
    'Lawyer': 'Service',
    'Doctor': 'Service',
    'Media_manager': 'Media',
    'Journalist': 'Media'
}
data['Occupation'] = data['Occupation'].replace(mapping)

data

#Iloss do valor academic

iloss_academic = (4-1)/9
print("O iloss de Academic é:",iloss_academic)

#Generalizar o atributo idade para os intervalos [20-29], [30-39]

#Definir os limites dos intervalos
bins = [0, 19, 29, 39, 49, 59, 69, 120]

#Definir os rótulos dos intervalos
labels = ['0-18', '19-29', '30-39', '40-49', '50-59', '60-69', '70+']

#Aplicar a generalização da coluna idade usando a função cut()
data['Age'] = pd.cut(data['Age'], bins=bins, labels=labels)

data

#Iloss do valor [20-29]

iloss_age = (4-1)/17
print("O iloss de [20-29] é:",iloss_age)

#Adicionar um ruído independente entre -1000 e 1000 no atributo Annual_Income em cada registro

noise = np.random.uniform(low=-1000, high=1000, size=len(data))
data['Annual_Income_Noise'] = data['Annual_Income'] + noise

# Armazenando a nova coluna em uma variável separada
income_with_noise = data['Annual_Income_Noise'].tolist()

data

#Reporte a diferença entre a média de Annual_Income anonimizado para original

#Média dataset original
media = data['Annual_Income'].mean()

#Média dataset anonimizado
media_noise = data['Annual_Income_Noise'].mean()

#Diferença entre os dois
dif = media_noise - media

print("Diferença entre os dois:",dif)
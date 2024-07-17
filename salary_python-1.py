# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:39:13 2023

@author: Dell
"""

import pandas as pd

df = pd.read_csv('salary_data.csv')

df['continent_name'] = df['continent_name'].replace('Caribbean','North America')
df['continent_name'] = df['continent_name'].replace('Northern America','North America')
df['continent_name'] = df['continent_name'].replace('Central America','North America')

df['continent_name'] = df['continent_name'].replace('Oceania','Australia/Oceania')


df.to_csv('modified_data.csv',index=False)
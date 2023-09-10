#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:05:44 2023

@author: carlmagnusson
"""

import os
import json
import pandas as pd
import matplotlib.pyplot as plt

# Opening JSON file
folder_path = 'info_playmaker-playmakeropendata-21eca6c6a3b8/allsvenskan, 2021/matcher'

data_list = []

#läser in alla JSON-filer. 
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
            data_list.append(json_data)
 
# Skapar df innehållandes all information kring matcherna i Allsvenskan 2021.
# Alla kolumner (som vi får ut från filinlösningen) är strängar
# Så lite strängmanipulation kommer krävas för att få ut de värden jag vill ha
all_data = pd.DataFrame(data_list)

# skapar en df som innehåller de kolumner som ja gär intresserad av att analysera. 
teams_efficiency = all_data[["visitingTeam","homeTeam", "xG", "score"]]

# "frigör" minne, tar egentligen bara bort referensen. 
del all_data, data_list, file_path, filename, folder_path, json_data, json_file

# Initialiserar listor som ska användas vid analys. 
# Finns ett par listor här nedan som vi egentligen inte behöver. 
home_team = []
home_eff = []
visiting_team = []
visiting_eff = []

for i in range(len(teams_efficiency.index)):
    # Plockar ut lagen i listor
    home_team.append(teams_efficiency["homeTeam"].iloc[i])
    visiting_team.append(teams_efficiency["visitingTeam"].iloc[i])
    
    # tar bort '[' och ']'
    teams_efficiency["xG"].iloc[i] = teams_efficiency["xG"].iloc[i].replace('[', '')
    teams_efficiency["xG"].iloc[i] = teams_efficiency["xG"].iloc[i].replace(']', '')
    teams_efficiency["score"].iloc[i] = teams_efficiency["score"].iloc[i].replace('[', '')
    teams_efficiency["score"].iloc[i] = teams_efficiency["score"].iloc[i].replace(']', '')
    
    
    # Plockar ut lagens effektivitet i listor
    # Vill inte försöka dela med 0, så kör try-except. 
    try: 
        home_eff.append(int(teams_efficiency["score"].iloc[i].split(',')[0]) / float(teams_efficiency["xG"].iloc[i].split(',')[0]))
    except: 
            home_eff.append(0)
    try: 
        visiting_eff.append(int(teams_efficiency["score"].iloc[i].split(',')[1]) / float(teams_efficiency["xG"].iloc[i].split(',')[1]))
    except: 
            visiting_eff.append(0)
            
# skapar nya dataframes och lägger till mina serier
home_team = pd.DataFrame(list(zip(home_team, home_eff)), columns = ['Team', 'efficiency'])
home_team['isHome'] =  'Hemma'
visiting_team = pd.DataFrame(list(zip(visiting_team, visiting_eff)), columns = ['Team', 'efficiency'])
visiting_team['isHome'] = 'Borta'

# "Frigör minne"
del i, teams_efficiency, home_eff, visiting_eff


# Skapar 1 dataframe av visiting_team och home_team, som är grupperad på lag, hemma/borta samt beräknar dess effektivitet.  
grouped_by = pd.concat([home_team, visiting_team]).groupby(['Team', 'isHome']).mean()

# skapar en ny DF som resettar indexeringen och droppar onödiga kolumner. 
df = grouped_by.reset_index()


# Pivot på vår DF, detta ger oss 2 kolumner per lag istället för 2 rader. 
pivot_df = df.pivot(index='Team', columns='isHome', values='efficiency').sort_values(['Borta', 'Hemma'])

# "Frigör minne"
del grouped_by, df, home_team, visiting_team



# Skapar vår graf
pivot_df.plot(
        y = ['Borta', 'Hemma'], 
        kind = 'bar', 
        color = ['#3E8EDE', '#324AB2']
    )
plt.legend(title = "Effektivitet")
plt.title(label="Allsvenskan 2021")
plt.xlabel('Lag')
plt.ylabel('Mål / xG')





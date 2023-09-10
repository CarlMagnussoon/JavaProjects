#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:50:12 2023

@author: carlmagnusson
"""

import os
import json
import pandas as pd
import numpy as np

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
teams_xG = all_data[["visitingTeam","homeTeam", "xG"]]

del all_data, data_list, file_path, filename, folder_path, json_data, json_file

home_team = []
visiting_team = []
home_points = []
visiting_points = []

for i in range(len(teams_xG.index)): 
    # Plockar ut lagen i listor
    home_team.append(teams_xG["homeTeam"].iloc[i])
    visiting_team.append(teams_xG["visitingTeam"].iloc[i])
    
   # tar bort '[' och ']'
    teams_xG["xG"].iloc[i] = teams_xG["xG"].iloc[i].replace('[', '')
    teams_xG["xG"].iloc[i] = teams_xG["xG"].iloc[i].replace(']', '')
    
    home_xG = np.round(float(teams_xG["xG"].iloc[i].split(',')[0]), decimals = 0)
    visiting_xG = np.round(float(teams_xG["xG"].iloc[i].split(',')[1]), decimals = 0)
    
    if home_xG == visiting_xG: 
        home_points.append(1)
        visiting_points.append(1)
        
    elif home_xG < visiting_xG: 
        visiting_points.append(3)
        home_points.append(0)
    else: 
        visiting_points.append(0)
        home_points.append(3)
        
#del teams_xG
        
visiting_team = pd.DataFrame(list(zip(visiting_team, visiting_points)), columns = ['Team', 'points'])
home_team = pd.DataFrame(list(zip(home_team, home_points)), columns = ['Team', 'points'])
    

teams = pd.concat([visiting_team, home_team]).groupby('Team').sum().sort_values(by='points', ascending= 0)
del home_points, home_xG, i, visiting_xG, visiting_points, visiting_team, home_team, teams_xG


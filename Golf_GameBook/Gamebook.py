#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:39:46 2023

@author: carlmagnusson
"""

from player import player
from golf_hole import golf_hole    

# Funktion som tar emot en txt-sträng och öppnar filen -> skapar upp en lista och returnerar. 
def import_holes(filename: str) -> list: 
    golf_holes = []
    
    with open(filename) as holes: 
        line = 0 # Används bara för att skippa första raden. 
        for hole in holes: 
            if line == 0:
                line += 1
                pass 
            else: 
               row = hole.split(' ') # Splittar strängen
               golf_holes.append(golf_hole(int(row[0]), int(row[1]), int(row[2]))) # Fyller vår lista med golfhål. 
                
    return golf_holes

# Funktion som distribuerar spelarens extra slag, baserat på index. 
def distribute_extra_strokes(player, golf_hole_list): 
    
    player_strokes = player.get_strokes()
    
    sorted_holes = sorted(golf_hole_list, key=lambda hole: hole.get_index())
    
    while player_strokes != 0: 
        
       for hole in sorted_holes: 
           
           hole.set_extra_strokes(hole.get_extra_strokes() + 1)
                
           player_strokes -= 1
            
           if player_strokes == 0: 
               break

def calculate_stableford_points(score, par, extra_strokes):   
    return max(0, 2 + (par + extra_strokes) - score)

def count_stableford_points(golf_hole_list: list) -> int: 
    stableford_points = 0
    
    for hole in golf_hole_list:
        if hole.get_score() is not None: 
            stableford_points += calculate_stableford_points(hole.get_score(), hole.get_par(), hole.get_extra_strokes())
    return stableford_points

# Totala brutto
def gross_result(golf_hole_list: list) -> int: 
    
    total_number_of_strokes = 0
    
    for holes in golf_hole_list: 
        if hole.get_score() is not None: 
            total_number_of_strokes += hole.get_score()
    return total_number_of_strokes

# Netto
def net_results(golf_hole_list: list, player: player) -> str: 
    gross_results = gross_result(golf_hole_list)
    strokes = player.get_strokes()
    course_par = 0
    
    #Summerar banans par 
    for hole in golf_hole_list: 
        course_par += hole.get_par()
        
    if course_par == gross_results - strokes: 
        return 'E'
    elif course_par < gross_results - strokes: 
        return '+' + ((gross_results - strokes) - course_par)
    else: 
        return str(course_par - (gross_results - strokes))


# Spelare     
player_name = 'Carl Magnusson'
player_hcp = 12.5
player_strokes = 14
player = player(player_name, player_hcp, player_strokes)



# Importerar golfhålen. 
golf_holes = []
golf_holes = import_holes('Ljunghusen 1-18.txt')

# Distribuerar golfslagen
distribute_extra_strokes(player, golf_holes)

# Printar lite stuff
print('-----Spelare-----')
print(player)
print('')
print('-----Hål-----')
for hole in golf_holes:
    print(f'Hål {hole.get_number()} Par {hole.get_par()} Index {hole.get_index()}')
    hole.set_score(int(input('Hur många slag fick du?: ')))
    points = count_stableford_points(golf_holes)
    print(f'Poängsumma: {points}')
    


print(total_number_of_strokes(golf_holes))
    



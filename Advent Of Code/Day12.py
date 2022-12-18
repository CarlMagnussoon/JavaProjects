#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:27:14 2022

@author: carlmagnusson
"""
# --- Day 12: Hill Climbing Algorithm ---
# You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

# You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

# Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

# For example:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^
# In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

# This path reaches the goal in 31 steps, the fewest possible.

# What is the fewest steps required to move from your current position to the location that should get the best signal?


#Använder mig av BFS för att hitta kortaste distansen. 
import numpy as np 

#Funktion som konverterar min input till siffror istället.
#Enklare att jämföra
def convert(char): 
    #Initierar en Sträng som hjälper mig att byta bokstäver mot siffror. 
    convert = 'SabcdefghijklmnopqrstuvwxyzE'
    result = 0
    
    for r in range(0, len(convert)): 
        if convert[r] == char: 
            result = r
            break
        else:
            continue
        
    return result

#Klass som innehåller en cells rad, kolumn värde och hur långt ifrån det är från startcellen. 
class node: 
    def __init__(self, row, col, distancetoEnd): 
        self.row = row
        self.col = col
        self.distancetoEnd = distancetoEnd
        
    def __repr__(self): 
        return f"node({self.row}, {self.col}, {self.distancetoEnd})"

def distanceToStart(arr2D): 
    #Initierar startcellen
    start = node(0, 0, 0)
    
    
    NoRows = len(arr2D) 
    NoCols = len(arr2D[0]) 
    
    #Skapar upp en 0-array för att hålla koll på var vi redan varit (vill inte kontrollera det igen).
    visited = np.zeros((NoRows, NoCols))
    
    #Plats vi ska starta på
    for r in range(len(arr2D)):
        for c in range(len(arr2D[r])): 
            
            if arr2D[r][c] == 0: 
                start.row = r
                start.col = c
                break
    
    #Lista som ska användas för att lägga in nästa möjliga cell. 
    queue = []
    queue.append(start)
    visited[start.row][start.col] = 1
    
    #Loopar igenom tills vi stöter på slutcellen 
    while len(queue) != 0: 
        source = queue.pop(0)
        
        #Kommit till slutposition
        if (arr2D[source.row][source.col] == 27):
            return source.distancetoEnd
        
        #Rör oss upp 
        if validMove(source.row - 1, source.col, arr2D, visited, 'U'): 
            queue.append(node(source.row-1, source.col, source.distancetoEnd + 1))
            visited[source.row - 1][source.col] = 1
            
        #Rör oss ner
        if validMove(source.row + 1, source.col, arr2D, visited, 'D'): 
            queue.append(node(source.row + 1, source.col, source.distancetoEnd + 1))
            visited[source.row + 1][source.col] = 1
            
        #Rör oss höger 
        if validMove(source.row, source.col + 1, arr2D, visited, 'R'): 
            queue.append(node(source.row, source.col + 1, source.distancetoEnd + 1))
            visited[source.row][source.col  + 1] = 1
            
         #Rör oss vänster 
        if validMove(source.row, source.col - 1, arr2D, visited, 'L'): 
            queue.append(node(source.row, source.col - 1, source.distancetoEnd + 1))
            visited[source.row][source.col - 1] = 1
            
    return -1

def validMove(r, c, arr2D, visited, direction): 
    result = False
    
    #Först kollar vi så att vi inte försöker ta ett gammal position och att vi håller oss inom ramen för matrisenn
    if ((r >= 0 and c >= 0) and
        (r < len(arr2D) and c < len(arr2D[0])) and
         (visited[r][c] == 0)):
        
        #Om vi rör oss i en riktning så måste vi kolla att det går enligt reglerna. 
        if direction == 'D' and  arr2D[r][c] - arr2D[r-1][c] <= 1: 
            result = True
        elif direction == 'U' and arr2D[r][c] - arr2D[r+1][c] <= 1:
            result = True
        elif direction == 'R' and arr2D[r][c] - arr2D[r][c-1] <= 1: 
            result = True
        elif direction == 'L' and arr2D[r][c] - arr2D[r][c+1] <= 1:
            result = True
    
    return result

if __name__ == '__main__':
    with open('Day12Input.txt') as f:
       myList = []
       for line in f.readlines(): 
           myList.append(line.replace('\n', ''))
            
         
    #Mina rader och kolumner  
    listLen = len(myList) 
    strLen = len(myList[0]) 
    
    #initierar en tom 2D-array
    arr2D = np.zeros((listLen, strLen))
     
    
    for r in range(0, listLen): 
        for c in range(0, strLen): 
            arr2D[r][c] = convert(myList[r][c])

    print('Resultat: ' + str(distanceToStart(arr2D)))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:17:41 2022

@author: carlmagnusson
"""
# --- Day 8: Treetop Tree House ---
# Part 1
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

# Consider your map; how many trees are visible from outside the grid?

# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

# In the example above, consider the middle 5 in the second row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is not blocked; it can see 1 tree (of height 3).
# Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# Looking right, its view is not blocked; it can see 2 trees.
# Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# Looking left, its view is not blocked; it can see 2 trees.
# Looking down, its view is also not blocked; it can see 1 tree.
# Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

# Consider each tree on your map. What is the highest scenic score possible for any tree?

import numpy as np
#Funktion som tar emot en position och en array. 
def BiggestFromAnyDirection(pos, myArr): 
    
    #Initiering av variabler. 
    #börjar med att plocka ut var i arrayen vi är.
    r = pos[0]
    c = pos[1]
    
    # Värde på aktuell plats
    value = myArr[r, c]
    
    #Största värdena på aktuell rad/kolumn.
    BiggestLTR = 0 #Störst värdet left-to-right
    BiggestRTL = 0 #Största värdet right-to-left
    BiggestUD = 0 #Största värdet up-down
    BiggestDU = 0 #Största värdet down-up
    
    #Resultat
    result = 0
    
    #Börjar med att plocka fram största värdet på aktuell rad, från vänster till höger
    for cf in range(0, c): 
        if myArr[r, cf] > BiggestLTR:
            BiggestLTR = myArr[r, cf]
        
    #Tar fram största värdet på aktuell rad, höger till vänster
    for cf in range(c+1, len(myArr[0])):
        if myArr[r, cf] > BiggestRTL: 
            BiggestRTL = myArr[r, cf]

    #Tar fram största värdet i kolumnen uppifrån och nedan
    for rf in range(0, r): 
        if myArr[rf, c] > BiggestUD:
            BiggestUD = myArr[rf, c]
            
    #Tar fram största värdet i kolumnen nedifrån och upp
    for rf in range(r+1, len(myArr)): 
        if myArr[rf, c] > BiggestDU:
            BiggestDU = myArr[rf, c]
            
    #Om cellens värde är större än något av dessa fyra -> då syns trädet.
    if value > BiggestLTR or value > BiggestRTL or value > BiggestUD or value > BiggestDU:
        result = 1
        
    return result

def viewingdistance(pos, myArr): 
    r = pos[0]
    c = pos[1]
    value = myArr[r, c]
    
    R = 0
    L = 0
    U = 0 
    D = 0 
    
    #Vad kan vi se neråt?
    for rf in range(r+1, len(myArr)):
        if myArr[rf,c]>=value: 
            D +=1
            break
        else: 
            D +=1
    #print(D)
    
    #Vad kan vi se åt höger? 
    for cf in range(c+1, len(myArr[r])): 
        #print(myArr[r, cf])
        if myArr[r, cf] >= value: 
            R += 1
            break
        else: 
            R += 1
    #print(R)
    #Vad kan vi se uppåt? 
    for rf in range(r-1, -1, -1): 
        if myArr[rf, c] >= value: 
            U += 1
            break
        else: 
            U += 1
    #print(U)
    
    #Vad kan vi se åt vänster? 
    for cf in range(c-1, -1, -1): 
        if myArr[r, cf] >= value: 
            L += 1
            break
        else: 
            L += 1
    #print(L)
    return U*L*R*D
    

if __name__ == '__main__':
    
    myArr = []
    myList = []
    internaltrees = 0
    
    with open('day8.txt') as f: 
        #Läser in filen, och lägger till mellanrum mellan siffrorna för att skapa en multidimensionell lista
        for line in f: 
            res = ' '.join(line)
            res = res.rstrip()
            myList.append(res.split(' '))
         
    #Tar resultatet från min lista och lägger i en 2D-array. 
    #Beräknar antal rader och kolumner. 
    myArr = np.array(myList, dtype = int)
    rows = len(myArr)
    cols = len(myArr[0])
    
    #För part 2, skapar vi en tom lista som ska innehålla alla trädens viewingdistance. 
    viewingdistance_list = []
    #Börjar med att räkna ut antal träd som befinner sig längs kanterna. 
    Edges = (rows + cols - 2)*2
    
    #Loopar igenom min array men bortser från kanterna. 
    #Denna loop fungerar för part 2, då viewingdistance blir 0 för kanterna. 
    for r in range(1, rows-1): 
        for c in range(1, cols-1):
            #Kallar på funktionerna ovan
            internaltrees += BiggestFromAnyDirection([r, c], myArr)
            viewingdistance_list.append(viewingdistance([r, c], myArr))
               
    print('Resultat part 1: ' + str(internaltrees + Edges))
    print('Resultat part 2: ' + str(max(viewingdistance_list)))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:09:50 2022

@author: carlmagnusson
"""
# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

#  --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?  

# Importerar bibliotek
import pandas as pd
import re
     
# Funktion som tar emot en lista, hur många som ska flyttas, vilken sublista som objekten ska flyttas från och till.

def moveblocks(version, Blocks, numberofblocks, movefrom, moveto): 
    
    # I version 1 av problemet så flytas blocken 1 och 1. 
    if version == 1:
        for i in range(0, numberofblocks): 
            Block = Blocks[movefrom].pop(0)
            Blocks[moveto].insert(0, Block)
    # I version 2 av problemet kan flera objekt flyttas samtidigt och dessutom behålla sin ursprungliga ordning. 
    elif version == 2: 
        #get sublist. 
        Block_sublist = Blocks[movefrom][0:numberofblocks]
        #Remove from the original list
        del Blocks[movefrom][0:numberofblocks]

        for i in range(0, numberofblocks): 
            Block = Block_sublist.pop()
            Blocks[moveto].insert(0, Block)
            
# Funktion som tar emot en lista, hur många som ska flyttas, vilken sublista som objekten ska flyttas från och till.


    
    
if __name__ == '__main__':
    
    #Input 
    #     [P]                 [Q]     [T]
    # [F] [N]             [P] [L]     [M]
    # [H] [T] [H]         [M] [H]     [Z]
    # [M] [C] [P]     [Q] [R] [C]     [J]
    # [T] [J] [M] [F] [L] [G] [R]     [Q]
    # [V] [G] [D] [V] [G] [D] [N] [W] [L]
    # [L] [Q] [S] [B] [H] [B] [M] [L] [D]
    # [D] [H] [R] [L] [N] [W] [G] [C] [R]
    #  1   2   3   4   5   6   7   8   9 
    
    #Version 1
    Blocks = [
    ['F', 'H', 'M', 'T', 'V', 'L', 'D'],
    ['P', 'N', 'T', 'C', 'J', 'G', 'Q', 'H'],
    ['H', 'P', 'M', 'D', 'S', 'R'],
    ['F', 'V', 'B', 'L'],
    ['Q', 'L', 'G', 'H', 'N'],
    ['P', 'M', 'R', 'G', 'D', 'B', 'W'],
    ['Q', 'L', 'H', 'C', 'R', 'N', 'M', 'G'],
    ['W', 'L', 'C'],
    ['T', 'M', 'Z', 'J', 'Q', 'L', 'D', 'R']]
    
    #Öppnar filen inehållandes förflyttningar
    with open('Day5.txt') as f:
        #Loopar igenom filen
        for line in f:
            #Skapar lista över vilka siffror som finns i texten. 
            numbers =  re.findall(r'\d+', line)
            
            # Antal kommer först
            numberofblocks = int(numbers[0])
            
            #Sedan från
            movefrom = int(numbers[1])-1
            
            #Till slut, vart vi ska flytta de
            moveto = int(numbers[2])-1
            
            #Anrop till funktion ovan med version = 1
            moveblocks(1, Blocks, numberofblocks, movefrom, moveto)
        
    #Version 2
    Blocks_v2 = [
    ['F', 'H', 'M', 'T', 'V', 'L', 'D'],
    ['P', 'N', 'T', 'C', 'J', 'G', 'Q', 'H'],
    ['H', 'P', 'M', 'D', 'S', 'R'],
    ['F', 'V', 'B', 'L'],
    ['Q', 'L', 'G', 'H', 'N'],
    ['P', 'M', 'R', 'G', 'D', 'B', 'W'],
    ['Q', 'L', 'H', 'C', 'R', 'N', 'M', 'G'],
    ['W', 'L', 'C'],
    ['T', 'M', 'Z', 'J', 'Q', 'L', 'D', 'R']]
    
    with open('Day5.txt') as f:
        for line in f:
            #Skapar lista över vilka siffror som finns i texten. 
            numbers =  re.findall(r'\d+', line)
            
            # Antal kommer först
            numberofblocks = int(numbers[0])
            
            #Sedan från
            movefrom = int(numbers[1])-1
            
            #Till slut, vart vi ska flytta de
            moveto = int(numbers[2])-1
            
            #Anrop till funktion ovan med version = 2
            moveblocks(2, Blocks_v2, numberofblocks, movefrom, moveto)
            

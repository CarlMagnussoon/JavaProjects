#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:18:32 2022

@author: carlmagnusson
"""
# --- Day 3: Rucksack Reorganization ---
# One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

# The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

# The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

# For example, suppose you have the following list of contents from six rucksacks:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.
# To help prioritize item rearrangement, every item type can be converted to a priority:

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

# Importerar bilbiotek som behövs
import pandas as pd

# Läser från vår csv-fil. 
df = pd.read_csv('Rucksacks.csv', sep = ';')

#Info om vår dataframe
df.info()
size = len(df)

# Använda nedanstående sträng för att få ut poängen på ett lätt vis.
Alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Part 1
#Skapa ny kolumn som innehåller vilket gemensamt tecken delsträngarna har. 
df['Common Letter'] = 0
# Kolumn för att lagra poängen. 
df['points'] = 0

#LLoopar igenom df för att dela strängen på hälften och hitta gemensamt tecken. 
for x in range (0, size): 
    
    #pick out string in the current cell
    str_str = df['Rucksack'][x]
    
    #Size of the string
    str_size = len(str_str)
    
    #try to divide the string into 2 separate strings
    try: 
        str_half = int(str_size/2)
        str1 = str_str[0:str_half]
        str2 = str_str[str_half:str_size]
        
        Commonletter = list(set(str1)&set(str2))
        
        df['Common Letter'][x] = ''.join(Commonletter)
        
    except: 
        print('The string does not contain an even number of characters.')
        
# Loopar igenom dataframen igen och sätter poäng 
for x in range (0, size): 
    #Reset
    points = 0
    
    #Pick out the character
    character = df['Common Letter'][x]
    
    #Get the index of the character in the string to get the point
    points = Alphabet.index(character) + 1
    
    #Insert into dataframe
    df['points'][x] = points
    
#Poängen
totalpoints = df['points'].sum()
print(totalpoints)

# --- Part Two ---
# As you finish identifying the misplaced items, the Elves come to you with another issue.

# For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

# The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

# Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

# Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# And the second group's rucksacks are the next three lines:

# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

# Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

# Ny kolumn som innehåller den gemensamma bokstaven i de tre raderna. 
# Ny kolumn som innehåller grupppoängen
# Variabel som håller grupppoängen. 
df['Common Letter Group'] = 0
df['grouppoints'] = 0
grouppoints  = 0


#Seperate the rows into groups of 3. 
for x in range (0, size, 3): 
    
    str1 = df['Rucksack'][x]
    str2 = df['Rucksack'][x+1]
    str3 = df['Rucksack'][x+2]
    
    Commonletter = list(set(str1)&set(str2)&set(str3))
    
    df['Common Letter Group'][x] = ''.join(Commonletter)
    df['Common Letter Group'][x+1] = ''.join(Commonletter)
    df['Common Letter Group'][x+2] = ''.join(Commonletter)
    

for x in range(0, size): 
    #reset points
    grouppoints = 0 
    
    character = df['Common Letter Group'][x]
    
    grouppoints = Alphabet.index(character) + 1
    
    df['grouppoints'][x] = grouppoints
    
totalgrouppoints = int(df['grouppoints'].sum()/3)
print(totalgrouppoints)
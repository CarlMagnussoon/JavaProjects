#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:16:07 2022

@author: carlmagnusson
"""

# --- Day 7: No Space Left On Device ---
# You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

# The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

# $ system-update --please --pretty-please-with-sugar-on-top
# Error: No space left on device
# Perhaps you can delete some files to make space for the update?

# You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.
# Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
# Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

# Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

# The total sizes of the directories above can be found as follows:

# The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
# The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
# Directory d has total size 24933642.
# As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?



# Behöver "bygga" upp min filstruktur, från min input. 
#Importerar bibliotek som kan hantera heirarkisk struktur,
from anytree import Node

#Skapar en lista med alla strängar i filen
with open('Day7input.txt') as f: 
    lines = [line.rstrip() for line in f]

#Skapar upp en dict som ska innehålla min struktur. 
#Dicten innehåller en lista för directories, en för filerna och en för "rooten"
filestructure = {'directories': [], 'files': [], 'root': Node('root', size = 0)}

#Initierar vilken som är den nuvarande noden. 
current = filestructure['root']

#For-loop som går igenom min listan av input.
for curr_line in lines: 
    
    #Skapar en lista där vi delar upp strängen i substrängar.
    curr_line_list = curr_line.split(' ')
    
    #Om det är userinput
    if curr_line_list[0] == '$':
        
        #Om vi ska byta directory
        if curr_line_list[1] == 'cd':
            
            #Vilken directory ska vi byta till?
            cd_to = curr_line_list[2]
            
            #Om det är root, sätt nuvarande till root
            if cd_to == '/':
                current = filestructure['root']
                
            #om vi ska backa 1 steg, plocka ut nuvarande nodens förälder.
            elif cd_to == '..': 
                current = current.parent
                
            # Annars loopar vi igenom barn-noderna till den nod vi befinner oss i. 
            else: 
                for d in current.children: 
                    #Om namnet på barnnoden motsvarar dit vi ska, sätt current till denna nod. 
                    if d.name == cd_to: 
                        current = d
                        break
                    
        #om vi ska lista så vill vi inte göra något. 
        elif curr_line_list[1] == 'ls':
            continue
    # Om nuvarande sträng inte börjar med $ ska vi lägga till noder. 
    else: 
        #Om strängen börjar med dir, ska vi skapa en ny nod och lägga till den i vår directories-lista.
        if curr_line_list[0] == 'dir': 
            filestructure['directories'].append(Node(curr_line_list[1], parent = current, size = None))
        #Annars skapar vi en ny nod i vår files-lista. 
        else: 
            filestructure['files'].append(Node(curr_line_list[1], parent=current, size=int(curr_line_list[0])))


# Rekursiv funktion. 
# Funktionen tar emot vår dict och en "startnod". 
def calculatesize(filestructure, directory):
    #initierar en size = 0
    dir_size = 0
    
    #loopar igenom nodens barnnoder. 
    for child_directory in directory.children:
        
        #Om barnnodens storlek = 0, Barnet är en directory. 
        #Kalla på funktionen igen med barnnoden.
        if child_directory.size is None:
            child_directory.size = calculatesize(filestructure, child_directory)
            
        #Öka nodens storlek med alla barn nodernas filstorlekar.
        dir_size += child_directory.size
        
    return dir_size


#Kör funktionen med startnod = root
#Detta sätter ett värde på size för varje directory i vår dict. 
filestructure['root'].size = calculatesize(filestructure, filestructure['root'])


part_1 = 0
space_needed = 30000000 - (70000000 - filestructure['root'].size)
smallest_dir_size = filestructure['root'].size

for directory in filestructure['directories']:
    
    if directory.size <= 100000:
        part_1 += directory.size
        
    if space_needed <= directory.size < smallest_dir_size:
        smallest_dir_size = directory.size

print("Part 1:", part_1)
print("Part 2:", smallest_dir_size)
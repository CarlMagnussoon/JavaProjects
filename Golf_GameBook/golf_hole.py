#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:50:50 2023

@author: carlmagnusson
"""

class golf_hole(): 
    # "PK" blir nummer i detta fall. 
    def __init__(self, number, par, index): 
        self.number = number
        self.par = par
        self.index = index
        self.extra_strokes = 0
        self.score = None 
        
    def __str__(self): 
        return ('Hål: ' + str(self.number) + '. Par: ' + str(self.par) + '. Index: ' + str(self.index)+'. Extra slag: ' + str(self.extra_strokes))
    
    def get_number(self):
        return self.number
    
    def set_number(self, number): 
        self.number = number
        
    def get_par(self):
        return self.par
    
    def set_par(self, par): 
        self.par = par
        
    def get_index(self): 
        return self.index
    
    def set_index(self, index): 
        self.index = index
        
    def get_extra_strokes(self): 
        return self.extra_strokes
    
    def set_extra_strokes(self, extra_strokes): 
        self.extra_strokes = extra_strokes
        
    def get_score(self):
        return self.score
        
    def set_score(self, score): 
        self.score = score
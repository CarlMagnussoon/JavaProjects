#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:48:26 2023

@author: carlmagnusson
"""
class player(): 
    # "PK" blir namn för denna klass
    def __init__(self, name, hcp, strokes): 
        self.name = name
        self.hcp = hcp
        self.strokes = strokes
        
    def get_name(self):
        return self.name
    
    def set_name(self, name): 
        self.name = name
        
    def get_hcp(self): 
        return self.hcp
    
    def set_hcp(self, hcp): 
        self.hcp = hcp
        
    def get_strokes(self): 
        return self.strokes
    
    def set_strokes(self, strokes):
        self.strokes = strokes
        
    def __str__(self): 
        return (self.name + ', hcp: ' + str(self.hcp) + ', antal slag: ' + str(self.strokes))
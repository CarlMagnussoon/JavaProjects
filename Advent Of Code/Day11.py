#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:19:30 2022

@author: carlmagnusson
"""
import heapq
class monkey: 
    #Varje apa har en lista med items, en operation de utför, sedan vem de kasta till om deras test visar sig vara  sant/falskt. 
    def __init__(self, InspectedItems ,Items, OperationSign, OperationNumber, Divisor, ThrowToTrue, ThrowToFalse):
        self.Items = Items
        self.OperationSign = OperationSign
        self.OperationNumber = OperationNumber
        self.ThrowToTrue = ThrowToTrue
        self.ThrowToFalse = ThrowToFalse
        self.Divisor = Divisor
        self.InspectedItems = InspectedItems
        
    def getNumberOfItems(self): 
        return len(self.Items)
    
    def inspectItems(self): 
        #vilket föremål ska vi inspektera
        ItemToInspect = self.Items.pop(0)
        self.InspectedItems += 1
        #Försök konvertera OperationNumber till en int, gå inte det så anta att det är "Old"
        try: 
           OperationNumber = int(self.OperationNumber)
        except: 
            OperationNumber = ItemToInspect
              
        #Vad har vi för operation under inspektion?
        if self.OperationSign == '*':
            ItemToInspect *= OperationNumber 
            
        elif self.OperationSign == '/': 
            ItemToInspect /= OperationNumber
            
        elif self.OperationSign == '-': 
            ItemToInspect -=  OperationNumber
            
        elif self.OperationSign == '+': 
            ItemToInspect +=  OperationNumber
        
        return int(ItemToInspect)
    
    #Funktion som avgör vem apan kommer kasta till. 
    def throwItemTo(self, ItemToThrow): 
        ThrowTo = 0
        
        if ItemToThrow%self.Divisor == 0: 
            ThrowTo = self.ThrowToTrue
        else: 
            ThrowTo =self.ThrowToFalse
            
        return ItemToThrow, ThrowTo
        
    def addItemToList(self, Item): 
        self.Items.append(Item)
        return
    
    def returnNumberOfItemsInspected(self): 
        return self.InspectedItems
    
if __name__ == '__main__':
    
    #Skapa upp aporna. 
    #Skapa upp en lista med aporna i. 
    #loopa igenom aporna i en for-loop som, med hjälp av while-loopen tömmer listorna. 
    monkey0 = monkey(0, [77, 69, 76, 77, 50, 58], '*', '11', 5, 1, 5)
    monkey1 = monkey(0, [75, 70, 82, 83, 96, 64, 62], '+', '8', 17, 5, 6)
    monkey2 = monkey(0, [53], '*', '3', 2, 0, 7)
    monkey3 = monkey(0, [85, 64, 93, 64, 99], '+', '4', 7, 7, 2)  
    monkey4 = monkey(0, [61, 92, 71], '*', 'Old', 3, 2, 3)
    monkey5 = monkey(0, [79, 73, 50, 90], '+', '2', 11, 4, 6)
    monkey6 = monkey(0, [50, 89], '+', '3', 13, 4, 3)
    monkey7 = monkey(0, [83, 56, 64, 58, 93, 91, 56, 65], '+', '5', 19, 1, 0)
    
    monkeys = []
    ThrowTo = 0
    
    #Lägger till mina apor i min aplista
    monkeys.append(monkey0)
    monkeys.append(monkey1)
    monkeys.append(monkey2)
    monkeys.append(monkey3)
    monkeys.append(monkey4)
    monkeys.append(monkey5)
    monkeys.append(monkey6)
    monkeys.append(monkey7)
    
    for r in range(0, 10000): 
        for i in range(0, len(monkeys)):
            while monkeys[i].getNumberOfItems() > 0: 
                ItemToThrow, ThrowTo = monkeys[i].throwItemTo(monkeys[i].inspectItems())
                #print(ThrowTo)
                #ThrowTo -= 1
                monkeys[ThrowTo].addItemToList(ItemToThrow)
            
    numberOfItemsInspected = []
    
    for i in range(0, len(monkeys)): 
        numberOfItemsInspected.append(monkeys[i].returnNumberOfItemsInspected())
    
    highest = heapq.nlargest(2, numberOfItemsInspected)
    
    print('Part 1: ' + str(highest[0]*highest[1]))
    
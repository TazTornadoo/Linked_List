
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:51:50 2020

@author: janfaulstich
"""

class Node():
    
    def __init__(self, data):
        #we create our Node, which is like a box
        #the box consists of an item and a pointer, pointing to the next item
        
        self.item = data #in this variable is the number stored
        
        self.next_item = None #thats the pointer to the next Node

class Linked_List_():
    
    def __init__(self):
        
        #the next item pointer points to this variable
        #the LinkedList class and the Node class are our construct
        #to build the Linked List with our functions
        self.head = None
        
    
    #the insert_at_beginning function always inserts a new element at the beginning
    #this is the fastest way to insert a new element to the Linked List
    def insert_at_beginning(self, data):
        
    #if the head is None, create the head of the linked List
      if self.head == None:
          self.head = Node(data)
          
    #else create a new Node with data, take the head of the previous data
    #and new_node.next_data points to the previous header
    #and create a new header
      else:
 
        #this creates a variable pointing to our new created node, filled with data
        new_node = Node(data)
          
        #this sets the pointer of the nex node to LinkedList box of the previous Node
        new_node.next_item = self.head
        
        #the head construct/variable of our Linked List points to our new node now
        self.head = new_node
    
    
    #by calling this function we can insert into our Linked List anywhere
    def insert_after_item(self, x, data):

    #n points to self.head so its better readable
        n = self.head
    
    #if our head of the Linked List is not None take the , otherwise go iterative over the Linked List
    #until we find the head to insert it at
        while n is not None:
            if n.item == x:
                break
            n = n.next_item
            
        if n is None:
            print("Not possible")
            return False
        else:
            #creates a new Node with our data we want to insert
            new_node = Node(data)
            
            #the pointer of our new Node, points to the point where 
            #the previous Node  pointer points to
            new_node.next_item = n.next_item
            
            #the pointer of the previous Node points now to our new Node
            n.next_item = new_node
        
    def print_linked_list(self): 
        temp = self.head 
        while (temp): 
            print(temp.item) 
            temp = temp.next_item

            

        

###############
#Visualization#
###############


import time


import matplotlib.pyplot as plt

llist = Linked_List_()  


time_results = []

items = []

i = 1000


while i <= 1024000:
    
    list_ = list(reversed(range(0,1000)))
    
    for number in list_:
        
        llist.insert_at_beginning(number)
        
    start_time = time.time()
    
    llist.insert_after_item(900, -10)
    
    end_time = time.time()
    
    total_time = end_time - start_time
                     
    time_results.append(total_time)
    
    items.append(i)
    
    i = i * 2
    


plt.plot(items, time_results, marker='.', label ='Time Complexity - Insertion LL')























   
          


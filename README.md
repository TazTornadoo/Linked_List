# Linked_List
This repository contains the Linked List as py-file.
The Linked List consists of two classes. The Linked List and the Node class which build our Linked List data structure.
The Node class contains the stored data and a pointer, pointing to the next node.
The Linked List class contains a head which points to the class Node. Additionally, the Linked List also has three functions.
A function to insert each Node right at the beginning, a function to insert a new Node between two Nodes of a Linked List and a print function which prints the Linked List.

After that I visualized the time complexity of the insert_after_item function in a chart.
The time complexity is measured by inserting an element in an already existing Linked List. 
These Linked List sizes start at 1000 elements and double each iteration until the size of 1.024.000 elements.
In all if these different lists, the elements get inserted always at the same place.
This results in a time complexity of O(1), since it always takes the same amount of time to insert an element at the same position.

Cheers,
Jan

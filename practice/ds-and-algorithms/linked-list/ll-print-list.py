def print_list(self):
    temp = self.head # Points to the head node
    while temp is not None: # meaning temp is is not at the end of the list
        print(temp.value) # prints node
        temp = temp.next #moves to next node in the list 


head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# This is how you would print a dictornary list
# This will print the number 23
print(head['next']['next']['value'])

#This will only run with a linked list
# print(my_linked_list.head.next.next.value)




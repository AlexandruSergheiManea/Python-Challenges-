# import module
from tabulate import tabulate
 
# assign data
mydata = [
    ["Is it mutable? ", "Yes", "Yes", "No"],
    ["Can we change the size after creation? ", "No", "Yes", "No"],
    ["Can items in the list be changed? ", "Yes", "Yes", "No"],
      ["How many different types of data can be stored ", "Multiple", "Just one", "Many"]
]
 
# create header
head = ["questions", "List", "Array", "Tuple"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))

import math

def suggest(product_idea):
    if len(product_idea) 
    raise ValueError ("Your idea must be more than 2 characters long")
    return product_idea + "inator"

try:
    product_idea = int(input("What is a good product name?  ")
    suggested = suggest(product_idea)
except ValueError as err:
       print("No")
       print("({})".format(err))
else:
     print("{}".format(suggested))                     
                          
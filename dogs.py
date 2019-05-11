info = "I love dogs so I would like to start a project on them."
print(info)
print(" ")
favorite = input("Who is your favorite dog?  ")
print(favorite, "is an amazing dog!")
if favorite == "Jolie" :
    print(favorite, "is also my favorite dog!")
elif favorite == "Nelly" :
    print(favorite, "is my sister's favorite dog!")
else : 
    # this is for older pups
    age = int(input("How old is {}?   ".format(favorite)))
    if age > 10 :
        print("Wow, I can't beleive {} is older than 10!".format(favorite))
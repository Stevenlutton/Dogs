import math

def split_check(total, number_of_people):
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person

amount_due = split_check(84.97, 4)
print("Each person owes ${}".format(amount_due))
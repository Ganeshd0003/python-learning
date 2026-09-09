nos = [1,0.22,33,4,500,6,7,89,9,10,11,13]

def is_greater_than9(x):
    if x>9:
        return True
    else:
        return False

new_nos = list(filter(is_greater_than9, nos))
print(new_nos)
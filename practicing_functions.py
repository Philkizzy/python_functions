# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)





max_num(90, 98, 56)
#expected_output: 56

# Write a Python function called mult_list() to multiply all the numbers in a list.
 
def mult_list(*args):
    prod = 1
    for i in args:
        prod = prod * i
    print(prod)



mult_list(3, 4, 2, 4, 5)
#expected_output: 480
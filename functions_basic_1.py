#For each of the following code snippets, first predict the output (what you will see printed to the terminal). Once you've made a prediction, run the code snippet to see if you are correct!

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# This function should return 5

#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triagle_sides() + number_of_military_branches)
# This will return an error, "number_of_days_in_a_week_silicon_or_triagle_sides() is not defined"

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# This will return 5, wont be able to return 10, because as soon as it hits the first return statement it exists the function.

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# This will return 5, it ignores the first print statement because it has exited the function when reaching the return statement.

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# it will return the print statement 5, but x will be nothing, since nothing is being passed into the function

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# this will add the numbers together and return 3 and 5. afterwards it will error out NoneTypes

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# it will concatenate the two arguments that are being passed in. "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# this will print b which equals to 100 and else statement in the function which is 10.

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# the first print statement will return 7
# the second print statement will return 14
# the third print statement will return 21 since it adds the final numbers together

#10
def addition(b,c):
    return b + c
    return 10
print(addition(3,5))
#this will return the addition of the passed in arguments which is 8

#11
b = 500
print(b)
def foobar():
    b = 300 
    print(b)
print(b)
foobar()
print(b)
#first print statement will be 500
#second print statement will be 500
#third print statement will be 300
#fourth print statement will be 500

#12
b = 500
print(b)
def foobar1():
    b = 300
    print(b)
    return b
print(b)
foobar1()
print(b)
#first print statement will be 500
#second print statement will be 300
#third print statement will be 500
#fourth print statement will be 500

#13
b = 500
print(b)
def foobar2():
    b = 300
    print(b)
    return b
print(b)
b = foobar2()
print(b)
#first and second print statement will retturn 500
#third and fourth will return 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# first it will run function foo() and print 1 on the next line itll see function bar() and run that to print 3, after its completed that it will go back to function foo() and print 2. 1 - 3 - 2 

#15
def foo1():
    print(1)
    x = bar()
    print(x)
def bar():
    print(3)
    return 5
y = foo1()
print(y)
# first it will run function foo() and print 1 on the next line itll see a variable x which is equal to function bar() and run that to print 3 and return 5 which x = 5, after its completed that it will go back to function foo() and print x. itll set a variable y = foo() but nothing is passed in so itll print None. 1 - 3 - 5 - None
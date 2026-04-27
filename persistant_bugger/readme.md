Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)


PLAN: 
INPUT -> STR
OUTPUT -> STR

GIVEN A NUMBER: 24
TURN TO STRING
INDEX 1 + INDEX 2 

WHILE LOOP
STORE INSIDE TO NOT NEED TO REDO STRINGIFICATION EACH TIME
AND THEN TAKE FIRST INDEX AND SECOND INDEX INTO INTS
MULTIPLY THEM - AND COUNT += 1. IF RETURNS SINGLE DIGIT COUNT += 1 
AND RETURN COUNT

WHAT IF THE USER INPUT IS MORE THAN TWO DIGITS LONG?
SUCH AS 999:


PSEUDO-CODE:
USER_INPUT = STR(NUM)
WHILE LEN(USER_INPUT) != 1:
    FOR I IN LIST(USER_INPUT):


plan:
problem 1:
given a number. How do you multiply all parts by each other when you don't know the length?

num into string into list
multiples = 1
then loop through it, and multiply each num in the list into the variable
string comprehension to do it in a line

problem 2:
How to keep multiplying the numbers until a single digit is recieved

While loop
initial_num = num
number multiplies itself, update the initial number
counter += 1 
if len(initial_num) == 1
return counter

counter += 1




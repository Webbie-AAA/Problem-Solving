Description:
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""


PLAN:
INPUT -> STRING
OUTPUT -> STRING

HOW TO DO THIS:
RANGE IS 1-10
IF 1 IN APPEND TO EMPTY STRING

PSEUDO-CODE: 

STRING CONVERTED TO LIST OF STRINGS - .SPLIT(' ')
EMPTY_STR = '' 
FOR I IN RANGE(LEN(LIST)):
    EMPTY_STR + (X FOR X IN LIST_OF_STRINGS IF I IN LIST_OF_STRINGS)
RETURN EMPTY_STR
    
    


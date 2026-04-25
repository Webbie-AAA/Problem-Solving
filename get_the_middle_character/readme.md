You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, 
return the middle character.
If the string's length is even, 
return the middle 2 characters.

Examples:

"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"


PLAN: 
Input string
Output string

How to find the middle character: find length. 
if even: 4. divide by 2. that number + 1
so 6: divide by 2 = 3. 3 + 1.   3 4 

if odd: divide by 2. 3%2=1 1 [2] 3
how to find the middle number: len(letters)/2 = middle 


Description:
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

PLAN:
There's a Counter class part of the collections module
But let's do it first with only the dictionary rules

REFRESH:
How to add key:value to a string?
empty_dict = {}
empty_dict['key'] = 'value' - that will insert new key value pairing
there's also the .count function - let me check if it works for strings or lists. Seems to work for both

1. So given a string
2. First what characters are in it: a, b, c? - create a set or the distinct function. Check if can loop through set.  You can. 
3. Then loop through each character, how many of it is in the string.
og_string.count(letter) for letter from set_letters
4. Then insert char and amount as key value pair into dict
then dict[letter] = count
5. if empty return 0


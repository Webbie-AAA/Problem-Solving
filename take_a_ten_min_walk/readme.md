Description:
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


PLAN:
INPUT : ARRAY[STRING]
OUTPUT: BOOLEAN

WHAT PINGS TRUE:
- WALK TAKES EXACTLY TEN MINUTES: 
    EACH DIRECTION COUNTS A 1
    SO EXACTLY 10 DIRECTIONS
- DIRECTION GOES BACK TO STARTING POINT
    N -> N -> N -> E -> 

    N -> UP
    E -> TURN RIGHT
    S -> DOWN
    W -> TURN LEFT

    TO GET BACK FROM UP -> GO DOWN
    TO GET BACK FROM LEFT -> GO RIGHT

MAYBE ASSIGN A POINT SYSTEM TO EACH DIRECTION:
IF N FIRST - THEN N=1, S=-1
IF E FIRST - THEN E=1, W=-1
POINTS START AT 0, AND SHOULD END AT 0
BUT ALSO INITIAL CONDITION THAT THERE SHOULD BE ONLY 10 VALUES IN THE ARRAY

CONDITIONS OF A TURN MIN WALK THAT TAKES YOU BACK TO THE STARTING POINT:
MUST HAVE EXACTLY 10 DIRECTIONS. 
THE LATTER 5 MUST BE THE REVERSE OF THE FORMER FIVE 

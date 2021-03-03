'''CCC '03 S2 - Poetry'''

# list of vowels
VOWELS = ['a', 'e', 'i', 'o', 'u']

# function to find the rhyming part of the last word
def rhyme(s):
    # iterate backwards through the word
    for i in range(1, len(s) + 1):
        if s[-i] in VOWELS: # check if the letter is a vowel
            # if it is then the substring becomes vowel to the end of the word
            s = s[-i:] 
            break

    return s

# function to find the type of poem by passing in the rhyming part of each line
def poetry(a, b, c, d):
    # four lines all rhyme
    # ie. boo, boohoo, too, foo
    if a == b == c == d:
        return 'perfect'

    # first two lines rhyme and last two lines rhyme
    # ie. though, dough, bash, cash
    elif a == b and c == d:
        return 'even'

    # first and third lines rhyme, second and fourth lines rhyme
    # ie.small, not, tall, not
    elif a == c and b == d:
        return 'cross'

    # first and fourth lines rhyme, second and third lines rhyme
    # ie.mark, teach, reach, lark
    elif a == d and b == c:
        return 'shell'
    
    # no rhymes
    # ie. see, fair, verse, rhyme
    else:
        return 'free'
    
n = int(input()) # number of verses

for i in range(n):
    
    # take the last word of each of the four lines of the verse
    w1 = input().split()[-1].lower()
    w2 = input().split()[-1].lower()
    w3 = input().split()[-1].lower()
    w4 = input().split()[-1].lower()

    # pass it through the rhyme function to get the rhyming portion 
    # then pass the rhyming portions to the poetry function
    print(poetry(rhyme(w1), rhyme(w2), rhyme(w3), rhyme(w4)))

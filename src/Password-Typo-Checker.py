from functools import lru_cache

# ALGORITHM #

def hammDist(char1, char2): # The table below holds all characters on the keyboard, with their neighboring keys
    distance_table = {
        'q' : ['w', 'a', '1'], 'w': ['2', 'e', 's', 'q'], 'e': ['3', 'r', 'd', 'w'], 'r': ['4', 't', 'f', 'e'],
        't' : ['5', 'y', 'g', 'r'], 'y': ['6', 'u', 'h', 't'], 'u': ['7', 'i', 'j', 'y'], 'i': ['8', 'u', 'o', 'k'],
        'o' : ['9', 'p', 'l', 'i'], 'p': ['0', '[', ';', 'o'], 'a': ['q', 's', 'z'], 's': ['w', 'd', 'x', 'a'],
        'd' : ['e', 'f', 'c', 's'], 'f': ['r', 'g', 'v', 'd'], 'g': ['t', 'h', 'b', 'f'], 'h': ['y', 'j', 'n', 'g'],
        'j' : ['u', 'k', 'm', 'h'], 'k': ['i', 'l', ',', 'j'], 'l': ['o', ';', '.', 'k'], 'z': ['a', 'x'],
        'x' : ['s', 'c', 'z'], 'c': ['d', 'v', 'x'], 'v': ['f', 'b', 'c'], 'b': ['g', 'n', 'v'],
        'n' : ['h', 'm', 'b'], 'm': ['j', ',', 'n'],
        'Q' : ['W', 'A', '!'], 'W': ['@', 'E', 'S', 'Q'], 'E': ['#', 'R', 'D', 'W'], 'R': ['$', 'T', 'F', 'E'],
        'T' : ['%', 'Y', 'G', 'R'], 'Y': ['^', 'U', 'H', 'T'], 'U': ['&', 'I', 'J', 'Y'], 'I': ['*', 'U', 'O', 'K'],
        'O' : ['(', 'P', 'L', 'I'], 'P': [')', '[', ';', 'O'], 'A': ['Q', 'S', 'Z'], 'S': ['W', 'D', 'X', 'A'],
        'D' : ['E', 'F', 'C', 'S'], 'F': ['R', 'G', 'V', 'D'], 'G': ['T', 'H', 'B', 'F'], 'H': ['Y', 'J', 'N', 'G'],
        'J' : ['U', 'K', 'M', 'H'], 'K': ['I', 'L', '<', 'J'], 'L': ['O', ':', '>', 'K'], 'Z': ['A', 'X'],
        'X' : ['S', 'C', 'Z'], 'C': ['D', 'V', 'X'], 'V': ['F', 'B', 'C'], 'B': ['G', 'N', 'V'],
        'N' : ['H', 'M', 'B'], 'M': ['J', '<', 'N'],
        '1' : ['2', 'q', '`'], '2' : ['3', 'w', '1'], '3' : ['4', 'e', '2'], '4' : ['5', 'r', '3'], '5' : ['6', 't', '4'],
        '6' : ['7', 'y', '5'], '7' : ['8', 'u', '6'], '8' : ['9', 'i', '7'], '9' : ['0', 'o', '8'], '0' : ['-', 'p', '9'],
        '`' : ['1', '~'], '-' : ['0', '=', '[', '_'], '=' : ['-', ']', '+'], '\\' : [']', '|'], '[' : ['-', ']', '\'', 'p', '{'], ']' : ['=', '\\', '[', '}'],
        ';' : ['p', 'l', '/', '\'', ':'], '\'' : ['[', ';', '/', '"'], ',' : ['m', 'k', '.', '<'], '.' : ['l', ',', '/', '>'], '/' : [';', '.', '\'', '?'],
        '~' : ['!'], '_' : [')', '+', '{'], '+' : ['_', '}'], '|' : ['}'], '{' : ['_', '}', '"', 'P'], '}' : ['+', '|', '{'],
        ':' : ['P', 'L', '?', '"'], '"' : ['{', ':', '?'], '<' : ['M', 'K', '>'], '>' : ['L', '<', '?'], '?' : [':', '>', '"'],
        '!' : ['@', 'Q', '~'], '@' : ['#', 'W', '!'], '#' : ['$', 'E', '@'], '$' : ['%', 'R', '#'], '%' : ['^', 'T', '$'],
        '^' : ['&', 'Y', '%'], '&' : ['*', 'U', '^'], '*' : ['(', 'I', '&'], '(' : [')', 'O', '*'], ')' : ['_', 'P', '('], '' : []
    }
    
    if char1 == char2: # If the two chars in the passwords are the same
        return 0 # No penalty, weight of 0
    elif char2 in distance_table.get(char1, []): # If s2's char is different from s1's char, and is in its dictionary entry
        return 0.49 # Minor typo, weight of 0.49
    elif char1.lower() == char2.lower(): # If the characters are the same, but different cases
        return 0.50 # Minor typo, weight of 0.49
    else: # Otherwise the two characters are too far apart to be considered common
        return 1.0 # Major typo, weight of 1.0

@lru_cache(None)
def editDist(n, m): # Utilizes Levenshtein Algorithm to calculate standard edit distance
    if n == 0: # n is the length of s1, if it is currently empty, all m chars need to be added
        return float(m) # Adds each char from s2 with a weight of 1.0
    if m == 0: # m is the length of s2, if it is currently empty, all n chars need to be added
        return float(n)  # Adds each char from s1 with a weight of 1.0
    if s1[n - 1] == s2[m - 1]: 
        return editDist(n - 1, m - 1) # Checks if the chars are equal and moves on if they are 
    
    insertCost = editDist(n, m - 1) + (0.50 if m == len(s2) else 1.0) # If inserting at the end, add weight of 0.5
    deleteCost = editDist(n - 1, m) + (0.50 if n == len(s1) else 1.0) # If deleting from the end, add weight of 0.5
    substitutionCost = editDist(n - 1, m - 1) + hammDist(s1[n - 1], s2[m - 1]) # Calculate weight based on distance table
    return min(insertCost, deleteCost, substitutionCost) # Standard Levenshein procedure, returns minimum of the above operations


# AUTOMATED TESTING FUNCTIONS #

def testRunner(testNum):
    score = editDist(len(s1), len(s2))
    print(f"Test {testNum} score: {score}")
    print(f"Test {testNum} output:")
    editDist.cache_clear() # Clears the memoized cache to ensure tests don't contaminate each other
    accessStatus(score)
    print("~~~~~~~~~~~~~~~~~~~~~")

def accessStatus(dissimilarity):
    if dissimilarity < 1.0:
        print(f"Your password had a low enough dissimilarity score! Logging you in...")
    else:
        print("Your entered password was too dissimilar, please try again.")

# TEST CASES #
# Dear Grader, please examine and tweak the test cases below as you see fit #

s1 = "Password321"
s2 = "Password321"
testRunner(1)

s1 = "NeotheOne!0!"
s2 = "NEotheOne!0~"
testRunner(2)

s1 = "qweasdzxc"
s2 = "iopjklbnm"
testRunner(3)

s1 = "mopmeC-qynfi6-faznax"
s2 = "TmopmeC_qynfi6-faznavm"
testRunner(4)

s1 = "sitting"
s2 = "kitten"
testRunner(5)

s1 = "7589403-58904'385904-387590-47328690743859-0473920-85-=043829-06843=285-=43826-=82-906589=04-32860=32][]';'/."
s2 = "mopmeC-qynfi6-faznaxajigropejgioprmkosnmgkl;fnmdkl;.nfjkl;hjvbiopr980gujrdpjig;ojkfl;dmcnkx/.l,bnmkl;fdjggiop"
testRunner(6)

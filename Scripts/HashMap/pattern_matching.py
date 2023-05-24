#Given a string and a pattern, write a program to find all occurences of the pattern in the string
#For example, string = "THIS IS A TEST TEXT", pattern = "TEST"
#Output = Pattern found at index 10

string = "AABAACAADAABAABA"
pattern = "AABA"

def patternMatch(string, pattern):
    # input check
    if len(list(string)) <= 0 or len(list(pattern)) <= 0 or (len(list(pattern)) > len(list(string))):
        print("undefined")
    
    # converting to list
    string = list(string)
    pattern = list(pattern)

    for i in range(0, len(string)): # looping over each character
        if string[i:i + len(pattern)] == pattern: # slicing index from starting pointer to equal length of the pattern array
            print(f"matched at {i} to {i + len(pattern)}")

patternMatch(string, pattern)
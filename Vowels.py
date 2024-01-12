def countA(input_str):
    vowels = 0
    consonants = 0
    spaces = 0
    
    for i in range(len(input_str)):
        ch = input_str[i]
        if (ch.isalpha()):  
            ch = ch.lower()  
            
            if (ch in ['a', 'e', 'i', 'o', 'u']):
                vowels += 1
            else:
                consonants += 1
        elif (ch.isspace()):  
            spaces += 1
    
    return vowels, consonants, spaces

result = countA("geeks for geeks121")
print("Vowels:", result[0])
print("Consonants:", result[1])
print("Spaces:", result[2])
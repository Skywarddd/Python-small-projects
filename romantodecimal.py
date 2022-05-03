letters = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}

def RomantoDecimal(romanNumeral):
    sum= 0
    for i in range(len(romanNumeral)-1):
        left= romanNumeral[i]
        right= romanNumeral[i + 1]
        if letters[left] < letters[right]:
            sum -= letters[left]
        else:
            sum += letters[left]
    sum += letters[romanNumeral[-1]]
    return sum
    
result= input("Enter a Roman number: ")    
convert= RomantoDecimal(result)
print(convert)
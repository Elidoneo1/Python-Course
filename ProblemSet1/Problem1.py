suma = 0
vocales = "aeiou"

for letter in s:
    if letter in vocales:
        suma +=1

print("Number of vowels:" + suma)
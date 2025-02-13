sumabob = 0
listabob = "bob"

for i in range(len(s)-len(listabob)+1):
    if s[i:i+len(listabob)] ==listabob:
        sumabob += 1

print("Number of times bob occurs is:", sumabob)
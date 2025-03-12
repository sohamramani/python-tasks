userinput = str(input("Enter a sentence : "))
print(userinput)
lower_char = []
lower_char_ascii = []
for a in userinput:
    if (a.isupper()) == True:
        pass
    elif (a.islower()) == True:
        lower_char.append(a)
        lower_char_ascii.append(ord(a))

print("lower case characters : ", lower_char)
print("ASCII code of the lower case characters: ", lower_char_ascii)



#%%
# Reverse input string
input_str = input('Insert String: ')
print('The reverse string is: ' + input_str[::-1])

# Reverse every line of string in txt file
f = open("string.txt","r")
for string in f:
    print('Given String is: ' + string.rstrip('\n'))
    print('The reverse string is: ' + string[::-1] + "\n")
# %%

"""
Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.
"""
#%%
# ord(a) = 97
input_str = input('Insert String: ')
input_str = input_str.lower()
count_arr = [0] * 26

for alphabet in input_str:
    if alphabet != " ":
        index = ord(alphabet) - 97
        count_arr[index]+=1

ret_str = "a: " + str(count_arr[ord('a') - 97]) + "\n"
ret_str += "e: " + str(count_arr[ord('e') - 97]) + "\n"
ret_str += "i: " + str(count_arr[ord('i') - 97]) + "\n"
ret_str += "o: " + str(count_arr[ord('o') - 97]) + "\n"
ret_str += "u: " + str(count_arr[ord('u') - 97])

print(ret_str)

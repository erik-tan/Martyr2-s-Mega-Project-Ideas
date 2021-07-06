"""
Pig latin is a game of alterations played on the English Language game
Banana -> anana-bay
"""

# Translate input string
def translate(str):
    return str[1:]+'-'+str[0]+'ay'

if __name__ == "__main__":
    ret_str = ""
    input_str = input('Insert String: ')

    for word in input_str.split():
        ret_str += translate(word) + " "

    print(ret_str)

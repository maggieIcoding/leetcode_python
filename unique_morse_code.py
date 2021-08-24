
letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

words_list = ["gin", "zen", "gig", "msg"]

# create a dict to put the items in letter_list as the keys, and items in morse_code as values:
# mapped = {}
# for i in range(0,26):
#     mapped[letter_list[i]] = morse_code[i]
# print(mapped)


def word_to_morse(word):
    letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    morse_trans = ''
    for char in word:
        morse_trans += morse_code[letter_list.index(char)]
    return morse_trans

 
words = ["gin", "zen", "gig", "msg"]

words_morse_codes = []

for word in words:
    words_morse_codes.append(word_to_morse(word)) 

print(words_morse_codes)

print(list(set(words_morse_codes)))










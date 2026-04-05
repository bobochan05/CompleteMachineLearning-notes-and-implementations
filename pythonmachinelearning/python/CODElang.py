#WAP a program to translate a given string into a secret code and vice versa
#use the following rules:
#codind: is word is atleast 3 then remove the first letter and add it to the end of the word and then add 3 random characters at the start of the word 
#else is the word is less than 3 then reverse the word 
import random
def encode_word(word):
    if len(word) >=3:
        first_letter =word[0]
        restofword=word[1:]
        randomchars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        encoded_word = randomchars + restofword + first_letter
        return encoded_word
    else:
        return word[::-1]
def decode_word(word):
    if len(word) >= 4:
      randomchars = word[:3]
      restofword = word[3:-1]
      first_letter =word[-1]
      decoded_word = first_letter + restofword
      return decoded_word
      
    else:   
        return word[::-1]
    
# Main program
print("Welcome to the secret code translator!")
print("You can encode or decode a word using the secret code rules.")
a_sk= input("Do you want to encode or decode a word? (e/d): ")
if a_sk.lower() == 'e':
    word = input("Enter a word to encode: ")
    encoded_word = encode_word(word)
    print("Encoded word:", encoded_word)
elif a_sk.lower() == 'd':
    word = input("Enter a word to decode: ")
    decoded_word = decode_word(word)
    print("Decoded word:", decoded_word)
else:
    print("Invalid option. Please enter 'e' to encode or 'd' to decode.")


    
    
        



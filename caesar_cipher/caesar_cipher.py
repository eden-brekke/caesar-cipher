import re
from caesar_cipher.corpus_loader import word_list, name_list



def encrypt(phrase, key):
  lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
  upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  # Takes first part and moves to end, shifting based on the key that was passed into the function :D
  shifted_lower_alphabet = lower_alphabet[key:] + lower_alphabet[:key]
  shifted_upper_alphabet = upper_alphabet[key:] + upper_alphabet[:key]
  
  # maketrans comparse the lower alphabet to shifted version and matches index values to tell the program which letter to change to which
  transformation = str.maketrans(lower_alphabet, shifted_lower_alphabet)
  # translate takes the maketrans return and compares to the phrase, translating it to the encrypted version of the phrase
  lower = phrase.translate(transformation)
  
  # does the same thing as the lower but with upper letters :)
  upper_transformation = str.maketrans(upper_alphabet, shifted_upper_alphabet)
  lower_and_upper = lower.translate(upper_transformation)
  
  # returns fully encrypted message with upper and lower letters but leaves symbols and numbers alone!
  return lower_and_upper
  
  

def decrypt(encrypted_text, key):
  return encrypt(encrypted_text, -key)

def crack(encrypted_text):

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            pass
            # print('not english word or name', word)

    return word_count


for phrase in candidates:
    word_count = count_words(phrase)
    percentage = int(word_count / len(phrase.split()) * 100)
    if percentage > 50:
        print(phrase, percentage)
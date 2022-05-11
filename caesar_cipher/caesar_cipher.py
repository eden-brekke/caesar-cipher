import re
from corpus_loader import word_list, name_list

def encrypt(phrase, shift):
  # okay, So I know I imported RE and I know that it's probably smarter to use RE but I'm gonna brute force my way through this. 
  normal_alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
  normal_alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  

def decrypt(encrypted_text, key):
  return encrypt(encrypted_text, -key)

def crack(encrypted_text):
  pass
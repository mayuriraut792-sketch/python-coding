word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Words are Anagrams")
else:
    print("Words are not Anagrams")
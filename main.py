# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

import string
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = "".join(word.split(" "))
    anagram = "".join(anagram.split(" "))

    word = word.lower()
    anagram = anagram.lower()

    word = word.translate(str.maketrans('', '', string.punctuation))
    anagram = anagram.translate(str.maketrans('', '', string.punctuation))

    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

print(find_anagram("Big man", "nab-mig"))
print(find_anagram('Church of Scientology', 'rich-chosen goofy cult'))
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))



    # Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    

    if len(word ) != len(anagram): return "The words are not of equal lengths"

    for char in word:
        if char not in anagram:
            return False
    return True

i = 'yes'
while i == 'yes':
    print(find_anagram("boy", "yos"))
    print(find_anagram("boy", "yob"))
    i = input('Do you want to continue (yes/no)')



"""
David Young
CSC119-479
Summary:
    Student 1: designs letters in word and programs digits of number.
    What this program does so far is to read the user input's word and lists the middle letter, the first letter, and the last letter of the word.
"""

def main():
    word = input("Enter word: ")
    print(word[0])
    print(word[-1])
    even = (len(word) % 2) == 0
    if even:
        print(word[(len(word) // 2) - 1])
    else:
        print(word[len(word) // 2])
main()
#trial inputs:
#Harry: H y r

# This method breaks up text into words for us
def break_words(text):
    words = text.split()
    return words

# Counts the number of words
def count_words(words):
    return len(words)

# Sorts the words (alphabetically)
def sortwords(words):
    words.sort()
    return words

# Takes in a full sentence and returns the sorted words
def sort_sentence(sentence1):
    word = break_words(sentence1)
    return sortwords(word)

# Prints the first word after popping it off
def print_first_word(words):
    word = words.pop(0)
    print(word)

# Prints the last word after popping it off
def print_last_word(words):
    word = words.pop(-1)
    print(word)

# Prints the first and last words of the sentence
def print_first_and_last_word(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


demitri_martin_joke = f"I used to play sports.\nThen I realized you can buy trophies. Now I am good at everything."

print("----------")
print(demitri_martin_joke)
print("----------")

bottles_of_beer = (100 + 10) -  11
print("This should be ninety-nine:", bottles_of_beer)

def sing(bottles):
    for number in reversed(range(bottles + 1)):
        if number > 0:
            print_verse(number)
        else:
            print_last_verse()

def print_verse(bottles):
    print(bottles, "bottles of beer on the wall,", end=' ')
    print(bottles, "bottles of beer.")
    print("Take one down and pass it around,", end=' ')
    print(bottles - 1, "bottles of beer on the wall.\n")

def print_last_verse():
    print("No more bottles of beer on the wall,", end=' ') 
    print("no more bottles of beer.")
    print("Go to the store and buy some more,", end=' ')
    print("99 bottles of beer on the wall.\n")

sing(bottles_of_beer)


sentence = 'I think it\'s interesting that \'cologne\' rhymes with \'alone\''

words = break_words(sentence)
sorted_words = sort_sentence(sentence)

print("\"{}\" has {} words".format(sentence, count_words(words)))
print("The words are:", words)
print("The sorted words are:", sorted_words)

print_first_word(words)
print_last_word(words)
print_first_and_last_word(sentence)


from itertools import groupby

with open('DATA/words.txt') as words_in:
    words = words_in.read().splitlines()

def by_first_letter(s):
    return s[0]

sorted_words = sorted(words, key=by_first_letter)

grouped_words = groupby(sorted_words, key=by_first_letter)
print(f"grouped_words: {grouped_words}\n")
for letter, word_list_iter in grouped_words:
    print(letter, len(list(word_list_iter)))

print('-' * 60)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'blackberry', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

sorted_fruits = sorted(fruits, key=by_first_letter)
print(f"sorted_fruits: {sorted_fruits}\n")

grouped_fruits = groupby(fruits, key=by_first_letter)

for letter, fruit_list_iter in grouped_fruits:
    print(letter, list(fruit_list_iter))


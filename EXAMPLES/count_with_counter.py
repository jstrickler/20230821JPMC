from collections import Counter

with open("../DATA/breakfast.txt") as breakfast_in:
    foods = []
    for line in breakfast_in:
        foods.append(line.rstrip())
#    foods = [line.rstrip() for line in breakfast_in]  # create list of foods with EOL removed from line

counts = Counter(foods)  # initialize Counter object with list of foods

# for item, count in counts.items():  # iterate over results
#     print(item, count)
print(counts.most_common(5))
print()

with open('../DATA/words.txt') as words_in:
    letters = [word[0] for word in words_in]
    letter_counts = Counter(letters)

print(letter_counts.most_common())
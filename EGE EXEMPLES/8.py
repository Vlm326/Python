from itertools import product


def no_three_in_a_row(word):
    return all(word[i] != word[i+1] or word[i] != word[i+2] for i in range(len(word) - 2))

def is_valid(word):
    return word[0] != 'Е' and word[-1] == 'Е' and word[5:8] == ('Е', 'Б', 'Ж') and no_three_in_a_row(word)

valid_words = 0
for prefix in product('ЕБЖ', repeat=5):
    for suffix in product('ЕБЖ', repeat=5):
        word = prefix + ('Е', 'Б', 'Ж') + suffix
        if is_valid(word):
            valid_words += 1

print(valid_words)
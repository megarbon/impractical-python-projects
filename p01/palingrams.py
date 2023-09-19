"""Find all word-pair palingrams in a dictionary file."""
from load_dictionary import load 

word_list = load('d6.txt')  

# Encuentra palingrams de pares de palabras
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()
# Ordena los palingrams por la primera palabra
palingrams_sorted = sorted(palingrams)

# Muestra la lista de palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))

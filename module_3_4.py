def single_root_words(root_word, *other_words):
    same_words = []
    other_words_low = (name.lower() for name in other_words)
    s = -1

    for i in other_words_low:
        s += 1
        if root_word.lower() in i:
            same_words.append(other_words[s])
        elif i in root_word.lower():
            same_words.append(other_words[s])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
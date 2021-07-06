def frequency_of_words(s):
    words = s.split()
    print('List of words: ')
    print(words)
    d = dict()

    for i in range(len(words)):
        if words[i] not in d:
            dict2 = {words[i]: 1}
            d.update(dict2)
        elif words[i] in d:
            count = d.get(words[i])
            dict2 = {words[i]: count + 1}
            d.update(dict2)
    print('Dict of given sentence: ')
    return d

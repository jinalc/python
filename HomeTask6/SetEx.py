# 8. WAF: uncommon_words() that takes two sentences (strings) as its arguments, and returns the
# uncommon words in both the sentences.
# [Hint: store all the in a set. Read the documentation for set.]


def uncommon_words(s1, s2):
    s1_1_words = s1.split()
    s2_2_words = s2.split()

    common = set(s1_1_words).intersection(set(s2_2_words))
    unique = set(s1_1_words).symmetric_difference(set(s2_2_words))

    print('Common: {}'.format(common))
    print('Unique: {}'.format(unique))


s1 = input('Enter sentence one: ')
s2 = input('Enter sentence two: ')
uncommon_words(s1, s2)

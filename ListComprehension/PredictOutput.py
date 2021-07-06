# Predict output of

print([i + j for i in "abc" for j in "def"])

# a) [‘da’, ‘ea’, ‘fa’, ‘db’, ‘eb’, ‘fb’, ‘dc’, ‘ec’, ‘fc’].
# b) [[‘ad’, ‘bd’, ‘cd’], [‘ae’, ‘be’, ‘ce’], [‘af’, ‘bf’, ‘cf’]].
# c) [[‘da’, ‘db’, ‘dc’], [‘ea’, ‘eb’, ‘ec’], [‘fa’, ‘fb’, ‘fc’]].
# d) [‘ad’, ‘ae’, ‘af’, ‘bd’, ‘be’, ‘bf’, ‘cd’, ‘ce’, ‘cf’].

print([i.lower() for i in "HELLO"])

# a) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’].
# b) ‘hello’
# c) [‘hello’].
# d) Hello

text = "Zero One Two Three Four Five Six Seven Eight Nine"
result = [word[0] + word[-1] for word in text.split()]
print(result)

text = "Zero One Two Three Four Five Six Seven Eight Nine"
result = [word[0] + word[-1] for word in text.split() if word[0] > word[-1]]
print(result)

text = "bangalore : city with lakes and punctures"
result = [word for word in text.split() if word.startswith(('a', 'e', 'I', 'o', 'u'))]
print(result)

word = 'synonymous'
g = ['a', 'o', 'n']
s = [ch if ch in g else '_' for ch in word]
s = ' '.join(s)
print('_' in s, s)
